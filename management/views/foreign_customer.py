from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import foreign_customer_form
from management import models


def foreign_customer(request):
    """外贸部客户档案"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.ForeignCustomerProfile._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.ForeignCustomerProfile.objects.filter(query)
    else:
        query_set = models.ForeignCustomerProfile.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'foreign_customer_list.html', context)


def foreign_customer_add(request):
    """外贸部客户添加"""
    if request.method == 'GET':
        form = foreign_customer_form()
        return render(request, 'foreign_customer_add.html', {'form': form})

    form = foreign_customer_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/foreign/customer/')

    return render(request, 'foreign_customer_add.html', {'form': form})


def foreign_customer_edit(request, _id):
    """编辑外贸部客户信息"""
    row_object = models.ForeignCustomerProfile.objects.filter(customer_profile_number=_id).first()
    if request.method == 'GET':
        form = foreign_customer_form(instance=row_object)
        return render(request, 'foreign_customer_edit.html', {'form': form})

    form = foreign_customer_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/foreign/customer/')

    return render(request, 'foreign_customer_edit.html', {'form': form})


def foreign_customer_delete(request, _id):
    """外贸部客户删除"""
    models.ForeignCustomerProfile.objects.filter(customer_profile_number=_id).delete()
    return redirect('/foreign/customer/')
