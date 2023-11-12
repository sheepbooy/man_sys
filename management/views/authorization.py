from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import authorization_form
from management import models


def authorization(request):
    """授权书总表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.Authorization._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.Authorization.objects.filter(query)
    else:
        query_set = models.Authorization.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'authorization.html', context)


def authorization_add(request):
    """授权书添加"""
    if request.method == 'GET':
        form = authorization_form()
        return render(request, 'authorization_add.html', {'form': form})

    form = authorization_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/authorization/')

    return render(request, 'authorization_add.html', {'form': form})


def authorization_edit(request, _id):
    """编辑授权书总表"""
    row_object = models.Authorization.objects.filter(authorization_number=_id).first()
    if request.method == 'GET':
        form = authorization_form(instance=row_object)
        return render(request, 'authorization_edit.html', {'form': form})

    form = authorization_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/authorization/')

    return render(request, 'authorization_edit.html', {'form': form})


def authorization_delete(request, _id):
    """授权表删除"""
    row_object = models.Authorization.objects.filter(authorization_number=_id).delete()
    return redirect('/authorization/')
