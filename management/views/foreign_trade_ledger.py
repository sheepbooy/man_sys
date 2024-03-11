from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.db.models import Q

from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import foreign_trade_ledger_form
from management import models


@permission_required('management.view_foreigntradeledger', login_url='/warning/')
def foreign_trade_ledger(request):
    """外贸部台账表"""

    # 获取搜索字段和值
    search_fields = request.GET.getlist('fields')  # 字段列表
    search_values = request.GET.getlist('values')  # 对应的值列表

    if search_fields and search_values:
        assert len(search_fields) == len(search_values), "字段和值列表长度不一致"
        query_set = models.Products.objects.all()  # 确保是您的模型名
        for field, value in zip(search_fields, search_values):
            if field and value:
                query = Q(**{f"{field}__icontains": value})
                query_set = query_set.filter(query)
    else:
        query_set = models.Products.objects.all()

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    # 保存当前页到会话，以便后续操作后可以返回到这一页
    request.session['last_emp_page'] = request.get_full_path()

    # 准备模型字段信息传递到模板
    field_info = [(field.name, field.verbose_name) for field in models.Products._meta.fields if field.name != 'id']

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'search_fields': search_fields,
        'search_values': search_values,
        'field_info': field_info,
        'page_start_index': page_object.page_start_index,  # 添加这行
    }
    return render(request, 'foreign_trade_ledger.html', context)


def x_month_foreign_trade_ledger(request):
    """报表"""
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

    query_set = models.ForeignTradeLedger.objects.filter(query)

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
        'value2': value2,
        'page_start_index': page_object.page_start_index,  # 添加这行
    }
    return render(request, 'm_foreign_trade_ledger.html', context)


@permission_required('management.add_foreigntradeledger', login_url='/warning/')
def foreign_trade_ledger_add(request):
    """外贸部台账添加"""
    if request.method == 'GET':
        form = foreign_trade_ledger_form()
        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/foreign/ledger/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = foreign_trade_ledger_form(data=request.POST)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/foreign/ledger/')
        return redirect(last_emp_page)

    # 从会话中获取之前的页面路径，如果没有则默认回到第一页
    back_url = request.session.get('last_emp_page', '/foreign/ledger/')
    # 确保将back_url传递给模板
    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.change_foreigntradeledger', login_url='/warning/')
def foreign_trade_ledger_edit(request, _id):
    """编辑外贸部台账表"""
    row_object = models.ForeignTradeLedger.objects.filter(serial_number=_id).first()
    if request.method == 'GET':
        form = foreign_trade_ledger_form(instance=row_object)
        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/foreign/ledger/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = foreign_trade_ledger_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/foreign/ledger/')
        return redirect(last_emp_page)

    # 从会话中获取之前的页面路径，如果没有则默认回到第一页
    back_url = request.session.get('last_emp_page', '/foreign/ledger/')
    # 确保将back_url传递给模板
    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.delete_foreigntradeledger', login_url='/warning/')
def foreign_trade_ledger_delete(request, _id):
    """外贸部台账删除"""
    models.ForeignTradeLedger.objects.filter(serial_number=_id).delete()
    last_emp_page = request.session.get('last_emp_page', '/foreign/ledger/')
    return redirect(last_emp_page)
