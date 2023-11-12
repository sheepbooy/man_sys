from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import NewProductDeveloping_form, NewProductCompleted_form
from management import models


def new(request, _type):
    """新品开发中，已完成进度表"""
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

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value,
        'type': _type
    }
    return render(request, 'new_product.html', context)


def new_add(request, _type):
    """新品（已完成，开发中）添加"""
    form_cls = {
        'completed': NewProductCompleted_form,
        'ing': NewProductDeveloping_form,
    }.get(_type)
    template_cls = {
        'completed': 'NewProductCompleted',
        'ing': 'NewProductDeveloping',
    }.get(_type)
    if request.method == 'GET':
        form = form_cls()
        return render(request, f'{template_cls}_add.html', {'form': form})
    form = form_cls(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(f'/new/{_type}/')
    return render(request, f'{template_cls}_add.html', {'form': form})


def new_edit(request, _type, _id):
    """编辑新品开发表"""
    if _type == 'ing':
        row_object = models.NewProductDevelopingProgress.objects.filter(serial_number=_id).first()
    elif _type == 'completed':
        row_object = models.NewProductCompleted.objects.filter(serial_number=_id).first()
    form_cls = {
        'completed': NewProductCompleted_form,
        'ing': NewProductDeveloping_form,
    }.get(_type)
    template_cls = {
        'completed': 'NewProductCompleted',
        'ing': 'NewProductDeveloping',
    }.get(_type)
    if request.method == 'GET':
        form = form_cls(instance=row_object)
        return render(request, f'{template_cls}_edit.html', {'form': form})
    form = form_cls(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect(f'/new/{_type}/')
    return render(request, f'{template_cls}_edit.html', {'form': form})


def new_delete(request, _type, _id):
    """删除新品开发表"""
    if _type == 'ing':
        models.NewProductDevelopingProgress.objects.filter(serial_number=_id).delete()
    elif _type == 'completed':
        models.NewProductCompleted.objects.filter(serial_number=_id).delete()
    return redirect(f'/new/{_type}/')
