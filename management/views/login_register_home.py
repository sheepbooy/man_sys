from django.http import HttpResponse
from django.shortcuts import render, redirect
from management.utils.form import EmployeesForm
from management import models
from io import BytesIO
from management.utils.code import check_code


# Create your views here.
def login_view(request):
    """登录页面"""
    display_error = False  # 默认情况下，不显示错误消息
    error_message = ""  # 默认错误消息为空字符串

    if request.method == 'POST':
        work_id = request.POST.get('id')  # 获取工号
        password = request.POST.get('password')  # 获取密码
        user = models.Employees.objects.filter(work_id=work_id).first()
        print(work_id, password)
        # 获取用户输入的验证码
        user_entered_image_code = request.POST.get('image_code', '')
        # 获取session中的验证码
        stored_image_code = request.session.get('image_code', '')
        print(user_entered_image_code, stored_image_code)
        # 验证成功，生成cookie并写入浏览器，再写入session
        if user is not None and user.password == password and user_entered_image_code.upper() == stored_image_code.upper():
            name = user.name
            request.session['info'] = {'work_id': work_id, 'name': name}
            # 重置cookie超时时间
            request.session.set_expiry(60 * 60 * 24)
            return redirect('/home/')
        else:
            display_error = True  # 登录失败时显示错误消息

            # 设置不同的错误信息
            if user is None:
                error_message = "工号不存在，请重新输入。"
            elif user.password != password:
                error_message = "密码错误，请重新输入。"
            elif user_entered_image_code != stored_image_code:
                error_message = "验证码错误，请重新输入。"

    return render(request, 'login.html', {'display_error': display_error, 'error_message': error_message})


def register(request):
    """注册"""
    if request.method == 'GET':
        form = EmployeesForm()
        return render(request, 'register.html', {'form': form})

    form = EmployeesForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/login/')
    else:
        return render(request, 'register.html', {'form': form})


def home(request):
    """登录后的主页面"""
    return render(request, 'home.html')

def report_home(request):
    """登录后的视图主页面"""
    return render(request, 'report_home.html')


def logout(request):
    """注销登录"""
    request.session.clear()
    return redirect('/login/')


def user_detail(request, _id):
    """用户个人详情页面"""
    row_object = models.Employees.objects.filter(work_id=_id).first()

    if request.method == 'GET':
        form = EmployeesForm(instance=row_object)
        return render(request, 'change.html', {'form': form, 'address': 'home'})

    form = EmployeesForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/home/')

    return render(request, 'change.html', {'form': form, 'address': 'home'})


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
