"""
URL configuration for man_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 登录，注册，主页等相关功能
    path('login/', views.login_view),
    path('register/', views.register),
    path('home/', views.home),

    # 所有员工信息
    path('employees/', views.employees_list),
    # 内贸部台账表
    path('innertrade/ledger/', views.inner_trade_ledger),
    # 外贸部台账表
    path('foreign/ledger/', views.foreign_trade_ledger),
    # 外贸部客户档案表
    path('foreign/customer/', views.foreign_customer),
    # 已有制剂已完成,开发中，待开发进度表
    path('preparation/<str:_type>/', views.preparation),
    # 授权书总表
    path('authorization/', views.authorization),
    # 新品已完成，开发中进度表
    path('new/<str:_type>', views.new),
    # 新品，已有制剂进度描述
    path('progress/<str:_type>', views.progress),
    #  研发部客户档案
    path('develop/customer/', views.dev_custom),
    # 研发部客户对接表
    path('develop/butting/', views.butting),
    # 研发部客户流水表
    path('develop/turnover/', views.turnover),
    # 辅料表
    path('product/', views.product),
    # 问题反馈表
    path('question/', views.question),

]
