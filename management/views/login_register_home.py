from django.shortcuts import render, redirect
from management.utils.form import EmployeesForm
from management import models


# Create your views here.
def login_view(request):
    """登录页面"""
    display_error = False  # 默认情况下，不显示错误消息

    if request.method == 'POST':
        work_id = request.POST.get('id')  # 获取工号
        password = request.POST.get('password')  # 获取密码
        user = models.Employees.objects.filter(work_id=work_id).first()

        # 验证成功，生成cookie并写入浏览器，再写入session
        if user is not None and user.password == password:
            name = user.name
            request.session['info'] = {'work_id': work_id, 'name': name}
            print(work_id, name)
            return redirect('/home/')
        else:
            display_error = True  # 登录失败时显示错误消息

    return render(request, 'login.html', {'display_error': display_error})


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
