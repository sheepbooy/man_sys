import json
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
from management.models import InternalTradeLedger, Reimbursement
from django.db.models import Sum, F, IntegerField, Value, FloatField
from django.db.models.functions import TruncMonth, ExtractYear, Cast, Coalesce


def monthly_sales_report(request):
    """202X年-销售部-业务员-月度各品类销售金额"""
    # 获取部门选项
    departments = [('all', '全部')] + list(Reimbursement.DEPARTMENT_CHOICES)
    departments = [name for code, name in departments]

    # 获取内贸部台账中的年份列表
    years = InternalTradeLedger.objects.annotate(
        year_annotate=ExtractYear('sales_month')
    ).values_list('year_annotate', flat=True).distinct()

    # 获取选择的年份和部门参数
    selected_year = request.GET.get('year', years[0])
    selected_department = request.GET.get('department', 'all')

    # 根据年份和部门进行过滤
    query = InternalTradeLedger.objects.annotate(year_annotate=ExtractYear('sales_month'))
    if selected_year:
        query = query.filter(year_annotate=selected_year)
    if selected_department != '全部':
        query = query.filter(region_department=selected_department)

    # 获取前一年的年份
    previous_year = str(int(selected_year) - 1) if selected_year else ''

    # 在查询中处理可能的空字符串
    current_year_sales = query \
        .annotate(month_annotate=TruncMonth('sales_month')) \
        .values('salesperson', 'product_name', 'month_annotate', 'region_department') \
        .annotate(total_sales=Sum(
        Coalesce('order_amount', Value(0), output_field=FloatField())
    )) \
        .order_by('salesperson', 'product_name', 'month_annotate', 'region_department')

    # 查询前一年的销售数据
    previous_year_sales = InternalTradeLedger.objects.annotate(
        year_annotate=ExtractYear('sales_month')
    ).filter(year_annotate=previous_year) \
        .annotate(month_annotate=TruncMonth('sales_month')) \
        .values('salesperson', 'product_name', 'month_annotate', 'region_department') \
        .annotate(total_sales=Sum('order_amount'))

    # 将前一年的销售数据转换为字典以便快速查找
    previous_year_sales_dict = {
        (item['salesperson'], item['product_name'], item['month_annotate'], item['region_department']): item[
            'total_sales']
        for item in previous_year_sales}

    # 计算增量
    for item in current_year_sales:
        prev_sales = previous_year_sales_dict.get(
            (item['salesperson'], item['product_name'], item['month_annotate'], item['region_department']), 0)
        item['sales_increment'] = item['total_sales'] - prev_sales

    # 使用 DjangoJSONEncoder 来处理日期和增量数据
    sales_data_json = json.dumps(list(current_year_sales), cls=DjangoJSONEncoder)

    # 渲染页面并传递数据
    context = {
        'sales_data_json': sales_data_json,
        'sales_data': current_year_sales,  # 确保这是包含增量数据的查询集
        'selected_year': selected_year,
        'selected_department': selected_department,
        'years': years,
        'departments': departments
    }

    return render(request, 'monthly_sales_report.html', context)


def sales_amount_report(request):
    """202X年-销售部-业务员-月度各品类销售数量"""
    # 获取部门选项
    departments = [('all', '全部')] + list(Reimbursement.DEPARTMENT_CHOICES)
    departments = [name for code, name in departments]

    # 获取内贸部台账中的年份列表
    years = InternalTradeLedger.objects.annotate(
        year_annotate=ExtractYear('sales_month')
    ).values_list('year_annotate', flat=True).distinct()

    # 获取选择的年份参数
    selected_year = request.GET.get('year', years[0])
    selected_department = request.GET.get('department', 'all')

    # 根据年份和部门进行过滤
    query = InternalTradeLedger.objects.annotate(year_annotate=ExtractYear('sales_month'))
    if selected_year:
        query = query.filter(year_annotate=selected_year)
    if selected_department != '全部':
        query = query.filter(region_department=selected_department)

    # 获取前一年的年份
    previous_year = str(int(selected_year) - 1) if selected_year else ''

    # 查询当前选定年份的销售数据
    current_sales_amount = query \
        .annotate(month_annotate=TruncMonth('sales_month')) \
        .values('salesperson', 'product_name', 'month_annotate', 'region_department') \
        .annotate(
        total_sales_quantity=Sum(
            Coalesce(Cast('cash_sales_quantity', IntegerField()), Value(0)) +
            Coalesce(Cast('receivable_sales_quantity', IntegerField()), Value(0))
        )
    ) \
        .order_by('salesperson', 'product_name', 'month_annotate', 'region_department')

    # 查询前一年的销售数据
    previous_sales_amount = InternalTradeLedger.objects.annotate(
        year_annotate=ExtractYear('sales_month')
    ).filter(year_annotate=previous_year) \
        .annotate(month_annotate=TruncMonth('sales_month')) \
        .values('salesperson', 'product_name', 'month_annotate', 'region_department') \
        .annotate(
        total_sales_quantity=Sum(
            Coalesce(Cast('cash_sales_quantity', IntegerField()), Value(0)) +
            Coalesce(Cast('receivable_sales_quantity', IntegerField()), Value(0))
        )
    ) \
        .order_by('salesperson', 'product_name', 'month_annotate', 'region_department')

    # 将前一年的销售数据转换为字典以便快速查找
    previous_sales_amount_dict = {
        (item['salesperson'], item['product_name'], item['month_annotate'], item['region_department']): item[
            'total_sales_quantity']
        for item in previous_sales_amount}

    # 计算增量
    for item in current_sales_amount:
        prev_sales = previous_sales_amount_dict.get(
            (item['salesperson'], item['product_name'], item['month_annotate'], item['region_department']), 0)
        item['sales_increment'] = item['total_sales_quantity'] - prev_sales

    # 使用 DjangoJSONEncoder 来处理日期
    sales_data_json = json.dumps(list(current_sales_amount), cls=DjangoJSONEncoder)

    # 渲染页面并传递数据
    context = {
        'sales_data_json': sales_data_json,
        'sales_data': current_sales_amount,
        'selected_year': selected_year,
        'selected_department': selected_department,
        'years': years,
        'departments': departments
    }
    return render(request, 'sales_amount_report.html', context)
