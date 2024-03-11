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
    # 获取搜索字段和值
    search_fields = request.GET.getlist('fields')  # 字段列表
    search_values = request.GET.getlist('values')  # 对应的值列表

    if search_fields and search_values:
        assert len(search_fields) == len(search_values), "字段和值列表长度不一致"
        query_set = models.SalesVisitReport.objects.all()  # 确保是您的模型名
        for field, value in zip(search_fields, search_values):
            if field and value:
                query = Q(**{f"{field}__icontains": value})
                query_set = query_set.filter(query)
    else:
        query_set = models.SalesVisitReport.objects.all()

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    # 保存当前页到会话，以便后续操作后可以返回到这一页
    request.session['last_emp_page'] = request.get_full_path()

    # 准备模型字段信息传递到模板
    field_info = [(field.name, field.verbose_name) for field in models.SalesVisitReport._meta.fields if field.name != 'id']

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'search_fields': search_fields,
        'search_values': search_values,
        'field_info': field_info,
        'page_start_index': page_object.page_start_index,  # 添加这行
    }
    return render(request, 'Sales_Visit_Report.html', context)


@permission_required('management.add_salesvisitreport', '/warning/')
def sales_visit_add(request):
    if request.method == 'GET':
        form = Sales_Visit_Form()
        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/sales_visit/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = Sales_Visit_Form(data=request.POST)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/sales_visit/')
        return redirect(last_emp_page)
        # 如果表单验证不通过，也需要传递back_url到模板
    back_url = request.session.get('last_emp_page', '/sales_visit/')

    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.change_salesvisitreport', '/warning/')
def sales_visit_edit(request, _id):
    row_object = models.SalesVisitReport.objects.filter(serial_number=_id).first()
    if request.method == 'GET':
        form = Sales_Visit_Form(instance=row_object)
        back_url = request.session.get('last_emp_page', '/sales_visit/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = Sales_Visit_Form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/sales_visit/')
        return redirect(last_emp_page)

    # 如果表单验证不通过，也需要传递back_url到模板
    back_url = request.session.get('last_emp_page', '/sales_visit/')
    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.delete_salesvisitreport', '/warning/')
def sales_visit_delete(request, _id):
    models.SalesVisitReport.objects.filter(serial_number=_id).delete()
    # 从会话中获取上一页的URL，如果没有则重定向到员工列表的首页
    last_emp_page = request.session.get('last_emp_page', '/sales_visit/')
    return redirect(last_emp_page)
