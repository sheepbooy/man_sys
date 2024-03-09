from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.db.models import Q

from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import NewProductDevelopment_form, ExistingFormulationProgressDescription_form
from management import models


def progress(request, _type):
    """新品，已有制剂进度描述表"""
    # 权限映射
    permission_map = {
        'new': 'management.view_newproductdevelopment',
        'preparation': 'management.view_existingformulationprogressdescription',
    }

    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    model_map = {
        'new': models.NewProductDevelopment,
        'preparation': models.ExistingFormulationProgressDescription
    }

    value = request.GET.get('q', '')
    model = model_map.get(_type)  # 获取相应的模型

    if value is not None:
        query = Q(subordinate_id__icontains=value)
        query_set = model.objects.filter(query) if model else None
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
        'can_add_new': request.user.has_perm('management.add_newproductdevelopment'),
        'can_edit_new': request.user.has_perm('management.change_newproductdevelopment'),
        'can_delete_new': request.user.has_perm('management.delete_newproductdevelopment'),

        'can_add_preparation': request.user.has_perm('management.add_existingformulationprogressdescription'),
        'can_edit_preparation': request.user.has_perm('management.change_existingformulationprogressdescription'),
        'can_delete_preparation': request.user.has_perm('management.delete_existingformulationprogressdescription'),
    }
    return render(request, 'progress.html', context)


def progress_add(request, _type):
    """添加新品或已有制剂的进度描述"""
    # 权限映射
    permission_map = {
        'new': 'management.add_newproductdevelopment',
        'preparation': 'management.add_existingformulationprogressdescription',
    }
    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    form_cls = {
        'new': NewProductDevelopment_form,
        'preparation': ExistingFormulationProgressDescription_form,
    }.get(_type)

    if request.method == 'GET':
        form = form_cls()
        return render(request, 'change.html', {'form': form, 'address': f'progress/{_type}'})
    form = form_cls(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(f'/progress/{_type}/')
    return render(request, 'change.html', {'form': form, 'address': f'progress/{_type}'})


def progress_edit(request, _type, _id):
    """新品和已有制剂进度描述信息"""
    # 权限映射
    permission_map = {
        'new': 'management.change_newproductdevelopment',
        'preparation': 'management.change_existingformulationprogressdescription',
    }
    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    if _type == 'new':
        row_object = models.NewProductDevelopment.objects.filter(id=_id).first()
    elif _type == 'preparation':
        row_object = models.ExistingFormulationProgressDescription.objects.filter(id=_id).first()
    form_cls = {
        'new': NewProductDevelopment_form,
        'preparation': ExistingFormulationProgressDescription_form,
    }.get(_type)

    if request.method == 'GET':
        form = form_cls(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': f'progress/{_type}'})
    form = form_cls(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect(f'/progress/{_type}/')
    return render(request, 'change.html', {'form': form, 'address': f'progress/{_type}'})


def progress_delete(request, _type, _id):
    """编辑进度描述信息"""
    # 权限映射
    permission_map = {
        'new': 'management.delete_newproductdevelopment',
        'preparation': 'management.delete_existingformulationprogressdescription',
    }
    # 检查权限
    user_has_permission = request.user.has_perm(permission_map.get(_type, ''))
    if not user_has_permission:
        raise PermissionDenied

    if _type == 'new':
        models.NewProductDevelopment.objects.filter(id=_id).delete()
    elif _type == 'preparation':
        models.ExistingFormulationProgressDescription.objects.filter(id=_id).delete()
    return redirect(f'/progress/{_type}/')
