from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import ProductNew_Form
from management import models
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods, require_POST
import json


@permission_required('management.view_product_new', '/warning/')
def product_new(request):
    """已有制剂展示与搜索"""

    # 获取搜索字段和值
    search_fields = request.GET.getlist('fields')  # 字段列表
    search_values = request.GET.getlist('values')  # 对应的值列表

    if search_fields and search_values:
        assert len(search_fields) == len(search_values), "字段和值列表长度不一致"
        query_set = models.product_new.objects.all()  # 确保是您的模型名
        for field, value in zip(search_fields, search_values):
            if field and value:
                query = Q(**{f"{field}__icontains": value})
                query_set = query_set.filter(query)
    else:
        query_set = models.product_new.objects.all()

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    # 保存当前页到会话，以便后续操作后可以返回到这一页
    request.session['last_emp_page'] = request.get_full_path()

    # 准备模型字段信息传递到模板
    field_info = [(field.name, field.verbose_name) for field in models.product_new._meta.fields if field.name != 'id']

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'search_fields': search_fields,
        'search_values': search_values,
        'field_info': field_info,
        'page_start_index': page_object.page_start_index,
    }

    return render(request, 'product_new.html', context)


@permission_required('management.add_product_new', '/warning/')
def product_new_add(request):
    """已有制剂添加"""
    if request.method == 'GET':
        form = ProductNew_Form()
        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/product_new/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = ProductNew_Form(data=request.POST)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/product_new/')
        return redirect(last_emp_page)

    # 从会话中获取之前的页面路径，如果没有则默认回到第一页
    back_url = request.session.get('last_emp_page', '/product_new/')
    # 确保将back_url传递给模板
    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.change_product_new', '/warning/')
def product_new_edit(request, _id):
    """已有制剂编辑"""
    row_object = models.product_new.objects.filter(id=_id).first()
    if request.method == 'GET':
        form = ProductNew_Form(instance=row_object)
        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/product_new/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = ProductNew_Form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/product_new/')
        return redirect(last_emp_page)

    # 从会话中获取之前的页面路径，如果没有则默认回到第一页
    back_url = request.session.get('last_emp_page', '/product_new/')
    # 确保将back_url传递给模板
    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.delete_product_new', '/warning/')
def product_new_delete(request, _id):
    """已有制剂删除"""
    models.product_new.objects.filter(id=_id).delete()
    last_emp_page = request.session.get('last_emp_page', '/product_new/')
    return redirect(last_emp_page)


def get_product_descriptions(request, product_new_id):
    """获取新品进度描述"""
    descriptions = models.ProductDescription.objects.filter(product_new_id=product_new_id)
    data = [model_to_dict(description, fields=['id', 'date', 'description']) for description in descriptions]
    for item in data:
        item['date'] = item['date'].strftime('%Y-%m-%d')
    return JsonResponse({'descriptions': data})


@require_http_methods(["DELETE"])
def delete_description(request, description_id):
    """新品进度描述的删除"""
    try:
        description = models.ProductDescription.objects.get(id=description_id)
        description.delete()
        return JsonResponse({'status': 'success'})
    except models.ProductDescription.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Description not found'}, status=404)


# @csrf_exempt
@require_http_methods(["POST"])
def edit_description(request, description_id):
    """编辑新品进度描述"""
    try:
        # 解析请求体中的 JSON 数据
        data = json.loads(request.body)
        # 获取对应的描述实例
        description = models.ProductDescription.objects.get(id=description_id)

        # 更新实例字段
        description.date = data['date']
        description.description = data['description']
        description.save()  # 保存更改

        # 返回成功响应
        return JsonResponse({'status': 'success'})
    except models.ProductDescription.DoesNotExist:
        # 描述实例未找到的错误处理
        return JsonResponse({'status': 'error', 'message': 'Description not found'}, status=404)
    except KeyError:
        # 数据不完整的错误处理
        return JsonResponse({'status': 'error', 'message': 'Missing data in request'}, status=400)
    except Exception as e:
        # 其他错误的处理
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


@require_POST
def add_product_description(request, product_new_id):
    """增加新品进度描述"""
    # 解析请求体中的 JSON 数据
    data = json.loads(request.body)
    # 获取对应的 product_new 实例
    product = get_object_or_404(models.product_new, pk=product_new_id)

    # 创建新的 ProductDescription 实例
    description = models.ProductDescription.objects.create(
        product_new=product,
        date=data['date'],
        description=data['description']
    )

    # 返回一个 JSON 响应
    return JsonResponse({
        'id': description.id,
        'date': description.date,
        'description': description.description
    })
