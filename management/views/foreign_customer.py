from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.db.models import Q

from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import foreign_customer_form
from management import models


@permission_required('management.view_foreigncustomerprofile', '/warning/')
def foreign_customer(request):
    """外贸部客户档案"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.ForeignCustomerProfile._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.ForeignCustomerProfile.objects.filter(query)
    else:
        query_set = models.ForeignCustomerProfile.objects.all()

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    # 保存当前页到会话，以便后续操作后可以返回到这一页
    request.session['last_emp_page'] = request.get_full_path()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value,
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
    row_object = models.ForeignCustomerProfile.objects.filter(customer_profile_number=_id).first()
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
    models.ForeignCustomerProfile.objects.filter(customer_profile_number=_id).delete()
    # 从会话中获取上一页的URL，如果没有则重定向到员工列表的首页
    last_emp_page = request.session.get('last_emp_page', '/foreign/customer/')
    return redirect(last_emp_page)
