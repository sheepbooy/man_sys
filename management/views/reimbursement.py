from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from management import models
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def reimbursement(request):
    """从数据库中得到部门和年份列表"""
    # 从 Reimbursement 模型中获取部门选择项。
    departments = models.Reimbursement.DEPARTMENT_CHOICES
    years = models.Reimbursement.objects.order_by('year').values_list('year', flat=True).distinct()
    # 使用 render 函数渲染 'Reimbursement.html' 模板。
    # 向模板传递一个名为 'departments' 的上下文变量，其中包含部门选项。
    months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
    return render(request, 'Reimbursement.html', {'departments': departments, 'months': months, 'years': years})


def get_target_data(request):
    """此函数根据用户选择的部门和年份从数据库中检索每个月的回款目标。它是一个 AJAX 调用的响应函数，用于动态更新页面上的数据。"""
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
    """根据输入的数据对指定的记录进行更新"""
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
    """计算年度目标"""
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
    """此函数根据提供的部门和年份获取当前的目标值。它可能用于初始化或更新页面上的表单字段。"""
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


def add_year_with_defaults_view(request):
    """这个函数用于处理增加新年份记录的逻辑。当用户提交新年份和默认值时，它会为指定的部门列表创建新的记录。"""
    if request.method == 'POST':
        year = request.POST.get('newYear')
        if models.Reimbursement.objects.filter(year=year).exists():
            messages.error(request, '这个年份已经存在。请重新输入。')
            return HttpResponseRedirect(reverse('reimbursement'))

        default_value = request.POST.get('defaultValue')
        print(year)
        print(default_value)

        departments = ['sales1', 'sales2', 'sales3', 'sales4', 'sales5', 'sales6', 'additives', 'rnd_service',
                       'foreign_trade']

        for dept in departments:
            # 创建新记录
            reimbursement, created = models.Reimbursement.objects.get_or_create(
                name=dept, year=year,
                defaults={
                    'target_jan': default_value, 'target_feb': default_value,  # 等等，为每个月设置默认值
                    'target_mar': default_value, 'target_apr': default_value,
                    'target_may': default_value, 'target_jun': default_value,
                    'target_jul': default_value, 'target_aug': default_value,
                    'target_sep': default_value, 'target_oct': default_value,
                    'target_nov': default_value, 'target_dec': default_value
                    # 其他字段根据需要设置
                }
            )

        messages.success(request, '年份及默认值添加成功！')
        return HttpResponseRedirect(reverse('reimbursement'))  # 重定向到一个成功页面或列表页面

        # 如果不是 POST 请求，显示表单或重定向
    return render(request, 'Reimbursement.html')
