from django.shortcuts import render
from management import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def reimbursement(request):
    # 从 Reimbursement 模型中获取部门选择项。
    departments = models.Reimbursement.DEPARTMENT_CHOICES
    years = range(2019, 2029)
    # 使用 render 函数渲染 'Reimbursement.html' 模板。
    # 向模板传递一个名为 'departments' 的上下文变量，其中包含部门选项。
    months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    return render(request, 'Reimbursement.html', {'departments': departments, 'months': months, 'years': years})


def get_target_data(request):
    department = request.GET.get('department')
    year = request.GET.get('year')
    reimbursement = models.Reimbursement.objects.filter(name=department, year=year).first()
    if reimbursement:
        targets = [
            reimbursement.target_jan, reimbursement.target_feb, reimbursement.target_mar, reimbursement.target_apr,
            reimbursement.target_may, reimbursement.target_jun, reimbursement.target_jul, reimbursement.target_aug,
            reimbursement.target_sep, reimbursement.target_oct, reimbursement.target_nov, reimbursement.target_dec
        ]
        return JsonResponse({'targets': targets})
    return JsonResponse({'targets': []})


@csrf_exempt  # 如果您没有设置 CSRF 令牌，可以使用此装饰器暂时禁用 CSRF 保护
def update_target_data(request):
    if request.method == 'POST':
        department = request.POST.get('department')
        year = request.POST.get('year')
        reimbursement = models.Reimbursement.objects.filter(name=department, year=year).first()
        if reimbursement:
            # 更新每个月的回款目标
            reimbursement.target_jan = request.POST.get('1月Target')
            reimbursement.target_feb = request.POST.get('2月Target')
            reimbursement.target_mar = request.POST.get('3月Target')
            reimbursement.target_apr = request.POST.get('4月Target')
            reimbursement.target_may = request.POST.get('5月Target')
            reimbursement.target_jun = request.POST.get('6月Target')
            reimbursement.target_jul = request.POST.get('7月Target')
            reimbursement.target_aug = request.POST.get('8月Target')
            reimbursement.target_sep = request.POST.get('9月Target')
            reimbursement.target_oct = request.POST.get('10月Target')
            reimbursement.target_nov = request.POST.get('11月Target')
            reimbursement.target_dec = request.POST.get('12月Target')
            # ... 更新其他月份 ...
            reimbursement.save()

            return JsonResponse({'status': 'success', 'message': '目标更新成功'})
        return JsonResponse({'status': 'error', 'message': '部门或年份未找到'})


def get_summary_data(request):
    department = request.GET.get('department')
    year = request.GET.get('year')
    reimbursement = models.Reimbursement.objects.filter(name=department, year=year).first()
    if reimbursement:
        # 计算汇总数据，例如年度目标总和
        total_target = sum([
            reimbursement.target_jan, reimbursement.target_feb, reimbursement.target_mar, reimbursement.target_apr,
            reimbursement.target_may, reimbursement.target_jun, reimbursement.target_jul, reimbursement.target_aug,
            reimbursement.target_sep, reimbursement.target_oct, reimbursement.target_nov, reimbursement.target_dec
        ])
        return JsonResponse({'total_target': total_target})
    return JsonResponse({'total_target': 0})


def get_current_targets(request):
    department_name = request.GET.get('department')
    year = request.GET.get('year')  # 使用 GET 方法获取年份

    try:
        target = models.Reimbursement.objects.get(name=department_name, year=year)
    except models.Reimbursement.DoesNotExist:
        return JsonResponse({'error': 'Department or year not found'}, status=404)

    # 创建包含每月目标的字典
    targets = {
        'janTarget': target.target_jan,
        'febTarget': target.target_feb,
        'marTarget': target.target_mar,
        'aprTarget': target.target_apr,
        'mayTarget': target.target_may,
        'junTarget': target.target_jun,
        'julTarget': target.target_jul,
        'augTarget': target.target_aug,
        'sepTarget': target.target_sep,
        'octTarget': target.target_oct,
        'novTarget': target.target_nov,
        'decTarget': target.target_dec,
    }

    return JsonResponse(targets)
