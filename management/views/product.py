from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import Products_form
from management import models


@permission_required('management.view_products', '/warning/')
def product(request):
    """辅料表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.Products._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.Products.objects.filter(query)
    else:
        query_set = models.Products.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }

    return render(request, 'product.html', context)


@permission_required('management.add_products', '/warning/')
def product_add(request):
    """辅料表添加"""
    if request.method == 'GET':
        form = Products_form()
        return render(request, 'change.html', {'form': form, 'address': 'product'})

    form = Products_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/product/')

    return render(request, 'change.html', {'form': form, 'address': 'product'})


@permission_required('management.change_products', '/warning/')
def product_edit(request, _id):
    """编辑药用辅料表"""
    row_object = models.Products.objects.filter(spec_code=_id).first()
    if request.method == 'GET':
        form = Products_form(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': 'product'})

    form = Products_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/product/')

    return render(request, 'change.html', {'form': form, 'address': 'product'})


@permission_required('management.delete_products', '/warning/')
def product_delete(request, _id):
    """删除辅料信息"""
    models.Products.objects.filter(spec_code=_id).delete()
    return redirect('/product/')
