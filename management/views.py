from django.shortcuts import render, redirect
from management import models
from django import forms


# Create your views here.
def login(request):
    """登录"""
    return render(request, 'login.html')


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = models.Employees
        fields = ['name', 'password', 'department', 'gender', 'position', 'work_id', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


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
