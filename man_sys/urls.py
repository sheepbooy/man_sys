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
from django.urls import path
from management import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 登录，注册，主页等相关功能
    path('login/', views.login_view),
    path('register/', views.register),
    path('home/', views.home),


    # 所有的表全部信息
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
    path('new/<str:_type>/', views.new),
    # 新品，已有制剂进度描述
    path('progress/<str:_type>/', views.progress),
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

    # 添加功能
    # 员工
    path('employees/add/', views.employees_add),
    # 内贸部台账表
    path('innertrade/ledger/add/', views.inner_trade_ledger_add),
    # 外贸部台账表
    path('foreign/ledger/add/', views.foreign_trade_ledger_add),
    # 外贸部客户档案表
    path('foreign/customer/add/', views.foreign_customer_add),
    # 已有制剂已完成,开发中，待开发进度表
    path('preparation/<str:_type>/add/', views.preparation_add),
    # 授权书总表
    path('authorization/add/', views.authorization_add),
    # 新品已完成，开发中进度表
    path('new/<str:_type>/add/', views.new_add),
    # 新品，已有制剂进度描述
    path('progress/<str:_type>/add/', views.progress_add),
    #  研发部客户档案
    path('develop/customer/add/', views.dev_custom_add),
    # 研发部客户对接表
    path('develop/butting/add/', views.butting_add),
    # 研发部客户流水表
    path('develop/turnover/add/', views.turnover_add),
    # 辅料表
    path('product/add/', views.product_add),
    # 问题反馈表
    path('question/add/', views.question_add),

    # 编辑功能
    # 员工编辑功能
    path('employees/edit/<str:_id>/', views.employees_edit),
    # 编辑内贸部台账表
    path('innertrade/ledger/edit/<int:_id>/', views.inner_trade_ledger_edit, name='edit_inner_trade_ledger'),

    # 编辑外贸部台账表
    path('foreign/ledger/edit/<int:_id>/', views.foreign_trade_ledger_edit, name='edit_foreign_trade_ledger'),

    # 编辑外贸部客户档案表
    path('foreign/customer/edit/<int:_id>/', views.foreign_customer_edit, name='edit_foreign_customer'),

    # 编辑已有制剂已完成,开发中，待开发进度表
    path('preparation/<str:_type>/edit/<int:_id>/', views.preparation_edit, name='edit_preparation'),

    # 编辑授权书总表
    path('authorization/edit/<int:_id>/', views.authorization_edit, name='edit_authorization'),

    # 编辑新品已完成，开发中进度表
    path('new/<str:_type>/edit/<int:_id>/', views.new_edit, name='edit_new'),

    # 编辑新品，已有制剂进度描述
    path('progress/<str:_type>/edit/<int:_id>/', views.progress_edit, name='edit_progress'),

    # 编辑研发部客户档案
    path('develop/customer/edit/<int:_id>/', views.dev_custom_edit, name='edit_dev_custom'),

    # 编辑研发部客户对接表
    path('develop/butting/edit/<int:_id>/', views.butting_edit, name='edit_butting'),

    # 编辑研发部客户流水表
    path('develop/turnover/edit/<int:_id>/', views.turnover_edit, name='edit_turnover'),

    # 编辑辅料表
    path('product/edit/<str:_id>/', views.product_edit, name='edit_product'),

    # 编辑问题反馈表
    path('question/edit/<int:_id>/', views.question_edit, name='edit_question'),

    # 删除功能
    # 员工删除功能
    path('employees/delete/<str:_id>/', views.employees_delete),
    # 删除内贸部台账表
    path('innertrade/ledger/delete/<int:_id>/', views.inner_trade_ledger_delete, name='delete_inner_trade_ledger'),

    # 删除外贸部台账表
    path('foreign/ledger/delete/<int:_id>/', views.foreign_trade_ledger_delete, name='delete_foreign_trade_ledger'),

    # 删除外贸部客户档案表
    path('foreign/customer/delete/<int:_id>/', views.foreign_customer_delete, name='delete_foreign_customer'),

    # 删除已有制剂已完成,开发中，待开发进度表
    path('preparation/<str:_type>/delete/<int:_id>/', views.preparation_delete, name='delete_preparation'),

    # 删除授权书总表
    path('authorization/delete/<int:_id>/', views.authorization_delete, name='delete_authorization'),

    # 删除新品已完成，开发中进度表
    path('new/<str:_type>/delete/<int:_id>/', views.new_delete, name='delete_new'),

    # 删除新品，已有制剂进度描述
    path('progress/<str:_type>/delete/<int:_id>/', views.progress_delete, name='delete_progress'),

    # 删除研发部客户档案
    path('develop/customer/delete/<int:_id>/', views.dev_custom_delete, name='delete_dev_custom'),

    # 删除研发部客户对接表
    path('develop/butting/delete/<int:_id>/', views.butting_delete, name='delete_butting'),

    # 删除研发部客户流水表
    path('develop/turnover/delete/<int:_id>/', views.turnover_delete, name='delete_turnover'),

    # 删除辅料表
    path('product/delete/<str:_id>/', views.product_delete, name='delete_product'),

    # 删除问题反馈表
    path('question/delete/<int:_id>/', views.question_delete, name='delete_question'),

]
