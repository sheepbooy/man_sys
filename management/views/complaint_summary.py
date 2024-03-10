from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.db.models import Q, Count

from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import Complaint_summary_form
from management import models


@permission_required('management.view_complaintsummary', '/warning/')
def complaint_summary(request):
    """结合部门和产品分类的客诉汇总"""
    departments_query = models.ComplaintSummary.objects.values('department').distinct()
    departments = [item['department'] for item in departments_query]
    category_choices = dict(models.ComplaintSummary.CATEGORY_CHOICES)

    # 获取选择的部门和类别
    selected_department = request.GET.get('department')
    selected_category = request.GET.get('category', '')
    category_counts = {}

    if selected_category:
        # 如果有选定的类别，计算该类别的数量
        category_counts[selected_category] = models.ComplaintSummary.objects.filter(category=selected_category).count()
        # 如果选定了“所有分类”，则计算每个类别的数量
    else:
        for category_key, _ in models.ComplaintSummary.CATEGORY_CHOICES:
            category_counts[category_key] = models.ComplaintSummary.objects.filter(category=category_key).count()

    if selected_department:
        query = Q(department__icontains=selected_department)
        complaints = models.ComplaintSummary.objects.filter(query)
    elif selected_category in category_choices:
        complaints = models.ComplaintSummary.objects.filter(category=selected_category)
    else:
        complaints = models.ComplaintSummary.objects.all()

    # 在这里处理查询集，将所有None值转换为空字符串
    complaints = convert_none_to_empty_string(complaints)

    summary_data = complaints.values('product_name', 'category').annotate(count=Count('id'))
    page_object = Pagination(request, complaints)
    page_object.html()

    # 保存当前页到会话，以便后续操作后可以返回到这一页
    request.session['last_emp_page'] = request.get_full_path()

    context = {
        'category_counts': category_counts,
        'category_choices': category_choices,
        'departments': departments,
        'summary_data': summary_data,
        'selected_department': selected_department,
        'selected_category': selected_category,
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
    }
    return render(request, 'complaint_summary.html', context)


@permission_required('management.add_complaintsummary', '/warning/')
def complaint_summary_add(request):
    """全国客诉汇总添加"""
    if request.method == 'GET':
        form = Complaint_summary_form()
        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/complaint_summary/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = Complaint_summary_form(data=request.POST)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/complaint_summary/')
        return redirect(last_emp_page)

    # 从会话中获取之前的页面路径，如果没有则默认回到第一页
    back_url = request.session.get('last_emp_page', '/complaint_summary/')
    # 确保将back_url传递给模板
    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.change_complaintsummary', '/warning/')
def complaint_summary_edit(request, _id):
    """全国客诉汇总编辑"""
    row_object = models.ComplaintSummary.objects.filter(id=_id).first()
    if request.method == 'GET':
        form = Complaint_summary_form(instance=row_object)
        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/complaint_summary/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = Complaint_summary_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        last_emp_page = request.session.get('last_emp_page', '/develop/butting/')
        return redirect(last_emp_page)

    # 从会话中获取之前的页面路径，如果没有则默认回到第一页
    back_url = request.session.get('last_emp_page', '/complaint_summary/')
    # 确保将back_url传递给模板
    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.delete_complaintsummary', '/warning/')
def complaint_summary_delete(request, _id):
    """全国客诉汇总删除"""
    models.ComplaintSummary.objects.filter(id=_id).delete()
    last_emp_page = request.session.get('last_emp_page', '/complaint_summary/')
    return redirect(last_emp_page)
