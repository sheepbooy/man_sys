import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from management.models import InternalTradeLedger
from django.db.models import Sum, F, IntegerField
from django.db.models.functions import TruncMonth, ExtractYear, Cast


def monthly_sales_report(request):
    """202X年-销售部-业务员-月度各品类销售金额"""
    # 获取内贸部台账中的年份列表
    years = InternalTradeLedger.objects.annotate(
        year_annotate=ExtractYear('sales_month')
    ).values_list('year_annotate', flat=True).distinct()

    # 获取选择的年份参数
    selected_year = request.GET.get('year', '')

    if selected_year:
        # 聚合查询
        sales_data = InternalTradeLedger.objects \
            .annotate(year_annotate=ExtractYear('sales_month')) \
            .filter(year_annotate=selected_year) \
            .annotate(month_annotate=TruncMonth('sales_month')) \
            .values('salesperson', 'product_name', 'month_annotate', 'region_department') \
            .annotate(total_sales=Sum('order_amount')) \
            .order_by('salesperson', 'product_name', 'month_annotate', 'region_department')
    else:
        # 如果没有选择年份，则设置 sales_data 为空列表
        sales_data = []

    # 使用 DjangoJSONEncoder 来处理日期
    sales_data_json = json.dumps(list(sales_data), cls=DjangoJSONEncoder)

    # 渲染页面并传递数据
    context = {
        'sales_data_json': sales_data_json,
        'sales_data': sales_data,
        'selected_year': selected_year,
        'years': years
    }
    return render(request, 'monthly_sales_report.html', context)


def sales_amount_report(request):
    """202X年-销售部-业务员-月度各品类销售数量"""
    # 获取内贸部台账中的年份列表
    years = InternalTradeLedger.objects.annotate(
        year_annotate=ExtractYear('sales_month')
    ).values_list('year_annotate', flat=True).distinct()

    # 获取选择的年份参数
    selected_year = request.GET.get('year', '')

    if selected_year:
        # 聚合查询
        sales_data = InternalTradeLedger.objects \
            .annotate(year_annotate=ExtractYear('sales_month')) \
            .filter(year_annotate=selected_year) \
            .annotate(month_annotate=TruncMonth('sales_month')) \
            .values('salesperson', 'product_name', 'month_annotate', 'region_department') \
            .annotate(
            total_sales_quantity=Sum(
                Cast('cash_sales_quantity', IntegerField()) +
                Cast('receivable_sales_quantity', IntegerField())
            )
        ) \
            .order_by('salesperson', 'product_name', 'month_annotate', 'region_department')
    else:
        # 如果没有选择年份，则设置 sales_data 为空列表
        sales_data = []

    # 使用 DjangoJSONEncoder 来处理日期
    sales_data_json = json.dumps(list(sales_data), cls=DjangoJSONEncoder)

    # 渲染页面并传递数据
    context = {
        'sales_data_json': sales_data_json,
        'sales_data': sales_data,
        'selected_year': selected_year,
        'years': years
    }
    print(sales_data)
    return render(request, 'sales_amount_report.html', context)
