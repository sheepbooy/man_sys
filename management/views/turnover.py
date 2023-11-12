from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import CustomerFlow_form
from management import models


def turnover(request):
    """研发部客户流水表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.CustomerFlow._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.CustomerFlow.objects.filter(query)
    else:
        query_set = models.CustomerFlow.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }

    return render(request, 'turnover.html', context)


def turnover_add(request):
    """研发部客户流水表添加"""
    if request.method == 'GET':
        form = CustomerFlow_form()
        return render(request, 'turnover_add.html', {'form': form})

    form = CustomerFlow_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/develop/turnover/')

    return render(request, 'turnover_add.html', {'form': form})


def turnover_edit(request, _id):
    """编辑研发部客户流水表"""
    row_object = models.CustomerFlow.objects.filter(customer_id=_id).first()
    if request.method == 'GET':
        form = CustomerFlow_form(instance=row_object)
        return render(request, 'turnover_edit.html', {'form': form})

    form = CustomerFlow_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/develop/turnover/')

    return render(request, 'turnover_edit.html', {'form': form})


def turnover_delete(request, _id):
    """删除研发部客户流水信息"""
    models.CustomerFlow.objects.filter(customer_id=_id).delete()
    return redirect('/develop/turnover/')
