from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import M_receivableForm
from management.utils.form import OverdueForm
from management.utils.form import Foreign_receivable_form
from management import models


def receivable_detail(request):
    """202X年X月应收账款明细"""
    value = request.GET.get('q', '')
    if value:
        # 创建 Q 对象来过滤 sales_month
        # 查询条件：未收款不等于0且不为空白的记录
        query = Q(logistics_shipment_date__icontains=value) & Q(unreceived_payment__isnull=False,
                                                                unreceived_payment__gt=0)
        query_set = models.InternalTradeLedger.objects.filter(query)
    else:
        query = Q(unreceived_payment__isnull=False, unreceived_payment__gt=0)
        query_set = models.InternalTradeLedger.objects.filter(query)

        # 进行分页等后续处理，保持不变
    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'y_m_receivable_details.html', context)


def receivable_detail_add(request, _id):
    """202X年X月应收账款明细增添"""
    internal_trade_ledger = models.InternalTradeLedger.objects.get(id=_id)

    # Check if a record with the given _id exists in the database
    existing_record = models.Receivable.objects.filter(internal_trade_ledger_id=_id).first()

    if request.method == 'POST':
        form = M_receivableForm(request.POST, instance=existing_record)
        if form.is_valid():
            # 更新内部交易台账实例的字段
            form.instance.transaction_date = internal_trade_ledger.logistics_shipment_date
            form.instance.province = internal_trade_ledger.province
            form.instance.customer_name = internal_trade_ledger.company_name
            form.instance.salesperson = internal_trade_ledger.salesperson
            form.instance.accounts_receivable = internal_trade_ledger.unreceived_payment
            form.instance.internal_trade_ledger_id = _id

            # 将计算值accounts_receivable_balance添加到表单实例
            form.instance.accounts_receivable_balance = form.cleaned_data.get('accounts_receivable_balance')

            # 保存表单数据到数据库
            form.save()
            return redirect('/report/inner/m_receivable_detail/')
    else:
        # 初始化表单并设置初始数据
        initial_data = {
            'transaction_date': internal_trade_ledger.logistics_shipment_date,
            'province': internal_trade_ledger.province,
            'customer_name': internal_trade_ledger.company_name,
            'salesperson': internal_trade_ledger.salesperson,
            'accounts_receivable': internal_trade_ledger.unreceived_payment,
            # 其他Receivable模型的字段可以从form.cleaned_data中获取
        }

        # 如果是 GET 请求，使用初始化的表单数据创建表单实例
        form = M_receivableForm(initial=initial_data, instance=existing_record)

    context = {
        'form': form,
        'address': 'report/inner/m_receivable_detail',
        'internal_trade_ledger': internal_trade_ledger,
    }

    return render(request, 'receivable_detail_add.html', context)


def d_overdue_detali(request):
    """截止202X年X月X日已逾期账款明细"""
    value = request.GET.get('q', '')
    if value:
        # 创建 Q 对象来过滤 sales_month
        # 查询条件：未收款不等于0且不为空白的记录
        # 创建查询条件
        query = Q(repayment_date__lte=value) & Q(accounts_receivable_balance__isnull=False,
                                                 accounts_receivable_balance__gt=0)
        query_set = models.Receivable.objects.filter(query)
    else:
        query = Q(accounts_receivable_balance__isnull=False, accounts_receivable_balance__gt=0)
        query_set = models.Receivable.objects.filter(query)

        # 进行分页等后续处理，保持不变
    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'd_overdue_detail.html', context)


def d_overdue_detali_add(request, _id):
    """添加逾期描述"""
    row_object = models.Receivable.objects.filter(id=_id).first()
    form = M_receivableForm(instance=row_object)

    # Check if a record with the given _id exists in the database
    existing_record = models.Overdue.objects.filter(received_id=_id).first()

    if request.method == 'POST':
        overdue_form = OverdueForm(request.POST, instance=existing_record)
        if overdue_form.is_valid():
            # 更新内部交易台账实例的字段
            overdue_form.instance.received_id = _id
            # 保存表单数据到数据库
            overdue_form.save()
            return redirect('/report/inner/d_overdue_detail/')
    else:
        # 初始化表单并设置初始数据
        overdue_form = OverdueForm(instance=existing_record)

    context = {
        'form': form,
        'address': 'report/inner/d_overdue_detail',
        'overdue_form': overdue_form,
    }

    return render(request, 'd_overdue_detali_add.html', context)


def foreign_receivable(request):
    """应收账款明细（外贸部）"""
    value = request.GET.get('q', '')
    if value:
        query = Q(sales_date__icontains=value) & (Q(unreceived_payment_usd__gt=0) | Q(unreceived_payment_cny__gt=0))
        query_set = models.ForeignTradeLedger.objects.filter(query)

    else:
        query = Q(unreceived_payment_usd__gt=0) | Q(unreceived_payment_cny__gt=0)
        query_set = models.ForeignTradeLedger.objects.filter(query)

    # 进行分页等后续处理，保持不变

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'foreign_receivable.html', context)


def foreign_receivable_add(request, _id):
    """应收账款明细（外贸部）增添"""
    foreign_trade_ledger = models.ForeignTradeLedger.objects.get(serial_number=_id)

    # Check if a record with the given _id exists in the database
    existing_record = models.Foreign_receivable.objects.filter(foreign_trade_ledger_id=_id).first()

    if request.method == 'POST':
        form = Foreign_receivable_form(request.POST, instance=existing_record)
        if form.is_valid():
            # 更新内部交易台账实例的字段
            form.instance.transaction_date = foreign_trade_ledger.sales_date
            form.instance.customer_name = foreign_trade_ledger.company_name
            form.instance.salesperson = foreign_trade_ledger.salesperson
            form.instance.accounts_receivable_usd = foreign_trade_ledger.unreceived_payment_usd
            form.instance.accounts_receivable_rmb = foreign_trade_ledger.unreceived_payment_cny
            form.instance.foreign_trade_ledger_id = _id
            # 保存表单数据到数据库
            form.save()
            return redirect('/report/foreign/m_receivable_detail/')
    else:
        # 初始化表单并设置初始数据
        initial_data = {
            'transaction_date': foreign_trade_ledger.sales_date,
            'customer_name': foreign_trade_ledger.company_name,
            'salesperson': foreign_trade_ledger.salesperson,
            'accounts_receivable_usd': foreign_trade_ledger.unreceived_payment_usd,
            'accounts_receivable_rmb': foreign_trade_ledger.unreceived_payment_cny,
            # 其他Receivable模型的字段可以从form.cleaned_data中获取
        }

        # 如果是 GET 请求，使用初始化的表单数据创建表单实例
        form = Foreign_receivable_form(initial=initial_data, instance=existing_record)

    context = {
        'form': form,
        'address': 'report/foreign/m_receivable_detail',
        'foreign_trade_ledger': foreign_trade_ledger,
    }

    return render(request, 'foreign_receivable_add.html', context)