from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import CustomerProfile_form
from management import models


def dev_custom(request):
    """研发部客户档案表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.CustomerProfile._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.CustomerProfile.objects.filter(query)
    else:
        query_set = models.CustomerProfile.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'dev_custom.html', context)


def dev_custom_add(request):
    """研发部客户档案添加"""
    if request.method == 'GET':
        form = CustomerProfile_form()
        return render(request, 'change.html', {'form': form, 'address': 'develop/customer'})

    form = CustomerProfile_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/develop/customer/')

    return render(request, 'change.html', {'form': form, 'address': 'develop/customer'})


def dev_custom_edit(request, _id):
    """编辑研发部客户档案"""
    row_object = models.CustomerProfile.objects.filter(customer_id=_id).first()
    if request.method == 'GET':
        form = CustomerProfile_form(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': 'develop/customer'})

    form = CustomerProfile_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/develop/customer/')

    return render(request, 'change.html', {'form': form, 'address': 'develop/customer'})


def dev_custom_delete(request, _id):
    """删除研发部客户信息"""
    models.CustomerProfile.objects.filter(customer_id=_id).delete()
    return redirect('/develop/customer/')
