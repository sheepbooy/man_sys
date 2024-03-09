from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.db.models import Q

from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import NewProductDeveloping_form, NewProductCompleted_form
from management import models


def new(request, _type):
    """新品开发中，已完成进度表"""

    # 权限映射
    permission_map = {
        'ing': 'management.view_newproductdevelopingprogress',
        'completed': 'management.view_newproductcompleted',
    }
    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    model_map = {
        'ing': models.NewProductDevelopingProgress,
        'completed': models.NewProductCompleted
    }

    value = request.GET.get('q', '')
    model = model_map.get(_type)  # 获取相应的模型

    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        if model:
            # 获取模型的字段列表
            fields = model._meta.fields
            for field in fields:
                if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                    # 创建Q对象，并将字段名和搜索值拼接成查询条件
                    q = Q(**{f"{field.name}__icontains": value})
                    # 使用|操作符将Q对象添加到主查询中
                    query |= q

            query_set = model.objects.filter(query)
        else:
            query_set = None
    else:
        query_set = model.objects.all() if model else None

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value,
        'type': _type,

        # 为每种类型和操作组合检查权限
        'can_add_completed': request.user.has_perm('management.add_newproductcompleted'),
        'can_edit_completed': request.user.has_perm('management.change_newproductcompleted'),
        'can_delete_completed': request.user.has_perm('management.delete_newproductcompleted'),

        'can_add_ing': request.user.has_perm('management.add_newproductdevelopingprogress'),
        'can_edit_ing': request.user.has_perm('management.change_newproductdevelopingprogress'),
        'can_delete_ing': request.user.has_perm('management.delete_newproductdevelopingprogress'),
    }
    return render(request, 'new_product.html', context)


def new_add(request, _type):
    """新品（已完成，开发中）添加"""
    # 权限映射
    permission_map = {
        'ing': 'management.add_newproductdevelopingprogress',
        'completed': 'management.add_newproductcompleted',
    }
    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    form_cls = {
        'completed': NewProductCompleted_form,
        'ing': NewProductDeveloping_form,
    }.get(_type)

    if request.method == 'GET':
        form = form_cls()
        return render(request, 'change.html', {'form': form, 'address': f'new/{_type}'})
    form = form_cls(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(f'/new/{_type}/')
    return render(request, 'change.html', {'form': form, 'address': f'new/{_type}'})


def new_edit(request, _type, _id):
    """编辑新品开发表"""
    # 权限映射
    permission_map = {
        'ing': 'management.change_newproductdevelopingprogress',
        'completed': 'management.change_newproductcompleted',
    }
    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    if _type == 'ing':
        row_object = models.NewProductDevelopingProgress.objects.filter(serial_number=_id).first()
    elif _type == 'completed':
        row_object = models.NewProductCompleted.objects.filter(serial_number=_id).first()
    form_cls = {
        'completed': NewProductCompleted_form,
        'ing': NewProductDeveloping_form,
    }.get(_type)

    if request.method == 'GET':
        form = form_cls(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': f'new/{_type}'})
    form = form_cls(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect(f'/new/{_type}/')
    return render(request, 'change.html', {'form': form, 'address': f'new/{_type}'})


def new_delete(request, _type, _id):
    # 权限映射
    permission_map = {
        'ing': 'management.delete_newproductdevelopingprogress',
        'completed': 'management.delete_newproductcompleted',
    }
    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    """删除新品开发表"""
    if _type == 'ing':
        models.NewProductDevelopingProgress.objects.filter(serial_number=_id).delete()
    elif _type == 'completed':
        models.NewProductCompleted.objects.filter(serial_number=_id).delete()
    return redirect(f'/new/{_type}/')
