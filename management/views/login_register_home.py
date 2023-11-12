from django.shortcuts import render, redirect
from django.db.models import Q
from management.utils.pagination import Pagination
from management.utils.form import *

# Create your views here.
def login_view(request):
    """登录页面"""
    display_error = False  # 默认情况下，不显示错误消息

    if request.method == 'POST':
        work_id = request.POST.get('id')  # 获取工号
        password = request.POST.get('password')  # 获取密码
        user = models.Employees.objects.filter(work_id=work_id).first()

        if user is not None and user.password == password:
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