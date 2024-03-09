from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.db.models import Q

from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import inner_trade_ledger_form
from management import models


@permission_required('management.view_internaltradeledger', login_url='/warning/')
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

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'inner_trade_ledger.html', context)


def x_month_inner_trade_ledger(request):
    """根据 sales_month 进行查询"""
    value = request.GET.get('q', '')
    value1 = request.GET.get('q1', '')
    value2 = request.GET.get('q2', '')

    query = Q()
    if value:
        query &= Q(sales_month__icontains=value)
    if value1:
        # 假设 value1 对应的查询条件
        query &= Q(salesperson__icontains=value1)
    if value2:
        # 假设 value2 对应的查询条件
        query &= Q(product_name__icontains=value2)

    query_set = models.InternalTradeLedger.objects.filter(query)

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    # 进行分页等后续处理，保持不变
    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value,
        'value1': value1,
        'value2': value2
    }
    return render(request, 'm_inner_trade_ledger.html', context)


@permission_required('management.add_internaltradeledger', login_url='/warning/')
def inner_trade_ledger_add(request):
    """内贸部台账表添加"""
    if request.method == 'GET':
        form = inner_trade_ledger_form()
        return render(request, 'change.html', {'form': form, 'address': 'innertrade/ledger'})

    form = inner_trade_ledger_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/innertrade/ledger/')

    return render(request, 'change.html', {'form': form, 'address': 'innertrade/ledger'})


@permission_required('management.change_internaltradeledger', login_url='/warning/')
def inner_trade_ledger_edit(request, _id):
    """编辑内贸部台账信息"""
    row_object = models.InternalTradeLedger.objects.filter(id=_id).first()

    if request.method == 'GET':
        form = inner_trade_ledger_form(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': 'innertrade/ledger'})

    form = inner_trade_ledger_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/innertrade/ledger/')

    return render(request, 'change.html', {'form': form, 'address': 'innertrade/ledger'})


@permission_required('management.delete_internaltradeledger', login_url='/warning/')
def inner_trade_ledger_delete(request, _id):
    """内贸部台账表删除"""
    models.InternalTradeLedger.objects.filter(id=_id).delete()
    return redirect('/innertrade/ledger/')
