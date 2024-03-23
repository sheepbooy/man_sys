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
from django.contrib import admin
from management.views import login_register_home
from management.views import employee
from management.views import inner_trade_ledger
from management.views import foreign_trade_ledger
from management.views import foreign_customer
from management.views import authorization
from management.views import dev_customer
from management.views import butting
from management.views import turnover
from management.views import product
from management.views import question
from management.views import y_m_receivable_details
from management.views import reimbursement
from management.views import actual_sales
from management.views import customers_sales
from management.views import complaint_summary
from management.views import Salesperson_Sales_Category
from management.views import sales_visit_report
from management.views import sales_forecast
from management.views import medicine
from management.views import customer_audit
from management.views import preparation_new
from management.views import product_new

urlpatterns = [
    path('admin/', admin.site.urls),

    # 测试
    path('test/', login_register_home.test),  # 登录，注册，主页等相关功能
    path('', login_register_home.login_view),
    path('login/', login_register_home.login_view),
    path('register/', login_register_home.register),
    # path('home/', login_register_home.home),
    path('logout/', login_register_home.logout),
    path('detail/<str:_id>/', login_register_home.user_detail),

    # 警告页面
    path('warning/', login_register_home.warning),
    # 生成图片验证码
    path('image/code/', login_register_home.image_code),

    # 客户管理
    path('customer/management/', login_register_home.customer_management_home),

    # 项目管理
    path('project/management/', login_register_home.project_management_home),

    # 台账管理
    path('ledger/management/', login_register_home.ledger_management_home),

    # 用户管理
    path('user/management/', login_register_home.user_management_home),

    # 报表查看
    path('report/management/', login_register_home.report_show),

    # 所有员工信息
    path('employees/', employee.employees_list),
    path('employees/add/', employee.employees_add),
    path('employees/edit/<str:_id>/', employee.employees_edit),
    path('employees/delete/<str:_id>/', employee.employees_delete),
    path('get-positions/', employee.get_positions, name='get-positions'),
    # 导入导出功能
    path('employees/export/', employee.employees_export, name='employees_export'),
    path('employees/import/', employee.employees_import, name='employees_import'),

    # 内贸部台账表
    path('innertrade/ledger/', inner_trade_ledger.inner_trade_ledger),
    path('innertrade/ledger/add/', inner_trade_ledger.inner_trade_ledger_add),
    path('innertrade/ledger/edit/<int:_id>/', inner_trade_ledger.inner_trade_ledger_edit,
         name='edit_inner_trade_ledger'),
    path('innertrade/ledger/delete/<int:_id>/', inner_trade_ledger.inner_trade_ledger_delete,
         name='delete_inner_trade_ledger'),
    path('innertrade/ledger/import/', inner_trade_ledger.inner_trade_ledger_import, name='inner_trade_ledger_import'),
    path('innertrade/ledger/export/', inner_trade_ledger.inner_trade_ledger_export, name='inner_trade_ledger_export'),

    # 外贸部台账表
    path('foreign/ledger/', foreign_trade_ledger.foreign_trade_ledger),
    path('foreign/ledger/add/', foreign_trade_ledger.foreign_trade_ledger_add),
    path('foreign/ledger/edit/<int:_id>/', foreign_trade_ledger.foreign_trade_ledger_edit,
         name='edit_foreign_trade_ledger'),
    path('foreign/ledger/delete/<int:_id>/', foreign_trade_ledger.foreign_trade_ledger_delete,
         name='delete_foreign_trade_ledger'),
    path('foreign/ledger/import/', foreign_trade_ledger.foreign_trade_ledger_import, name='foreign_trade_ledger_import'),
    path('foreign/ledger/export/', foreign_trade_ledger.foreign_trade_ledger_export, name='foreign_trade_ledger_export'),

    # 外贸部客户档案表
    path('foreign/customer/', foreign_customer.foreign_customer),
    path('foreign/customer/add/', foreign_customer.foreign_customer_add),
    path('foreign/customer/edit/<int:_id>/', foreign_customer.foreign_customer_edit, name='edit_foreign_customer'),
    path('foreign/customer/delete/<int:_id>/', foreign_customer.foreign_customer_delete,
         name='delete_foreign_customer'),
    path('foreign/customer/export/', foreign_customer.foreign_customer_export, name='foreign_customer_export'),
    path('foreign/customer/import/', foreign_customer.foreign_customer_import, name='foreign_customer_import'),

    # 授权书总表
    path('authorization/', authorization.authorization),
    path('authorization/add/', authorization.authorization_add),
    path('authorization/edit/<int:_id>/', authorization.authorization_edit, name='edit_authorization'),
    path('authorization/delete/<int:_id>/', authorization.authorization_delete, name='delete_authorization'),
    path('authorization/import/', authorization.authorization_import, name='authorization_import'),
    path('authorization/export/', authorization.authorization_export, name='authorization_export'),

    #  研发部客户档案
    path('develop/customer/', dev_customer.dev_custom),
    path('develop/customer/add/', dev_customer.dev_custom_add),
    path('develop/customer/edit/<int:_id>/', dev_customer.dev_custom_edit, name='edit_dev_custom'),
    path('develop/customer/delete/<int:_id>/', dev_customer.dev_custom_delete, name='delete_dev_custom'),
    path('develop/customer/import/', dev_customer.dev_custom_import, name='import_dev_custom'),
    path('develop/customer/export/', dev_customer.dev_custom_export, name='export_dev_custom'),

    # 研发部客户对接表
    path('develop/butting/', butting.butting),
    path('develop/butting/add/', butting.butting_add),
    path('develop/butting/edit/<int:_id>/', butting.butting_edit, name='edit_butting'),
    path('develop/butting/delete/<int:_id>/', butting.butting_delete, name='delete_butting'),
    path('develop/butting/import/', butting.butting_import, name='butting_import'),
    path('develop/butting/export/', butting.butting_export, name='butting_export'),

    # 研发部客户流水表
    path('develop/turnover/', turnover.turnover),
    path('develop/turnover/add/', turnover.turnover_add),
    path('develop/turnover/edit/<int:_id>/', turnover.turnover_edit, name='edit_turnover'),
    path('develop/turnover/delete/<int:_id>/', turnover.turnover_delete, name='delete_turnover'),
    path('develop/turnover/import/', turnover.turnover_import, name='turnover_import'),
    path('develop/turnover/export/', turnover.turnover_export, name='turnover_export'),

    # 辅料表
    path('product/', product.product),
    path('product/add/', product.product_add),
    path('product/edit/<str:_id>/', product.product_edit, name='edit_product'),
    path('product/delete/<str:_id>/', product.product_delete, name='delete_product'),
    path('product/export/', product.product_export, name='export_product'),
    path('product/import/', product.product_import, name='product_import'),

    # 问题反馈表
    path('question/', question.question),
    path('question/add/', question.question_add),
    path('question/edit/<int:_id>/', question.question_edit, name='edit_question'),
    path('question/delete/<int:_id>/', question.question_delete, name='delete_question'),
    path('question/import/', question.question_import, name='question_import'),
    path('question/export/', question.question_export, name='question_export'),

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

    # 退换货台账表-全国客诉汇总
    path('complaint_summary/', complaint_summary.complaint_summary, name='complaint_summary'),
    path('complaint_summary/add/', complaint_summary.complaint_summary_add, name='complaint_summary_add'),
    path('complaint_summary/edit/<int:_id>/', complaint_summary.complaint_summary_edit, name='complaint_summary_edit'),
    path('complaint_summary/delete/<int:_id>/', complaint_summary.complaint_summary_delete,
         name='complaint_summary_delete'),
    path('complaint_summary/import/', complaint_summary.complaint_summary_import, name='complaint_summary'),
    path('complaint_summary/export/', complaint_summary.complaint_summary_export, name='complaint_summary'),

    # 202X年-销售部-业务员-月度各品类销售金额
    path('customer_sales/salesperson/category/', Salesperson_Sales_Category.monthly_sales_report,
         name='monthly_sales_report'),

    # 202X年-销售部-业务员-月度各品类销售数量
    path('sales_amount/salesperson/category/', Salesperson_Sales_Category.sales_amount_report,
         name='sales_amount_report'),

    # 销售客户拜访报告
    path('sales_visit/', sales_visit_report.sales_visit_report, name='sales_visit_report'),
    path('sales_visit/add/', sales_visit_report.sales_visit_add, name='sales_visit_add'),
    path('sales_visit/edit/<int:_id>/', sales_visit_report.sales_visit_edit, name='sales_visit_edit'),
    path('sales_visit/delete/<int:_id>/', sales_visit_report.sales_visit_delete, name='sales_visit_delete'),
    path('sales_visit/import/', sales_visit_report.sales_visit_report_import, name='sales_visit_report_import'),
    path('sales_visit/export/', sales_visit_report.sales_visit_report_export, name='sales_visit_report_export'),

    # 预算详情表
    path('sales_forecast/', sales_forecast.sales_forecast, name='sales_forecast'),
    path('sales_forecast/add/', sales_forecast.sales_forecast_add, name='sales_forecast_add'),
    path('sales_forecast/edit/<int:_id>/', sales_forecast.sales_forecast_edit, name='sales_forecast_edit'),
    path('sales_forecast/delete/<int:_id>/', sales_forecast.sales_forecast_delete, name='sales_forecast_delete'),
    path('sales_forecast/import/', sales_forecast.sales_forecast_import, name='sales_forecast_import'),
    path('sales_forecast/export/', sales_forecast.sales_forecast_export, name='sales_forecast_export'),

    # 仿制药参比制剂目录
    path('medicine/', medicine.medicine, name='medicine'),
    path('medicine/add/', medicine.medicine_add, name='medicine_add'),
    path('medicine/edit/<int:_id>/', medicine.medicine_edit, name='medicine_edit'),
    path('medicine/delete/<int:_id>/', medicine.medicine_delete, name='medicine_delete'),
    path('medicine/import/', medicine.medicine_import, name='medicine_import'),
    path('medicine/export/', medicine.medicine_export, name='medicine_export'),

    # 客户审计表
    path('customer_audit/', customer_audit.customer_audit, name='customer_audit'),
    path('customer_audit/add/', customer_audit.customer_audit_add, name='customer_audit_add'),
    path('customer_audit/edit/<int:_id>/', customer_audit.customer_audit_edit, name='customer_audit_edit'),
    path('customer_audit/delete/<int:_id>/', customer_audit.customer_audit_delete, name='customer_audit_delete'),
    path('customer_audit/import/', customer_audit.customer_audit_import, name='customer_audit'),
    path('customer_audit/export/', customer_audit.customer_audit_export, name='customer_audit'),

    # 已有制剂表
    path('preparation_new/', preparation_new.preparation_new, name='preparation_new'),
    path('preparation_new/add/', preparation_new.preparation_new_add, name='preparation_new_add'),
    path('preparation_new/edit/<int:_id>/', preparation_new.preparation_new_edit, name='preparation_new_edit'),
    path('preparation_new/delete/<int:_id>/', preparation_new.preparation_new_delete, name='preparation_new_delete'),
    path('preparation_new/import/', preparation_new.preparation_new_import, name='preparation_new_import'),
    path('preparation_new/export/', preparation_new.preparation_new_export, name='preparation_new_export'),

    # 已有制剂进度描述
    path('api/preparations/<int:preparation_id>/descriptions/', preparation_new.get_preparation_descriptions,
         name='get-preparation-descriptions'),
    path('api/descriptions/<int:description_id>/delete/', preparation_new.delete_description,
         name='delete-description'),
    path('api/descriptions/<int:description_id>/edit/', preparation_new.edit_description, name='edit-description'),
    path('api/preparations/<int:preparation_id>/add-description/', preparation_new.add_preparation_description,
         name='add_preparation_description'),

    # 新品表
    path('product_new/', product_new.product_new, name='product_new'),
    path('product_new/add/', product_new.product_new_add, name='product_new_add'),
    path('product_new/edit/<int:_id>/', product_new.product_new_edit, name='product_new_edit'),
    path('product_new/delete/<int:_id>/', product_new.product_new_delete, name='product_new_delete'),
    path('product_new/import/', product_new.product_new_import, name='product_new_import'),
    path('product_new/export/', product_new.product_new_export, name='product_new_export'),

    # 新品进度描述
    path('api/product_new/<int:product_new_id>/descriptions/', product_new.get_product_descriptions,
         name='get-preparation-descriptions'),
    path('api/product_new/<int:description_id>/delete/', product_new.delete_description, name='delete-description'),
    path('api/product_new/<int:description_id>/edit/', product_new.edit_description, name='edit-description'),
    path('api/product_new/<int:product_new_id>/add-description/', product_new.add_product_description,
         name='add_preparation_description'),

]
