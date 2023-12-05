from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import ExistingProductCompleted_form, ExistingFormulationDeveloping_form, \
    ExistingFormulationToDevelop_form
from management import models


def preparation(request, _type):
    """已有制剂的已完成，待开发，开发中进度表"""

    # 权限映射
    permission_map = {
        'completed': 'management.view_existingproductcompleted',
        'ing': 'management.view_existingformulationdeveloping',
        'todev': 'management.view_existingformulationtodevelop',
    }

    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    # 模型映射
    model_map = {
        'completed': models.ExistingProductCompleted,
        'ing': models.ExistingFormulationDeveloping,
        'todev': models.ExistingFormulationToDevelop
    }

    value = request.GET.get('q', '')
    model = model_map.get(_type)  # 定义一个默认的model

    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        if model:
            # 获取模型的字段列表
            fields = model._meta.fields
            for field in fields:
                if field.name != "serial_number":  # 排除默认的AutoField "id"字段
                    # 创建Q对象，并将字段名和搜索值拼接成查询条件
                    q = Q(**{f"{field.name}__icontains": value})
                    # 使用|操作符将Q对象添加到主查询中
                    query |= q

            query_set = model.objects.filter(query)
        else:
            query_set = None
    else:
        query_set = model.objects.all() if model else None

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value,
        'type': _type,
        # 为每种类型和操作组合检查权限
        'can_add_completed': request.user.has_perm('management.add_existingproductcompleted'),
        'can_edit_completed': request.user.has_perm('management.change_existingproductcompleted'),
        'can_delete_completed': request.user.has_perm('management.delete_existingproductcompleted'),

        'can_add_ing': request.user.has_perm('management.add_existingformulationdeveloping'),
        'can_edit_ing': request.user.has_perm('management.change_existingformulationdeveloping'),
        'can_delete_ing': request.user.has_perm('management.delete_existingformulationdeveloping'),

        'can_add_todev': request.user.has_perm('management.add_existingformulationtodevelop'),
        'can_edit_todev': request.user.has_perm('management.change_existingformulationtodevelop'),
        'can_delete_todev': request.user.has_perm('management.delete_existingformulationtodevelop'),
    }
    return render(request, 'preparation.html', context)


def preparation_add(request, _type):
    """已有制剂（待开发，开发中，已完成）添加"""
    # 权限映射
    permission_map = {
        'completed': 'management.add_existingproductcompleted',
        'ing': 'management.add_existingformulationdeveloping',
        'todev': 'management.add_existingformulationtodevelop',
    }
    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    form_cls = {
        'completed': ExistingProductCompleted_form,
        'ing': ExistingFormulationDeveloping_form,
        'todev': ExistingFormulationToDevelop_form,
    }.get(_type)

    if request.method == 'GET':
        form = form_cls()
        return render(request, 'change.html', {'form': form, 'address': f'preparation/{_type}'})
    form = form_cls(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(f'/preparation/{_type}/')
    return render(request, 'change.html', {'form': form, 'address': f'preparation/{_type}'})


def preparation_edit(request, _type, _id):
    """已有制剂开发表"""
    # 权限映射
    permission_map = {
        'completed': 'management.change_existingproductcompleted',
        'ing': 'management.change_existingformulationdeveloping',
        'todev': 'management.change_existingformulationtodevelop',
    }
    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    form_cls = {
        'completed': ExistingProductCompleted_form,
        'ing': ExistingFormulationDeveloping_form,
        'todev': ExistingFormulationToDevelop_form,
    }.get(_type)

    if _type == 'completed':
        row_object = models.ExistingProductCompleted.objects.filter(serial_number=_id).first()
    elif _type == 'todev':
        row_object = models.ExistingFormulationToDevelop.objects.filter(serial_number=_id).first()
    elif _type == 'ing':
        row_object = models.ExistingFormulationDeveloping.objects.filter(serial_number=_id).first()
    if request.method == 'GET':
        form = form_cls(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': f'preparation/{_type}'})
    form = form_cls(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect(f'/preparation/{_type}/')
    return render(request, 'change.html', {'form': form, 'address': f'preparation/{_type}'})


def preparation_delete(request, _type, _id):
    # 权限映射
    permission_map = {
        'completed': 'management.delete_existingproductcompleted',
        'ing': 'management.delete_existingformulationdeveloping',
        'todev': 'management.delete_existingformulationtodevelop',
    }
    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    """删除已有制剂开发表"""
    if _type == 'completed':
        models.ExistingProductCompleted.objects.filter(serial_number=_id).delete()
    elif _type == 'ing':
        models.ExistingFormulationDeveloping.objects.filter(serial_number=_id).delete()
    elif _type == 'todev':
        models.ExistingFormulationToDevelop.objects.filter(serial_number=_id).delete()
    return redirect(f'/preparation/{_type}/')
