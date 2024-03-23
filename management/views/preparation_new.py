from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from tablib import Dataset

from management.resources import preparation_new_resource
from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import PreparationNew_Form
from management import models
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods, require_POST
import json


@permission_required('management.view_preparation_new', '/warning/')
def preparation_new(request):
    """已有制剂展示与搜索"""

    # 获取搜索字段和值
    search_fields = request.GET.getlist('fields')  # 字段列表
    search_values = request.GET.getlist('values')  # 对应的值列表

    if search_fields and search_values:
        assert len(search_fields) == len(search_values), "字段和值列表长度不一致"
        query_set = models.preparation_new.objects.all()  # 确保是您的模型名
        for field, value in zip(search_fields, search_values):
            if field and value:
                query = Q(**{f"{field}__icontains": value})
                query_set = query_set.filter(query)
    else:
        query_set = models.preparation_new.objects.all()

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    # 保存当前页到会话，以便后续操作后可以返回到这一页
    request.session['last_emp_page'] = request.get_full_path()

    # 准备模型字段信息传递到模板
    field_info = [(field.name, field.verbose_name) for field in models.preparation_new._meta.fields if
                  field.name != 'id']

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'search_fields': search_fields,
        'search_values': search_values,
        'field_info': field_info,
        'page_start_index': page_object.page_start_index,
    }

    return render(request, 'preparation_new.html', context)


@permission_required('management.add_preparation_new', '/warning/')
def preparation_new_add(request):
    """已有制剂添加"""
    if request.method == 'GET':
        form = PreparationNew_Form()
        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/preparation_new/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = PreparationNew_Form(data=request.POST)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/preparation_new/')
        return redirect(last_emp_page)

    # 从会话中获取之前的页面路径，如果没有则默认回到第一页
    back_url = request.session.get('last_emp_page', '/preparation_new/')
    # 确保将back_url传递给模板
    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.change_preparation_new', '/warning/')
def preparation_new_edit(request, _id):
    """已有制剂编辑"""
    row_object = models.preparation_new.objects.filter(id=_id).first()
    if request.method == 'GET':
        form = PreparationNew_Form(instance=row_object)
        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/preparation_new/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = PreparationNew_Form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/preparation_new/')
        return redirect(last_emp_page)

    # 从会话中获取之前的页面路径，如果没有则默认回到第一页
    back_url = request.session.get('last_emp_page', '/preparation_new/')
    # 确保将back_url传递给模板
    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.delete_preparation_new', '/warning/')
def preparation_new_delete(request, _id):
    """已有制剂删除"""
    models.preparation_new.objects.filter(id=_id).delete()
    last_emp_page = request.session.get('last_emp_page', '/preparation_new/')
    return redirect(last_emp_page)


def get_preparation_descriptions(request, preparation_id):
    descriptions = models.PreparationDescription.objects.filter(preparation_new_id=preparation_id)
    data = [model_to_dict(description, fields=['id', 'date', 'description']) for description in descriptions]
    for item in data:
        item['date'] = item['date'].strftime('%Y-%m-%d')
    return JsonResponse({'descriptions': data})


@require_http_methods(["DELETE"])
def delete_description(request, description_id):
    try:
        description = models.PreparationDescription.objects.get(id=description_id)
        description.delete()
        return JsonResponse({'status': 'success'})
    except models.PreparationDescription.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Description not found'}, status=404)


# @csrf_exempt
@require_http_methods(["POST"])
def edit_description(request, description_id):
    try:
        # 解析请求体中的 JSON 数据
        data = json.loads(request.body)
        # 获取对应的描述实例
        description = models.PreparationDescription.objects.get(id=description_id)

        # 更新实例字段
        description.date = data['date']
        description.description = data['description']
        description.save()  # 保存更改

        # 返回成功响应
        return JsonResponse({'status': 'success'})
    except models.PreparationDescription.DoesNotExist:
        # 描述实例未找到的错误处理
        return JsonResponse({'status': 'error', 'message': 'Description not found'}, status=404)
    except KeyError:
        # 数据不完整的错误处理
        return JsonResponse({'status': 'error', 'message': 'Missing data in request'}, status=400)
    except Exception as e:
        # 其他错误的处理
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@require_POST
def add_preparation_description(request, preparation_id):
    # 解析请求体中的 JSON 数据
    data = json.loads(request.body)
    # 获取对应的 Preparation 实例
    preparation = get_object_or_404(models.preparation_new, pk=preparation_id)

    # 创建新的 PreparationDescription 实例
    description = models.PreparationDescription.objects.create(
        preparation_new=preparation,
        date=data['date'],
        description=data['description']
    )

    # 返回一个 JSON 响应
    return JsonResponse({
        'id': description.id,
        'date': description.date,
        'description': description.description
    })


@permission_required('management.change_preparation_new', '/warning/')
def preparation_new_export(request):
    """导出"""
    selected_fields = request.GET.get('fields', None)
    _resource = preparation_new_resource()

    if selected_fields:
        fields = selected_fields.split(',')
        _resource.set_export_fields(fields)

    dataset = _resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    filename = "export.xls"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    return response


@permission_required('management.change_preparation_new', '/warning/')
def preparation_new_import(request):
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

        result = preparation_new_resource().import_data(imported_data, dry_run=True)  # 先试运行

        if not result.has_errors():
            # 实际导入数据
            preparation_new_resource().import_data(imported_data, dry_run=False)
            # 导入成功，构建JSON响应
            response_data = {
                'message': '数据成功导入！',
                'redirect': request.session.get('last_emp_page', '/preparation_new/')
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

    back_url = request.session.get('last_emp_page', '/preparation_new/')
    # 确保将back_url传递给模板
    return render(request, 'import.html', {'back_url': back_url, 'redirect_url': '/preparation_new/import/'})
