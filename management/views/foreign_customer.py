from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import foreign_customer_form
from management import models
from django.http import JsonResponse
from django.http import HttpResponse
from tablib import Dataset
# from management.resources import ForeignCustomerProfileResource


@permission_required('management.view_foreigncustomerprofile', '/warning/')
def foreign_customer(request):
    """外贸部客户档案"""
    # 获取搜索字段和值
    search_fields = request.GET.getlist('fields')  # 字段列表
    search_values = request.GET.getlist('values')  # 对应的值列表

    if search_fields and search_values:
        assert len(search_fields) == len(search_values), "字段和值列表长度不一致"
        query_set = models.ForeignCustomerProfile.objects.all()
        for field, value in zip(search_fields, search_values):
            if field and value:
                query = Q(**{f"{field}__icontains": value})
                query_set = query_set.filter(query)
    else:
        query_set = models.ForeignCustomerProfile.objects.all()

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    # 保存当前页到会话，以便后续操作后可以返回到这一页
    request.session['last_emp_page'] = request.get_full_path()

    # 准备模型字段信息传递到模板
    field_info = [(field.name, field.verbose_name) for field in models.ForeignCustomerProfile._meta.fields if
                  field.name != 'id']

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'search_fields': search_fields,
        'search_values': search_values,
        'field_info': field_info,
        'page_start_index': page_object.page_start_index,  # 添加这行
    }
    return render(request, 'foreign_customer_list.html', context)


@permission_required('management.add_foreigncustomerprofile', '/warning/')
def foreign_customer_add(request):
    """外贸部客户添加"""
    if request.method == 'GET':
        form = foreign_customer_form()

        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/foreign/customer/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = foreign_customer_form(data=request.POST)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/foreign/customer/')
        return redirect(last_emp_page)

    # 如果表单验证不通过，也需要传递back_url到模板
    back_url = request.session.get('last_emp_page', '/foreign/customer/')

    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.change_foreigncustomerprofile', '/warning/')
def foreign_customer_edit(request, _id):
    """编辑外贸部客户信息"""
    row_object = models.ForeignCustomerProfile.objects.filter(id=_id).first()
    if request.method == 'GET':
        form = foreign_customer_form(instance=row_object)
        back_url = request.session.get('last_emp_page', '/foreign/customer/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = foreign_customer_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/foreign/customer/')
        return redirect(last_emp_page)

    # 如果表单验证不通过，也需要传递back_url到模板
    back_url = request.session.get('last_emp_page', '/foreign/customer/')
    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.delete_foreigncustomerprofile', '/warning/')
def foreign_customer_delete(request, _id):
    """外贸部客户删除"""
    models.ForeignCustomerProfile.objects.filter(id=_id).delete()
    # 从会话中获取上一页的URL，如果没有则重定向到员工列表的首页
    last_emp_page = request.session.get('last_emp_page', '/foreign/customer/')
    return redirect(last_emp_page)


# def foreign_customer_export(request):
#     resource = ForeignCustomerProfileResource()
#     dataset = resource.export()
#     response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="foreign_customer_profiles.xls"'
#     return response
#
#
# def foreign_customer_import(request):
#     """外贸部客户档案导入"""
#     if request.method == 'POST':
#         dataset = Dataset()
#         new_data = request.FILES['myfile']
#         imported_data = dataset.load(new_data.read(), format='xls')
#         result = ForeignCustomerProfileResource().import_data(dataset, dry_run=True)  # 测试数据导入
#
#         if not result.has_errors():
#             ForeignCustomerProfileResource().import_data(dataset, dry_run=False)  # 实际导入数据
#             # 导入成功，构建JSON响应
#             response_data = {
#                 'message': '数据成功导入！',
#                 'redirect': request.session.get('last_emp_page', '/foreign/customer/')
#             }
#             return JsonResponse(response_data)
#         else:
#             # 导入过程中发现错误，构建错误的JSON响应
#             return JsonResponse({'message': '导入过程中出现错误，请检查文件格式及内容。'}, status=400)
#     # 对于GET请求，仍然显示导入页面
#
#     back_url = request.session.get('last_emp_page', '/foreign/customer/')
#     return render(request, 'import.html', {'back_url': back_url, 'redirect_url': '/foreign/customer/import/'})
