from management import models
from django.shortcuts import render, redirect
from django.urls import reverse


def calculate_targets_and_achievements_for_department(department_name):
    # 根据部门名称获取回款目标
    try:
        target = models.Reimbursement.objects.get(name=department_name)
    except models.Reimbursement.DoesNotExist:
        target = models.Reimbursement.objects.get(name='sales1')

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

        # 获取目标值
        target_value = getattr(target, target_attr, 0)  # 使用默认值0

        # 获取实际销售数据
        actual_value = 0  # 默认为0
        actual_sales = models.ActualSales.objects.filter(department=target).first()
        if actual_sales:
            actual_value = getattr(actual_sales, actual_attr, 0)

        # 计算差额和完成比例
        difference = actual_value - target_value
        completion_ratio = round(actual_value / target_value * 100, 2) if target_value else 0  # 限制小数位数为2位

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
    selected_department = request.GET.get('department')

    if request.method == 'POST':
        # 从POST请求中提取数据
        selected_department = request.POST.get('department')
        print(selected_department)
        month = request.POST.get('month')
        new_actual_amount = request.POST.get('new_actual_amount')

        month_fields = {
            '01': 'jan', '02': 'feb', '03': 'mar', '04': 'apr',
            '05': 'may', '06': 'jun', '07': 'jul', '08': 'aug',
            '09': 'sep', '10': 'oct', '11': 'nov', '12': 'dec'
        }
        month = month_fields.get(month, month)


        # 更新数据库
        try:
            department = models.Reimbursement.objects.get(name=selected_department)
            actual_sales, _ = models.ActualSales.objects.get_or_create(department=department)
            setattr(actual_sales, f'actual_{month}', new_actual_amount)

            actual_sales.save()

        except models.Reimbursement.DoesNotExist:
            # 如果部门不存在，处理错误
            pass

        return redirect(reverse('targets-achievements') + f'?department={selected_department}')

    results = None

    results = calculate_targets_and_achievements_for_department(selected_department)

    total_target = sum(data['target'] for month, data in results.items() if results)
    total_actual = sum(data['actual'] for month, data in results.items() if results)

    return render(request, 'targets_and_achievements.html', {
        'departments': departments,
        'selected_department': selected_department,
        'results': results,
        'total_target': total_target,
        'total_actual': total_actual
    })
