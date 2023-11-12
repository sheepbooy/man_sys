from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import NewProductDevelopment_form, ExistingFormulationProgressDescription_form
from management import models


def progress(request, _type):
    """新品，已有制剂进度描述表"""
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

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value,
        'type': _type,
    }
    return render(request, 'progress.html', context)


def progress_add(request, _type):
    """添加新品或已有制剂的进度描述"""
    form_cls = {
        'new': NewProductDevelopment_form,
        'preparation': ExistingFormulationProgressDescription_form,
    }.get(_type)
    template_cls = {
        'new': 'NewProductDevelopment',
        'preparation': 'ExistingFormulationProgressDescription',
    }.get(_type)

    if request.method == 'GET':
        form = form_cls()
        return render(request, f'{template_cls}_add.html', {'form': form})
    form = form_cls(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(f'/progress/{_type}/')
    return render(request, f'{template_cls}_add.html', {'form': form})


def progress_edit(request, _type, _id):
    """新品和已有制剂进度描述信息"""
    if _type == 'new':
        row_object = models.NewProductDevelopment.objects.filter(id=_id).first()
    elif _type == 'preparation':
        row_object = models.ExistingFormulationProgressDescription.objects.filter(id=_id).first()
    form_cls = {
        'new': NewProductDevelopment_form,
        'preparation': ExistingFormulationProgressDescription_form,
    }.get(_type)
    template_cls = {
        'new': 'NewProductDevelopment',
        'preparation': 'ExistingFormulationProgressDescription',
    }.get(_type)

    if request.method == 'GET':
        form = form_cls(instance=row_object)
        return render(request, f'{template_cls}_edit.html', {'form': form})
    form = form_cls(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect(f'/progress/{_type}/')
    return render(request, f'{template_cls}_edit.html', {'form': form})


def progress_delete(request, _type, _id):
    """编辑进度描述信息"""
    if _type == 'new':
        models.NewProductDevelopment.objects.filter(id=_id).delete()
    elif _type == 'preparation':
        models.ExistingFormulationProgressDescription.objects.filter(id=_id).delete()
    return redirect(f'/progress/{_type}/')
