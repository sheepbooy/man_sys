from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from management.utils.form import EmployeesRegisterForm, PasswordChangeForm
from management import models
from io import BytesIO
from management.utils.code import check_code
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.


def login_view(request):
    """登录页面"""
    display_error = False
    error_message = ""

    if request.method == 'POST':
        work_id = request.POST.get('id')
        password = request.POST.get('password')

        # 首先尝试使用 Django 的标准用户模型进行验证
        user = authenticate(request, username=work_id, password=password)
        if user is not None:
            # 检查是否是超级用户
            if user.is_superuser:
                login(request, user)
                return redirect('/admin/')

        try:
            employee = models.Employees.objects.get(work_id=work_id)
            if employee and employee.user:
                user = authenticate(request, username=employee.user.username, password=password)
            else:
                user = None
        except models.Employees.DoesNotExist:
            user = None

        user_entered_image_code = request.POST.get('image_code', '')
        stored_image_code = request.session.get('image_code', '')

        if user is not None and user_entered_image_code.upper() == stored_image_code.upper():
            login(request, user)
            # 从 Employees 对象获取姓名
            name = employee.name
            user_permissions = user.get_all_permissions()
            user_permissions = list(user_permissions)
            # print(user_permissions)
            request.session['info'] = {'work_id': work_id, 'name': name, 'user_permissions': user_permissions}

            request.session.set_expiry(60 * 60 * 24)
            return redirect('/customer/management/')
        else:
            display_error = True
            if user is None:
                error_message = "工号或密码错误，请重新输入。"
            elif user_entered_image_code.upper() != stored_image_code.upper():
                error_message = "验证码错误，请重新输入。"

    return render(request, 'login.html', {'display_error': display_error, 'error_message': error_message})


def register(request):
    """注册"""
    if request.method == 'GET':
        form = EmployeesRegisterForm()
        return render(request, 'register.html', {'form': form})

    form = EmployeesRegisterForm(data=request.POST)
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
        messages.success(request, '注册成功，请联系相关人员开放权限')
        return redirect('/register/')
    else:
        messages.error(request, '工号已存在或格式错误（两位大写字母加三位数字）')
        return render(request, 'register.html', {'form': form})


def customer_management_home(request):
    """登录后的客户管理页面"""
    return render(request, 'customer_management_home.html')


def project_management_home(request):
    """登录后的项目管理页面"""
    return render(request, 'project_management_home.html')


def ledger_management_home(request):
    """登录后的台账管理页面"""
    return render(request, 'ledger_management_home.html')


def user_management_home(request):
    """用户管理页面"""
    return render(request, 'user_management_home.html')


def report_show(request):
    """报表查看页面"""
    return render(request, 'report_show.html')


def logout(request):
    """注销登录"""
    request.session.clear()
    return redirect('/login/')


def user_detail(request, _id):
    """用户个人详情页面"""
    row_object = models.Employees.objects.filter(work_id=_id).first()

    if request.method == 'GET':
        form = PasswordChangeForm(instance=row_object)
        return render(request, 'change.html', {'form': form, 'back_url': '/customer/management/'})

    form = PasswordChangeForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/customer/management/')

    return render(request, 'change.html', {'form': form, 'back_url': '/customer/management/'})


def image_code(request):
    """生成图片验证码"""

    # 调用pillow函数进行生成验证码
    img, code_string = check_code()
    # 将验证码写入到session中，以便于后续校验
    request.session['image_code'] = code_string
    # 设置验证码的有效时间(60s)
    request.session.set_expiry(60)
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())


def warning(request):
    """显示错误信息"""
    return render(request, 'warning.html')


def test(request):
    """测试"""
    return render(request, 'test.html')
