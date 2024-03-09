from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.db.models import Q

from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import Sales_Visit_Form
from management import models


@permission_required('management.view_salesvisitreport', '/warning/')
def sales_visit_report(request):
    """销售客户拜访报告"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.SalesVisitReport._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "serial_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.SalesVisitReport.objects.filter(query)
    else:
        query_set = models.SalesVisitReport.objects.all()

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'Sales_Visit_Report.html', context)


@permission_required('management.add_salesvisitreport', '/warning/')
def sales_visit_add(request):
    if request.method == 'GET':
        form = Sales_Visit_Form()
        return render(request, 'change.html', {'form': form, 'address': 'sales_visit'})

    form = Sales_Visit_Form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/sales_visit/')

    return render(request, 'change.html', {'form': form, 'address': 'sales_visit'})


@permission_required('management.change_salesvisitreport', '/warning/')
def sales_visit_edit(request, _id):
    row_object = models.SalesVisitReport.objects.filter(serial_number=_id).first()
    if request.method == 'GET':
        form = Sales_Visit_Form(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': 'sales_visit'})

    form = Sales_Visit_Form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/sales_visit/')

    return render(request, 'change.html', {'form': form, 'address': 'sales_visit'})


@permission_required('management.delete_salesvisitreport', '/warning/')
def sales_visit_delete(request, _id):
    models.SalesVisitReport.objects.filter(serial_number=_id).delete()
    return redirect('/sales_visit/')
