from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import Complaint_summary_form
from management import models


def complaint_summary(request):
    """全国客诉汇总"""
    departments_query = models.Complaint_summary.objects.values('department').distinct()
    departments = [item['department'] for item in departments_query]
    selected_department = request.GET.get('department')
    if selected_department:
        # 创建 Q 对象来过滤 sales_month
        # 查询条件：未收款不等于0且不为空白的记录
        query = Q(department__icontains=selected_department)
        query_set = models.Complaint_summary.objects.filter(query)
    else:
        query_set = models.Complaint_summary.objects.all()

        # 进行分页等后续处理，保持不变
    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'departments': departments,
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'selected_department': selected_department
    }
    return render(request, 'complaint_summary.html', context)


def complaint_summary_add(request):
    """全国客诉汇总添加"""
    if request.method == 'GET':
        form = Complaint_summary_form()
        return render(request, 'change.html', {'form': form, 'address': 'complaint_summary'})

    form = Complaint_summary_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/complaint_summary/')

    return render(request, 'change.html', {'form': form, 'address': 'complaint_summary'})


def complaint_summary_edit(request, _id):
    """全国客诉汇总编辑"""
    row_object = models.Complaint_summary.objects.filter(id=_id).first()
    if request.method == 'GET':
        form = Complaint_summary_form(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': 'complaint_summary'})

    form = Complaint_summary_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/complaint_summary/')

    return render(request, 'change.html', {'form': form, 'address': 'complaint_summary'})


def complaint_summary_delete(request, _id):
    """全国客诉汇总删除"""
    models.Complaint_summary.objects.filter(id=_id).delete()
    return redirect('/complaint_summary/')
