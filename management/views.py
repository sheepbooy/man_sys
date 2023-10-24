from django.shortcuts import render, redirect
from management import models
from django import forms
import django_tables2 as tables


class EmployeesForm(forms.ModelForm):
    """员工信息表类"""

    class Meta:
        model = models.Employees
        fields = ['name', 'password', 'department', 'gender', 'position', 'work_id', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


# Create your views here.
def login_view(request):
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


def employees_list(request):
    """所有员工信息表"""
    query_set = models.Employees.objects.all()
    return render(request, 'employees_list.html', {'query_set': query_set})


def inner_trade_ledger(request):
    """内贸部台账表"""
    query_set = models.InternalTradeLedger.objects.all()
    return render(request, 'inner_trade_ledger.html', {'query_set': query_set})


def foreign_trade_ledger(request):
    """外贸部台账表"""
    query_set = models.ForeignTradeLedger.objects.all()
    return render(request, 'foreign_trade_ledger.html', {'query_set': query_set})


def foreign_customer(request):
    """外贸部客户档案"""
    query_set = models.ForeignCustomerProfile.objects.all()
    return render(request, 'foreign_customer_list.html', {'query_set': query_set})


def preparation(request, _type):
    """已有制剂的已完成，待开发，开发中进度表"""
    if _type == 'completed':
        query_set = models.ExistingProductCompleted.objects.all()
        return render(request, 'preparation.html', {'query_set': query_set})

    elif _type == 'ing':
        query_set = models.ExistingFormulationDeveloping.objects.all()
        return render(request, 'preparation.html', {'query_set': query_set})

    elif _type == 'todev':
        query_set = models.ExistingFormulationToDevelop.objects.all()
        return render(request, 'preparation.html', {'query_set': query_set})


def authorization(request):
    """授权书总表"""
    query_set = models.Authorization.objects.all()
    return render(request, 'authorization.html', {'query_set': query_set})


def new(request, _type):
    """新品开发中，已完成进度表"""
    if _type == 'ing':
        query_set = models.NewProductDevelopingProgress.objects.all()
        return render(request, 'new_product.html', {'query_set': query_set})
    elif _type == 'completed':
        query_set = models.NewProductCompleted.objects.all()
        return render(request, 'new_product.html', {'query_set': query_set})


def progress(request, _type):
    """新品，已有制剂进度描述表"""
    if _type == 'new':
        query_set = models.NewProductDevelopment.objects.all()
        return render(request, 'progress.html', {'query_set': query_set})
    elif _type == 'preparation':
        query_set = models.ExistingFormulationProgressDescription.objects.all()
        return render(request, 'progress.html', {'query_set': query_set})


def dev_custom(request):
    """研发部客户档案表"""
    query_set = models.CustomerProfile.objects.all()
    return render(request, 'dev_custom.html', {'query_set': query_set})


def butting(request):
    """研发部客户对接表"""
    query_set = models.CustomerEngagement.objects.all()
    return render(request, 'butting.html', {'query_set': query_set})


def turnover(request):
    """研发部客户流水表"""
    query_set = models.CustomerFlow.objects.all()
    return render(request, 'turnover.html', {'query_set': query_set})


def product(request):
    """辅料表"""
    query_set = models.Products.objects.all()
    return render(request, 'product.html', {'query_set': query_set})


def question(request):
    """问题调查表"""
    query_set = models.Feedback.objects.all()
    return render(request, 'question.html', {'query_set': query_set})