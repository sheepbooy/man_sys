from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import CustomerAudit_Form
from management import models
from management.utils.convert import convert_none_to_empty_string


@permission_required('management.view_customeraudit', '/warning/')
def customer_audit(request):
    """客户审计表"""
    # 获取搜索字段和值
    search_fields = request.GET.getlist('fields')  # 字段列表
    search_values = request.GET.getlist('values')  # 对应的值列表

    if search_fields and search_values:
        assert len(search_fields) == len(search_values), "字段和值列表长度不一致"
        query_set = models.CustomerAudit.objects.all()  # 确保是您的模型名
        for field, value in zip(search_fields, search_values):
            if field and value:
                query = Q(**{f"{field}__icontains": value})
                query_set = query_set.filter(query)
    else:
        query_set = models.CustomerAudit.objects.all()

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    # 保存当前页到会话，以便后续操作后可以返回到这一页
    request.session['last_emp_page'] = request.get_full_path()

    # 准备模型字段信息传递到模板
    field_info = [(field.name, field.verbose_name) for field in models.CustomerAudit._meta.fields if field.name != 'id']

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'search_fields': search_fields,
        'search_values': search_values,
        'field_info': field_info,
        'page_start_index': page_object.page_start_index,  # 添加这行
    }

    return render(request, 'customer_audit.html', context)


@permission_required('management.add_customeraudit', '/warning/')
def customer_audit_add(request):
    """问题反馈表添加"""
    if request.method == 'GET':
        form = CustomerAudit_Form()
        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/customer_audit/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = CustomerAudit_Form(data=request.POST)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/customer_audit/')
        return redirect(last_emp_page)

    # 如果表单验证不通过，也需要传递back_url到模板
    back_url = request.session.get('last_emp_page', '/customer_audit/')

    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.change_customeraudit', '/warning/')
def customer_audit_edit(request, _id):
    """编辑问题反馈表"""
    row_object = models.CustomerAudit.objects.filter(id=_id).first()
    if request.method == 'GET':
        form = CustomerAudit_Form(instance=row_object)
        back_url = request.session.get('last_emp_page', '/customer_audit/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = CustomerAudit_Form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/customer_audit/')
        return redirect(last_emp_page)
    # 如果表单验证不通过，也需要传递back_url到模板
    back_url = request.session.get('last_emp_page', '/customer_audit/')

    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.delete_customeraudit', '/warning/')
def customer_audit_delete(request, _id):
    """编辑问题反馈信息"""
    models.CustomerAudit.objects.filter(id=_id).delete()
    last_emp_page = request.session.get('last_emp_page', '/customer_audit/')
    return redirect(last_emp_page)
