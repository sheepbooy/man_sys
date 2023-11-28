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
from management.views import login_register_home
from management.views import employee
from management.views import inner_trade_ledger
from management.views import foreign_trade_ledger
from management.views import foreign_customer
from management.views import preparation
from management.views import authorization
from management.views import new
from management.views import progress
from management.views import dev_customer
from management.views import butting
from management.views import turnover
from management.views import product
from management.views import question
from management.views import y_m_receivable_details
from management.views import reimbursement
from management.views import actual_sales
from management.views import customers_sales

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 登录，注册，主页等相关功能
    path('login/', login_register_home.login_view),
    path('register/', login_register_home.register),
    path('home/', login_register_home.home),
    path('logout/', login_register_home.logout),
    path('detail/<str:_id>/', login_register_home.user_detail),
    # 生成图片验证码
    path('image/code/', login_register_home.image_code),

    # 所有员工信息
    path('employees/', employee.employees_list),
    path('employees/add/', employee.employees_add),
    path('employees/edit/<str:_id>/', employee.employees_edit),
    path('employees/delete/<str:_id>/', employee.employees_delete),
    path('employees/reset/<str:_id>/', employee.employees_reset),

    # 内贸部台账表
    path('innertrade/ledger/', inner_trade_ledger.inner_trade_ledger),
    path('innertrade/ledger/add/', inner_trade_ledger.inner_trade_ledger_add),
    path('innertrade/ledger/edit/<int:_id>/', inner_trade_ledger.inner_trade_ledger_edit,
         name='edit_inner_trade_ledger'),
    path('innertrade/ledger/delete/<int:_id>/', inner_trade_ledger.inner_trade_ledger_delete,
         name='delete_inner_trade_ledger'),

    # 外贸部台账表
    path('foreign/ledger/', foreign_trade_ledger.foreign_trade_ledger),
    path('foreign/ledger/add/', foreign_trade_ledger.foreign_trade_ledger_add),
    path('foreign/ledger/edit/<int:_id>/', foreign_trade_ledger.foreign_trade_ledger_edit,
         name='edit_foreign_trade_ledger'),
    path('foreign/ledger/delete/<int:_id>/', foreign_trade_ledger.foreign_trade_ledger_delete,
         name='delete_foreign_trade_ledger'),

    # 外贸部客户档案表
    path('foreign/customer/', foreign_customer.foreign_customer),
    path('foreign/customer/add/', foreign_customer.foreign_customer_add),
    path('foreign/customer/edit/<int:_id>/', foreign_customer.foreign_customer_edit, name='edit_foreign_customer'),
    path('foreign/customer/delete/<int:_id>/', foreign_customer.foreign_customer_delete,
         name='delete_foreign_customer'),

    # 已有制剂已完成,开发中，待开发进度表
    path('preparation/<str:_type>/', preparation.preparation),
    path('preparation/<str:_type>/add/', preparation.preparation_add),
    path('preparation/<str:_type>/edit/<int:_id>/', preparation.preparation_edit, name='edit_preparation'),
    path('preparation/<str:_type>/delete/<int:_id>/', preparation.preparation_delete, name='delete_preparation'),

    # 授权书总表
    path('authorization/', authorization.authorization),
    path('authorization/add/', authorization.authorization_add),
    path('authorization/edit/<int:_id>/', authorization.authorization_edit, name='edit_authorization'),
    path('authorization/delete/<int:_id>/', authorization.authorization_delete, name='delete_authorization'),

    # 新品已完成，开发中进度表
    path('new/<str:_type>/', new.new),
    path('new/<str:_type>/add/', new.new_add),
    path('new/<str:_type>/edit/<int:_id>/', new.new_edit, name='edit_new'),
    path('new/<str:_type>/delete/<int:_id>/', new.new_delete, name='delete_new'),

    # 新品，已有制剂进度描述
    path('progress/<str:_type>/', progress.progress),
    path('progress/<str:_type>/add/', progress.progress_add),
    path('progress/<str:_type>/edit/<int:_id>/', progress.progress_edit, name='edit_progress'),
    path('progress/<str:_type>/delete/<int:_id>/', progress.progress_delete, name='delete_progress'),

    #  研发部客户档案
    path('develop/customer/', dev_customer.dev_custom),
    path('develop/customer/add/', dev_customer.dev_custom_add),
    path('develop/customer/edit/<int:_id>/', dev_customer.dev_custom_edit, name='edit_dev_custom'),
    path('develop/customer/delete/<int:_id>/', dev_customer.dev_custom_delete, name='delete_dev_custom'),

    # 研发部客户对接表
    path('develop/butting/', butting.butting),
    path('develop/butting/add/', butting.butting_add),
    path('develop/butting/edit/<int:_id>/', butting.butting_edit, name='edit_butting'),
    path('develop/butting/delete/<int:_id>/', butting.butting_delete, name='delete_butting'),

    # 研发部客户流水表
    path('develop/turnover/', turnover.turnover),
    path('develop/turnover/add/', turnover.turnover_add),
    path('develop/turnover/edit/<int:_id>/', turnover.turnover_edit, name='edit_turnover'),
    path('develop/turnover/delete/<int:_id>/', turnover.turnover_delete, name='delete_turnover'),

    # 辅料表
    path('product/', product.product),
    path('product/add/', product.product_add),
    path('product/edit/<str:_id>/', product.product_edit, name='edit_product'),
    path('product/delete/<str:_id>/', product.product_delete, name='delete_product'),

    # 问题反馈表
    path('question/', question.question),
    path('question/add/', question.question_add),
    path('question/edit/<int:_id>/', question.question_edit, name='edit_question'),
    path('question/delete/<int:_id>/', question.question_delete, name='delete_question'),

    # 报表管理
    path('report/', login_register_home.report_home),

    # 202X年X月台账基础表（原辅料、食品、研发、产品）
    path('report/inner/m_inner_trade_ledger/', inner_trade_ledger.x_month_inner_trade_ledger),

    # 202X年X月台账基础表（外贸部）
    path('report/foreign/m_foreign_trade_ledger/', foreign_trade_ledger.x_month_foreign_trade_ledger),

    # 202X年X月应收账款明细（原辅料、食品、研发、产品）：
    path('report/inner/m_receivable_detail/', y_m_receivable_details.receivable_detail),
    path('report/inner/m_receivable_detail/add/<int:_id>/', y_m_receivable_details.receivable_detail_add),

    # 截止202X年X月X日已逾期账款明细（原辅料、食品、研发、产品）
    path('report/inner/d_overdue_detail/', y_m_receivable_details.d_overdue_detali),
    path('report/inner/d_overdue_detail/add/<int:_id>/', y_m_receivable_details.d_overdue_detali_add),

    # 应收账款明细（外贸部）
    path('report/foreign/m_receivable_detail/', y_m_receivable_details.foreign_receivable),
    path('report/foreign/m_receivable_detail/add/<int:_id>/', y_m_receivable_details.foreign_receivable_add),

    # 销售各部门回款目标
    path('reimbursement/', reimbursement.reimbursement, name='reimbursement'),
    path('get-target-data/', reimbursement.get_target_data, name='get_target_data'),
    path('update-target-data/', reimbursement.update_target_data, name='update_target_data'),
    path('get-summary-data/', reimbursement.get_summary_data, name='get_summary_data'),
    path('get-current-targets/', reimbursement.get_current_targets, name='get-current-targets'),
    # 增加年份功能
    path('add_year_with_defaults_view/', reimbursement.add_year_with_defaults_view, name='add_year_with_defaults_view'),

    # 各部门回款目标与实际完成的结果
    path('targets-achievements/', actual_sales.targets_and_achievements_view, name='targets-achievements'),
    # 增加年份功能
    path('add_year_with_defaults/', actual_sales.add_year_with_defaults_view, name='add_year_with_defaults'),

    # 开发目标客户数和实现销售额
    path('customers_sales/', customers_sales.customers_sales, name='dashboard'),
    # 月实现订单数的统计
    path('order_summary/', customers_sales.order_summary, name='order-summary'),
    # 月度/季度销售额及其增量
    path('sales_increments/', customers_sales.sales_increments, name='sales_increments'),
    # 月度/季度回款金额及其增量
    path('sales_payback/', customers_sales.sales_payback, name='sales_payback'),
]
