from django.shortcuts import render, redirect
from management import models
from django import forms


# Create your views here.
def login(request):
    """登录"""
    return render(request, 'login.html')


def register(request):
    """注册"""
    return render(request, 'register.html')

