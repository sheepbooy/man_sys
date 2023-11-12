from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import EmployeesForm
from management import models


def employees_list(request):
    """所有员工信息表"""
    value = request.GET.get('q', '')
    # 创建一个空的Q对象
    if value is not None:
        query = Q()
        # 获取模型的字段列表
        fields = models.Employees._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "id":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.Employees.objects.filter(query)
    else:
        query_set = models.Employees.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }

    return render(request, 'employees_list.html', context)


def employees_add(request):
    """员工信息添加"""
    if request.method == 'GET':
        form = EmployeesForm()
        return render(request, 'change.html', {'form': form, 'address': 'employees'})

    form = EmployeesForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/employees/')

    return render(request, 'change.html', {'form': form, 'address': 'employees'})


def employees_edit(request, _id):
    """编辑员工信息"""
    row_object = models.Employees.objects.filter(work_id=_id).first()

    if request.method == 'GET':
        form = EmployeesForm(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': 'employees'})

    form = EmployeesForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/employees/')

    return render(request, 'change.html', {'form': form, 'address': 'employees'})


def employees_delete(request, _id):
    """用户删除"""
    models.Employees.objects.filter(work_id=_id).delete()
    return redirect('/employees/')


def employees_reset(request, _id):
    """重置用户密码"""
    row_object = models.Employees.objects.filter(work_id=_id).first()

    if request.method == 'GET':
        form = EmployeesForm(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': 'employees'})

    form = EmployeesForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/employees/')

    return render(request, 'change.html', {'form': form, 'address': 'employees'})