from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import M_receivableForm
from management import models


def receivable_detail(request):
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
    internal_trade_ledger = models.InternalTradeLedger.objects.get(id=_id)

    if request.method == 'POST':
        form = M_receivableForm(request.POST)
        if form.is_valid():
            # 更新内部交易台账实例的字段
            form.instance.transaction_date = internal_trade_ledger.logistics_shipment_date
            form.instance.province = internal_trade_ledger.province
            form.instance.customer_name = internal_trade_ledger.company_name
            form.instance.salesperson = internal_trade_ledger.salesperson
            form.instance.accounts_receivable = internal_trade_ledger.unreceived_payment

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
        form = M_receivableForm(initial=initial_data)

    context = {
        'form': form,
        'address': 'report/inner/m_receivable_detail',
        'internal_trade_ledger': internal_trade_ledger,
    }

    return render(request, 'report_change.html',
                  {'form': form, 'context': context, 'address': 'report/inner/m_receivable_detail'})