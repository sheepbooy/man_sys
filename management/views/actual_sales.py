from datetime import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect

from management import models
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


def calculate_targets_and_achievements_for_department(department_name, year):
    # 根据部门名称获取回款目标
    try:
        target = models.Reimbursement.objects.get(name=department_name, year=year)
    except models.Reimbursement.DoesNotExist:
        return {}

    # 初始化结果字典
    results = {}

    # 月份字段的映射
    month_fields = {
        '01': 'jan', '02': 'feb', '03': 'mar', '04': 'apr',
        '05': 'may', '06': 'jun', '07': 'jul', '08': 'aug',
        '09': 'sep', '10': 'oct', '11': 'nov', '12': 'dec'
    }

    # 对于每个月份进行计算
    for month_num, month_abbr in month_fields.items():
        target_attr = f"target_{month_abbr}"
        actual_attr = f"actual_{month_abbr}"

        # 获取目标值，并确保其不为 None
        target_value = getattr(target, target_attr, 0) or 0  # 使用默认值0，如果为 None 则视为0

        # 获取实际销售数据，并确保其不为 None
        actual_value = 0  # 默认为0
        actual_sales = models.ActualSales.objects.filter(department=target).first()
        if actual_sales:
            actual_value = getattr(actual_sales, actual_attr, 0) or 0

        # 计算差额和完成比例
        difference = actual_value - target_value
        completion_ratio = round(actual_value / target_value * 100, 2) if target_value else 0
        # 将结果存入字典
        results[month_num] = {
            'target': target_value,
            'actual': actual_value,
            'difference': difference,
            'completion_ratio': completion_ratio,
        }

    return results


def targets_and_achievements_view(request):
    departments = models.Reimbursement.DEPARTMENT_CHOICES
    years = models.ActualSales.objects.order_by('year').values_list('year', flat=True).distinct()
    selected_department = request.GET.get('department', departments[0][0])  # 默认选择第一个部门
    selected_year = request.GET.get('year', datetime.now().year)  # 使用当前年份作为默认值

    if request.method == 'POST':
        # 从POST请求中提取数据
        selected_department = request.POST.get('department')
        # print(selected_department)
        month = request.POST.get('month')
        new_actual_amount = request.POST.get('new_actual_amount')
        year = request.POST.get('selected_year')
        print(year)
        month_fields = {
            '01': 'jan', '02': 'feb', '03': 'mar', '04': 'apr',
            '05': 'may', '06': 'jun', '07': 'jul', '08': 'aug',
            '09': 'sep', '10': 'oct', '11': 'nov', '12': 'dec'
        }
        month = month_fields.get(month, month)


        # 这里确保处理的是正确的年份
        department = models.Reimbursement.objects.get(name=selected_department, year=year)
        actual_sales, _ = models.ActualSales.objects.get_or_create(department=department, year=year)
        setattr(actual_sales, f'actual_{month}', new_actual_amount)
        actual_sales.save()

        return redirect(f"{reverse('targets-achievements')}?department={selected_department}&year={year}")

    results = calculate_targets_and_achievements_for_department(selected_department, selected_year)
    if not results:
        return render(request, 'targets_and_achievements.html', {
            'departments': departments,
            'years': years,
            'selected_department': selected_department,
            'selected_year': selected_year,
            'results': None  # 或者不传递 results
        })

    total_target = sum(data['target'] for month, data in results.items() if results)
    total_actual = sum(data['actual'] for month, data in results.items() if results)

    return render(request, 'targets_and_achievements.html', {
        'departments': departments,
        'years': years,
        'selected_department': selected_department,
        'selected_year': selected_year,  # 确保这里是 selected_year
        'results': results,
        'total_target': total_target,
        'total_actual': total_actual
    })


def add_year_with_defaults_view(request):
    """这个函数用于处理增加新年份记录的逻辑。当用户提交新年份和默认值时，它会为指定的部门列表创建新的记录。"""
    years = models.Reimbursement.objects.order_by('year').values_list('year', flat=True).distinct()

    departments = ['sales1', 'sales2', 'sales3', 'sales4', 'sales5', 'sales6', 'additives', 'rnd_service',
                   'foreign_trade']

    if request.method == 'POST':
        year = request.POST.get('yearSelect')
        if models.ActualSales.objects.filter(year=year).exists():
            messages.error(request, '这个年份已经存在。请重新输入。')
            return HttpResponseRedirect(reverse('targets-achievements'))

        default_value = request.POST.get('defaultValue')

        for dept in departments:
            # 获取对应的 Reimbursement 实例
            reimbursement = get_object_or_404(models.Reimbursement, name=dept, year=year)

            # 创建或更新 ActualSales 实例
            actualSales, created = models.ActualSales.objects.get_or_create(
                department_id=reimbursement.id,  # 使用获取到的 Reimbursement id
                year=year,
                defaults={
                    'actual_jan': default_value, 'actual_feb': default_value,  # 等等，为每个月设置默认值
                    'actual_mar': default_value, 'actual_apr': default_value,
                    'actual_may': default_value, 'actual_jun': default_value,
                    'actual_jul': default_value, 'actual_aug': default_value,
                    'actual_sep': default_value, 'actual_oct': default_value,
                    'actual_nov': default_value, 'actual_dec': default_value
                    # 其他字段根据需要设置
                }
            )

        messages.success(request, '回款默认值添加成功！')
        return HttpResponseRedirect(reverse('targets-achievements'))  # 重定向到一个成功页面或列表页面

        # 如果不是 POST 请求，显示表单或重定向
    return render(request, 'targets_and_achievements.html', {'years': years})
