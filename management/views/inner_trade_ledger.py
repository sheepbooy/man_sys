from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import inner_trade_ledger_form
from management import models


def inner_trade_ledger(request):
    """内贸部台账表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.InternalTradeLedger._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "id":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.InternalTradeLedger.objects.filter(query)
    else:
        query_set = models.InternalTradeLedger.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'inner_trade_ledger.html', context)


def inner_trade_ledger_add(request):
    """内贸部台账表添加"""
    if request.method == 'GET':
        form = inner_trade_ledger_form()
        return render(request, 'inner_trade_ledger_add.html', {'form': form})

    form = inner_trade_ledger_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/innertrade/ledger/')

    return render(request, 'inner_trade_ledger_add.html', {'form': form})


def inner_trade_ledger_edit(request, _id):
    """编辑内贸部台账信息"""
    row_object = models.InternalTradeLedger.objects.filter(id=_id).first()

    if request.method == 'GET':
        form = inner_trade_ledger_form(instance=row_object)
        return render(request, 'inner_trade_ledger_edit.html', {'form': form})

    form = inner_trade_ledger_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/innertrade/ledger/')

    return render(request, 'inner_trade_ledger_edit.html', {'form': form})


def inner_trade_ledger_delete(request, _id):
    """内贸部台账表删除"""
    models.InternalTradeLedger.objects.filter(id=_id).delete()
    return redirect('/innertrade/ledger/')