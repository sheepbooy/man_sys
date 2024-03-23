from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.convert import convert_none_to_empty_string
from management.utils.pagination import Pagination
from management.utils.form import EmployeesForm, EmployeesAddForm
from management import models
from django.http import HttpResponse
from tablib import Dataset
# from management.resources import EmployeeResource
import chardet

# 职位与组名的映射关系
POSITION_TO_GROUP = {
    "数据库开发工程师": "Database Development Engineer",
    "营销中心总经理": "General Manager and Deputy General Manager of the Marketing Center",
    "营销中心副总经理": "General Manager and Deputy General Manager of the Marketing Center",
    "内务部主管": 'Head of the Ministry of Internal Affairs',
    "内务部助理": 'Assistant in the Ministry of Internal Affairs',
    "产品管理部主管": 'Head of Product Management',
    "产品管理部专员": 'Product Management Specialist',
    "研发服务部主管": 'Head of R&D Services',
    "研发服务部专员": "R&D Services Specialist",
    "外贸部主管": "Head of Foreign Trade Department",
    "外贸部业务员": "Salesman of Foreign Trade Department",
    "销售一部总经理": 'General Manager of Sales Department and Food Additives Department',
    "销售二部总经理": 'General Manager of Sales Department and Food Additives Department',
    "销售三部总经理": 'General Manager of Sales Department and Food Additives Department',
    "销售四部总经理": 'General Manager of Sales Department and Food Additives Department',
    "销售五部总经理": 'General Manager of Sales Department and Food Additives Department',
    "销售六部总经理": 'General Manager of Sales Department and Food Additives Department',
    "区域销售经理": "Regional Sales Manager of the Sales Department and the Food Additives Department",
    'GXD': "GXD",
    "DZR": "DZR",
    "ZMQ": 'Regional Sales Manager of the Sales Department and the Food Additives Department'
    # 添加更多职位和对应的组名
}


@permission_required('management.view_employees', login_url='/warning/')
def employees_list(request):
    # print(request.user)
    """所有员工信息表"""

    # 获取搜索字段和值
    search_fields = request.GET.getlist('fields')  # 字段列表
    search_values = request.GET.getlist('values')  # 对应的值列表

    if search_fields and search_values:
        assert len(search_fields) == len(search_values), "字段和值列表长度不一致"
        query_set = models.Employees.objects.all()  # 确保是您的模型名
        for field, value in zip(search_fields, search_values):
            if field and value:
                query = Q(**{f"{field}__icontains": value})
                query_set = query_set.filter(query)
    else:
        query_set = models.Employees.objects.all()

    # 在这里处理查询集，将所有None值转换为空字符串
    query_set = convert_none_to_empty_string(query_set)

    page_object = Pagination(request, query_set)
    page_object.html()

    # 保存当前页到会话，以便后续操作后可以返回到这一页
    request.session['last_emp_page'] = request.get_full_path()

    # 准备模型字段信息传递到模板
    field_info = [
        (field.name, field.verbose_name)
        for field in models.Employees._meta.fields
        if field.name not in ['id', 'user']
    ]

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'search_fields': search_fields,
        'search_values': search_values,
        'field_info': field_info,
        'page_start_index': page_object.page_start_index,  # 添加这行
    }

    return render(request, 'employees_list.html', context)


@permission_required('management.add_employees', login_url='/warning/')
def employees_add(request):
    """员工信息添加"""
    if request.method == 'GET':
        form = EmployeesAddForm()

        # 从会话中获取之前的页面路径，如果没有则默认回到第一页
        back_url = request.session.get('last_emp_page', '/employees/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = EmployeesAddForm(data=request.POST)
    if form.is_valid():
        # 在这里创建或更新User实例
        work_id = form.cleaned_data['work_id']
        password = form.cleaned_data['password']
        user, created = User.objects.get_or_create(username=work_id)
        if created or user.password != password:
            user.set_password(password)
            user.save()

        # 保存Employees实例
        employee = form.save(commit=False)
        employee.user = user
        employee.save()

        last_emp_page = request.session.get('last_emp_page', '/employees/')
        return redirect(last_emp_page)

    # 如果表单验证不通过，也需要传递back_url到模板
    back_url = request.session.get('last_emp_page', '/employees/')

    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.change_employees', login_url='/warning/')
def employees_edit(request, _id):
    """编辑员工信息"""
    row_object = models.Employees.objects.filter(work_id=_id).first()

    # 权限检查
    # if not request.user.has_perm('management.change_employees'):
    #     return render(request, 'warning.html', {"message": '您没有权限编辑此员工信息'})

    if request.method == 'GET':
        form = EmployeesForm(instance=row_object)  # 使用完整的 EmployeesForm
        back_url = request.session.get('last_emp_page', '/employees/')
        # 确保将back_url传递给模板
        return render(request, 'change.html', {'form': form, 'back_url': back_url})

    form = EmployeesForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 更新User实例
        work_id = form.cleaned_data['work_id']
        password = form.cleaned_data['password']
        user = row_object.user
        if user.username != work_id or user.password != password:
            user.username = work_id
            user.set_password(password)
            user.save()

        form.save()

        # 添加用户到相应的组
        position = form.cleaned_data['position']
        if position in POSITION_TO_GROUP:
            group_name = POSITION_TO_GROUP[position]
            try:
                group = Group.objects.get(name=group_name)
                group.user_set.add(user)
            except Group.DoesNotExist:
                pass  # 组不存在的处理方式，可以根据需要进行修改

        last_emp_page = request.session.get('last_emp_page', '/employees/')
        return redirect(last_emp_page)

    # 如果表单验证不通过，也需要传递back_url到模板
    back_url = request.session.get('last_emp_page', '/employees/')
    return render(request, 'change.html', {'form': form, 'back_url': back_url})


@permission_required('management.delete_employees', login_url='/warning/')
def employees_delete(request, _id):
    """用户删除"""
    # 删除指定工号的员工记录
    models.Employees.objects.filter(work_id=_id).delete()

    # 从会话中获取上一页的URL，如果没有则重定向到员工列表的首页
    last_emp_page = request.session.get('last_emp_page', '/employees/')
    return redirect(last_emp_page)


def get_positions(request):
    department = request.GET.get('department')
    positions = {
        '原辅料销售部': ['销售一部总经理', '销售二部总经理', '销售三部总经理', '销售四部总经理', '销售五部总经理',
                         '销售六部总经理', '区域销售经理', ],
        '食品添加剂部': [
            '食品添加剂部总经理', '食品添加剂部区域销售经理',
        ],
        '外贸部': [
            '外贸部主管', '外贸部业务员',
        ],
        '研发服务部': [
            '研发服务部主管', '研发服务部专员',
        ],
        '产品管理部': [
            '产品管理部主管', '产品管理部专员',
        ],
        '内务部': [
            '内务部主管', '内务部助理'
        ],
        '信管部': ['数据库开发工程师'],
    }
    response_data = positions.get(department, [])
    # print("Returning positions:", response_data)  # 打印返回的职位列表
    return JsonResponse(response_data, safe=False)


def employees_export(request):
    """员工导出功能"""
    employee_resource = EmployeeResource()
    dataset = employee_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="employees.xls"'
    return response


def employees_import(request):
    """员工导入功能"""
    if request.method == 'POST':
        dataset = Dataset()
        new_employees = request.FILES['myfile']
        imported_data = dataset.load(new_employees.read(), format='xls')
        for i in imported_data:
            print(i)
        result = EmployeeResource().import_data(dataset, dry_run=True)  # 测试数据导入

        if not result.has_errors():
            EmployeeResource().import_data(dataset, dry_run=False)  # 实际导入数据
            # 导入成功，构建JSON响应
            response_data = {
                'message': '数据成功导入！',
                'redirect': request.session.get('last_emp_page', '/employees/')
            }
            return JsonResponse(response_data)
        else:
            # 导入过程中发现错误，构建错误的JSON响应
            return JsonResponse({'message': '导入过程中出现错误，请检查文件格式及内容。'}, status=400)
    # 对于GET请求，仍然显示导入页面

    back_url = request.session.get('last_emp_page', '/employees/')
    return render(request, 'import.html', {'back_url': back_url, 'redirect_url': '/employees/import/'})
