from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import EmployeesForm
from management import models


def employees_list(request):
    """所有员工信息表"""
    value = request.GET.get('q', '')
    if value:
        query = Q()
        fields = models.Employees._meta.fields
        for field in fields:
            # 排除 id 和 OneToOneField 字段
            if field.name != "id" and not isinstance(field, models.OneToOneField):
                q = Q(**{f"{field.name}__icontains": value})
                query |= q

        # 特别处理 user 字段
        # 假设您想根据 User 模型的 username 进行搜索
        user_query = Q(user__username__icontains=value)
        query_set = models.Employees.objects.filter(query | user_query)
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
        # 在这里创建或更新User实例
        work_id = form.cleaned_data['work_id']
        password = form.cleaned_data['password']
        user, created = User.objects.get_or_create(username=work_id)
        if created or user.password != password:
            user.set_password(password)
            user.save()

        # 保存Employees实例
        employee = form.save(commit=False)
        employee.user = user
        employee.save()

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
        # 在这里更新User实例
        work_id = form.cleaned_data['work_id']
        password = form.cleaned_data['password']
        user = row_object.user
        if user.username != work_id or user.password != password:
            user.username = work_id
            user.set_password(password)
            user.save()

        form.save()
        return redirect('/employees/')

    return render(request, 'change.html', {'form': form, 'address': 'employees'})


def employees_delete(request, _id):
    """用户删除"""
    models.Employees.objects.filter(work_id=_id).delete()
    return redirect('/employees/')
