from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import EmployeesForm, EmployeesAddForm
from management import models

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
    print(request.user)
    """所有员工信息表"""
    value = request.GET.get('q', '')
    if value:
        query = Q()
        fields = models.Employees._meta.fields
        for field in fields:
            # 排除 id 和 OneToOneField 字段
            if field.name != "id" and not isinstance(field, models.OneToOneField):
                q = Q(**{f"{field.name}__icontains": value})
                query |= q

        # 特别处理 user 字段
        # 假设您想根据 User 模型的 username 进行搜索
        user_query = Q(user__username__icontains=value)
        query_set = models.Employees.objects.filter(query | user_query)
    else:
        query_set = models.Employees.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }

    return render(request, 'employees_list.html', context)


@permission_required('management.add_employees', login_url='/warning/')
def employees_add(request):
    """员工信息添加"""
    if request.method == 'GET':
        form = EmployeesAddForm()
        return render(request, 'change.html', {'form': form, 'address': 'employees'})

    form = EmployeesForm(data=request.POST)
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

        return redirect('/employees/')

    return render(request, 'change.html', {'form': form, 'address': 'employees'})


@permission_required('management.change_employees', login_url='/warning/')
def employees_edit(request, _id):
    """编辑员工信息"""
    row_object = models.Employees.objects.filter(work_id=_id).first()

    # 权限检查
    # if not request.user.has_perm('management.change_employees'):
    #     return render(request, 'warning.html', {"message": '您没有权限编辑此员工信息'})

    if request.method == 'GET':
        form = EmployeesForm(instance=row_object)  # 使用完整的 EmployeesForm
        return render(request, 'change.html', {'form': form, 'address': 'employees'})

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

        return redirect('/employees/')

    return render(request, 'change.html', {'form': form, 'address': 'employees'})


@permission_required('management.delete_employees', login_url='/warning/')
def employees_delete(request, _id):
    """用户删除"""
    models.Employees.objects.filter(work_id=_id).delete()
    return redirect('/employees/')


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
