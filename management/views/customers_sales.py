from management import models
from django.shortcuts import render
from django.db.models import Sum
from django.db.models import Count
from django.db.models.functions import TruncMonth, ExtractYear
from management.models import ForeignTradeLedger, InternalTradeLedger


def customers_sales(request):
    """开发目标客户数和实现销售额的统计"""
    # 获取请求的年份和月份
    selected_year = request.GET.get('year')
    selected_month = request.GET.get('month')

    # 初始化部门列表
    departments = {
        '销售一部': {'first_time_count': 0, 'sales_amount': 0},
        '销售二部': {'first_time_count': 0, 'sales_amount': 0},
        '销售三部': {'first_time_count': 0, 'sales_amount': 0},
        '销售四部': {'first_time_count': 0, 'sales_amount': 0},
        '销售五部': {'first_time_count': 0, 'sales_amount': 0},
        '销售六部': {'first_time_count': 0, 'sales_amount': 0},
        '研发和产品': {'first_time_count': 0, 'sales_amount': 0},
        '食品': {'first_time_count': 0, 'sales_amount': 0},
        '外贸部': {'first_time_count': 0, 'sales_amount': 0},
    }

    # 构建查询过滤条件
    query_filter_internal = {}
    query_filter_foreign = {}
    if selected_year and selected_month:
        query_filter_internal['sales_month__year'] = selected_year
        query_filter_internal['sales_month__month'] = selected_month
        query_filter_foreign['sales_date__year'] = selected_year  # 确保这个字段与您的模型字段相匹配
        query_filter_foreign['sales_date__month'] = selected_month

    # 一次客户数量统计
    internal_first_time = models.InternalTradeLedger.objects.filter(first_occurrence__isnull=False,
                                                                    **query_filter_internal).values(
        'region_department').annotate(first_time_count=Count('id'))
    for item in internal_first_time:
        if item['region_department'] in departments:
            departments[item['region_department']]['first_time_count'] = item['first_time_count']

    foreign_first_time_count = models.ForeignTradeLedger.objects.filter(customer_type='一次',
                                                                        **query_filter_foreign).count()
    departments['外贸部']['first_time_count'] = foreign_first_time_count

    # 销售额统计
    internal_sales = models.InternalTradeLedger.objects.filter(new__isnull=False, **query_filter_internal).values(
        'region_department').annotate(total_sales_amount=Sum('order_amount'))
    for item in internal_sales:
        if item['region_department'] in departments:
            departments[item['region_department']]['sales_amount'] = item['total_sales_amount']

    # 获取汇率
    exchange_rate_value = models.ForeignTradeLedger.objects.last().exchange_rate
    exchange_rate = float(exchange_rate_value) if exchange_rate_value else 1.0  # 提供默认汇率值

    # 外贸部销售额统计
    foreign_sales = models.ForeignTradeLedger.objects.filter(customer_type='新', **query_filter_foreign).aggregate(
        total_sales_amount_usd=Sum('order_amount_usd'), total_sales_amount_cny=Sum('order_amount_cny')
    )

    usd_sales_amount = foreign_sales.get('total_sales_amount_usd') or 0
    cny_sales_amount = foreign_sales.get('total_sales_amount_cny') or 0
    print(usd_sales_amount, cny_sales_amount)
    usd_to_cny = usd_sales_amount * exchange_rate
    total_foreign_sales = usd_to_cny + cny_sales_amount
    departments['外贸部']['sales_amount'] = total_foreign_sales

    # 添加年份和月份列表
    years = [str(year) for year in range(2020, 2024)]  # 示例年份范围，根据需要调整
    months = [str(i).zfill(2) for i in range(1, 13)]

    context = {
        'departments': departments,
        'selected_year': selected_year,
        'selected_month': selected_month,
        'years': years,
        'months': months,
    }
    return render(request, 'customers_sales.html', context)


def order_summary(request):
    # 提取内贸部的年份
    internal_years = InternalTradeLedger.objects.annotate(
        year_annotate=ExtractYear('sales_month')
    ).values_list('year_annotate', flat=True).distinct()

    print(internal_years)

    # 提取外贸部的年份
    foreign_years = ForeignTradeLedger.objects.annotate(
        year_annotate=ExtractYear('sales_month')
    ).values_list('year_annotate', flat=True).distinct()

    print(foreign_years)

    # 合并并排序年份
    years = sorted(set(list(internal_years) + list(foreign_years)))
    print(years)
    selected_year = request.GET.get('year', None)
    context = {'selected_year': selected_year, 'years': years}
    print(selected_year)

    if selected_year:
        # try:
        # 内贸部每月订单数
        internal_trade_counts = InternalTradeLedger.objects.filter(
            sales_month__year=selected_year
        ).annotate(
            month_annotate=TruncMonth('sales_month')
        ).values('month_annotate', 'region_department').annotate(
            count=Count('company_name', distinct=True)
        ).order_by('month_annotate', 'region_department')

        print(internal_trade_counts)

        # 外贸部每月订单数
        foreign_trade_counts = ForeignTradeLedger.objects.filter(
            sales_month__year=selected_year
        ).annotate(
            month_annotate=TruncMonth('sales_month')
        ).values('month_annotate').annotate(
            count=Count('company_name', distinct=True)
        ).order_by('month_annotate')

        print(foreign_trade_counts)

        # 计算每月的总订单数
        total_monthly_orders = {}
        for record in internal_trade_counts:
            month_annotate = record['month_annotate'].strftime("%Y-%m")
            total_monthly_orders[month_annotate] = total_monthly_orders.get(month_annotate, 0) + record['count']

        for record in foreign_trade_counts:
            month_annotate = record['month_annotate'].strftime("%Y-%m")
            total_monthly_orders[month_annotate] = total_monthly_orders.get(month_annotate, 0) + record['count']

        context['total_monthly_orders'] = total_monthly_orders
        context['internal_trade_department_counts'] = internal_trade_counts
        context['foreign_trade_department_counts'] = foreign_trade_counts

    return render(request, 'order_summary.html', context)
