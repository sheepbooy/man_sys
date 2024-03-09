from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.db.models import Q

from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import Sales_Forecast_Form
from management import models


@permission_required('management.view_salesforecast', '/warning/')
def sales_forecast(request):
    """预算详情表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.SalesForecast._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "id":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.SalesForecast.objects.filter(query)
    else:
        query_set = models.SalesForecast.objects.all()
    # print(query_set)

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    # print(page_object)
    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }

    return render(request, 'sales_forecast.html', context)


@permission_required('management.add_salesforecast', '/warning/')
def sales_forecast_add(request):
    """问题反馈表添加"""
    if request.method == 'GET':
        form = Sales_Forecast_Form()
        return render(request, 'change.html', {'form': form, 'address': 'sales_forecast'})

    form = Sales_Forecast_Form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/sales_forecast/')

    return render(request, 'change.html', {'form': form, 'address': 'sales_forecast'})


@permission_required('management.change_salesforecast', '/warning/')
def sales_forecast_edit(request, _id):
    """编辑问题反馈表"""
    row_object = models.SalesForecast.objects.filter(id=_id).first()
    if request.method == 'GET':
        form = Sales_Forecast_Form(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': 'sales_forecast'})

    form = Sales_Forecast_Form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/sales_forecast/')

    return render(request, 'change.html', {'form': form, 'address': 'sales_forecast'})


@permission_required('management.delete_salesforecast', '/warning/')
def sales_forecast_delete(request, _id):
    """编辑问题反馈信息"""
    models.SalesForecast.objects.filter(id=_id).delete()
    return redirect('/sales_forecast/')
