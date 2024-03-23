from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from tablib import Dataset

from management.resources import customer_audit_resource
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


@permission_required('management.change_customeraudit', '/warning/')
def customer_audit_export(request):
    """导出"""
    selected_fields = request.GET.get('fields', None)
    _resource = customer_audit_resource()

    if selected_fields:
        fields = selected_fields.split(',')
        _resource.set_export_fields(fields)

    dataset = _resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    filename = "export.xls"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


@permission_required('management.change_customeraudit', '/warning/')
def customer_audit_import(request):
    """导入"""
    if request.method == 'POST' and request.FILES['myfile']:
        file_content = request.FILES['myfile']

        dataset = Dataset()
        imported_data = dataset.load(file_content.read(), format='xls')
        empty_rows = []

        # 检查空行
        for index, row in enumerate(imported_data, start=1):  # 从1开始计数以匹配Excel行号
            if not any(row):
                empty_rows.append(index)

        if empty_rows:
            # 如果存在空行，返回错误信息
            empty_rows_str = ", ".join(str(row_num) for row_num in empty_rows)
            return JsonResponse({
                'message': f'导入失败！文件中的以下行是空的，请去除这些空行后重试：{empty_rows_str}'
            }, status=400, safe=True)

        result = customer_audit_resource().import_data(imported_data, dry_run=True)  # 先试运行

        if not result.has_errors():
            # 实际导入数据
            customer_audit_resource().import_data(imported_data, dry_run=False)
            # 导入成功，构建JSON响应
            response_data = {
                'message': '数据成功导入！',
                'redirect': request.session.get('last_emp_page', '/customer_audit/')
            }
            return JsonResponse(response_data)
        else:
            # 如果导入过程中出现错误
            errors = []
            for error in result.row_errors():
                errors.append(f"行 {error[0]}: " + "; ".join([str(e.error) for e in error[1]]))
            error_msg = "导入过程中出现错误，请检查文件格式和内容。具体错误包括：" + "<br>".join(errors)

            # 注意这里我们使用safe=True，并且返回一个字典
            return JsonResponse({'message': error_msg}, status=400, safe=True)

    back_url = request.session.get('last_emp_page', '/customer_audit/')
    # 确保将back_url传递给模板
    return render(request, 'import.html', {'back_url': back_url, 'redirect_url': '/customer_audit/import/'})
