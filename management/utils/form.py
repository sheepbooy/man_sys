import re
from django.core.exceptions import ValidationError
from management import models
from management.utils.BootStrap import BootStrapModelForm


class EmployeesForm(BootStrapModelForm):
    """用来编辑员工全部信息的表单"""

    class Meta:
        model = models.Employees
        exclude = ['user']


class PasswordChangeForm(BootStrapModelForm):
    """更改密码表"""

    class Meta:
        model = models.Employees
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        # 禁用除了密码以外的所有字段
        for field_name in self.fields:
            if field_name != 'password':  # 假设密码字段名为 'password'
                self.fields[field_name].disabled = True


class EmployeesAddForm(BootStrapModelForm):
    """用户添加时的表单类"""

    class Meta:
        model = models.Employees
        exclude = ['user']
        # fields = '__all__'

    def clean_work_id(self):
        work_id = self.cleaned_data.get('work_id')
        # 使用正则表达式检查格式
        if not re.match(r'^[A-Z]{2}\d{3}$', work_id):
            raise ValidationError('工号必须是两个大写字母加三个数字')
        return work_id


class inner_trade_ledger_form(BootStrapModelForm):
    """内贸部台账表"""

    class Meta:
        model = models.InternalTradeLedger
        # fields = [
        #     'id', 'order_date', 'sales_date', 'contract_number', 'contract_returned', 'region_department',
        #     'province', 'city', 'year', 'month', 'industry_category', 'product_usage', 'company_name',
        #     'product_name', 'model', 'code', 'specification', 'quantity', 'unit_price', 'total_amount',
        #     'quantity1', 'unit_price1', 'increase_debit', 'decrease_credit', 'balance', 'f26', 'f27',
        #     'first_occurrence', 'new', 'second_occurrence', 'unreceived_payment', 'payment_date', 'old',
        #     'salesperson', 'acceptance_amount', 'cash', 'date', 'invoice_number', 'invoice_receipt_number',
        #     'sales_month', 'customer_type', 'logistics_shipment_date', 'waybill_number',
        #     'unit_price_below_current_price_list'
        # ]
        fields = '__all__'


class foreign_trade_ledger_form(BootStrapModelForm):
    """外贸部台账表"""

    class Meta:
        model = models.ForeignTradeLedger
        # fields = [
        #     'serial_number', 'order_date', 'sales_date', 'contract_number', 'customs_declaration', 'other_details',
        #     'country_province', 'nature', 'development_date', 'company_name', 'product_name', 'model', 'code',
        #     'specification', 'cash_sales_quantity', 'cash_sales_price_usd', 'cash_sales_price_cny',
        #     'cash_sales_total_usd', 'cash_sales_total_cny', 'accounts_receivable_sales_quantity',
        #     'accounts_receivable_sales_price_usd', 'accounts_receivable_sales_price_cny',
        #     'accounts_receivable_sales_total_usd', 'accounts_receivable_sales_total_cny',
        #     'accounts_receivable_debit_usd',
        #     'accounts_receivable_debit_cny', 'accounts_receivable_credit_usd', 'accounts_receivable_credit_cny',
        #     'order_amount_usd', 'order_amount_cny', 'payment_received_usd', 'payment_received_cny', 'first_occurrence',
        #     'customer_type', 'unreceived_payment_usd', 'unreceived_payment_cny', 'salesperson', 'payment_usd',
        #     'payment_cny', 'payment_date', 'invoice_number', 'invoice_receipt_number', 'sales_month',
        #     'international_freight_rmb', 'international_freight_usd', 'miscellaneous_fees', 'total_amount',
        #     'logistics_shipping_date', 'waybill_number', 'price_below_current_price_list', 'tax_refund_amount',
        #     'exchange_rate'
        # ]
        fields = '__all__'


class foreign_customer_form(BootStrapModelForm):
    """外贸部客户档案表"""

    class Meta:
        model = models.ForeignCustomerProfile
        # fields = [
        #     'customer_profile_number', 'salesperson', 'classification', 'development_date', 'company_name',
        #     'country', 'media', 'product_name', 'specification_code', 'specification_code_notes', 'usage',
        #     'follow_up_record', 'company_type', 'company_profile', 'customer_contact', 'customer_email',
        #     'customer_phone',
        #     'customer_website', 'preliminary_negotiation', 'samples', 'questionnaire', 'deal', 'supplier_audit',
        #     'estimated_annual_usage', 'current_supplier', 'level', 'model', 'unit_price', 'time', 'progress_description'
        # ]
        fields = '__all__'


class authorization_form(BootStrapModelForm):
    """授权书总表"""

    class Meta:
        model = models.Authorization
        # fields = [
        #     'authorization_number', 'issuance_month', 'product_name', 'registration_number',
        #     'registration_status', 'related_manufacturer', 'related_product_name', 'administration_route',
        #     'follow_up_person', 'review_status', 'acceptance_month', 'during_review_month', 'disappearing_month',
        #     'notes'
        # ]
        fields = '__all__'


class CustomerProfile_form(BootStrapModelForm):
    """研发部客户档案表"""

    class Meta:
        model = models.CustomerProfile
        # fields = [
        #     'customer_id', 'sales_department', 'province', 'research_capacity', 'company_name',
        #     'legal_representative', 'general_manager', 'license_number', 'gmp_certificate', 'company_type',
        #     'research_scope', 'drug', 'business_scale', 'number_of_employees', 'other_description',
        #     'customer_name', 'customer_mobile', 'customer_department', 'customer_job_level_assessment_abc',
        #     'initial_contact_time', 'customer_address', 'sample_time', 'sample_product', 'sample_model',
        #     'sample_quantity_grams', 'sample_purpose', 'sample_progress', 'sales_time', 'sales_product',
        #     'sales_specification', 'sales_unit_price_cny', 'sales_quantity_kg', 'sales_amount', 'sales_purpose',
        #     'sales_progress', 'phone_sales_visit_description'
        # ]
        fields = '__all__'


class CustomerEngagement_form(BootStrapModelForm):
    """研发部客户对接表"""

    class Meta:
        model = models.CustomerEngagement
        # fields = [
        #     'engagement_number', 'recorder', 'proactive_or_passive_engagement', 'company_name',
        #     'company_category', 'customer_name', 'customer_category', 'product_inquiry', 'price_inquiry',
        #     'sample_request', 'purchase', 'electronic_material_provision', 'physical_material_preparation',
        #     'sample_tracking', 'product_use_or_question_inquiry', 'product_name', 'specification_code',
        #     'weight', 'dosage_form_or_dosage_category', 'issue', 'is_resolved', 'resolution_solution'
        # ]
        fields = '__all__'


class CustomerFlow_form(BootStrapModelForm):
    """研发部客户流水表"""

    class Meta:
        model = models.CustomerFlow
        # fields = [
        #     'customer_id', 'sales_department', 'province', 'city', 'company_name',
        #     'company_type', 'company_size', 'company_address', 'customer_name', 'phone',
        #     'tags', 'department', 'position', 'job_level_assessment', 'sample_or_purchase',
        #     'level_of_contact', 'contact_person', 'overlapping_contacts', 'contact_method',
        #     'initial_contact_time', 'first_promotional_material', 'summer_gift_2021',
        #     'injection_books_2021', 'year_end_gift_delivery_2021', 'summer_gift_2022',
        #     'books_2022', 'major_customer_gift_2022', 'year_end_gift_2022', 'former_employer'
        # ]
        fields = '__all__'


class Products_form(BootStrapModelForm):
    """辅料表"""

    class Meta:
        model = models.Products
        # fields = [
        #     'category', 'product_name', 'specification', 'specification_features',
        #     'requirements', 'labels', 'spec_code'
        # ]
        fields = '__all__'


class Feedback_form(BootStrapModelForm):
    """问题反馈表"""

    class Meta:
        model = models.Feedback
        # fields = [
        #     'id', 'timestamp', 'department', 'product', 'related_formulation',
        #     'message', 'progress_status', 'contact_department_lead', 'details'
        # ]
        fields = '__all__'


class M_receivableForm(BootStrapModelForm):
    """202X年X月应收账款明细（原辅料、食品、研发、产品）："""

    class Meta:
        model = models.Receivable
        exclude = ['internal_trade_ledger_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置已填充字段为禁用状态
        self.fields['transaction_date'].widget.attrs['disabled'] = True
        self.fields['province'].widget.attrs['disabled'] = True
        self.fields['customer_name'].widget.attrs['disabled'] = True
        self.fields['salesperson'].widget.attrs['disabled'] = True
        self.fields['accounts_receivable'].widget.attrs['disabled'] = True
        self.fields['accounts_receivable_balance'].widget.attrs['disabled'] = True

        # 将以下字段设置为非必填项
        self.fields['transaction_date'].required = False
        self.fields['province'].required = False
        self.fields['customer_name'].required = False
        self.fields['salesperson'].required = False
        self.fields['accounts_receivable'].required = False
        self.fields['accounts_receivable_balance'].required = False


class OverdueForm(BootStrapModelForm):
    """截止202X年X月X日已逾期账款明细（原辅料、食品、研发、产品）"""

    class Meta:
        model = models.Overdue
        # fields = [
        #     'id', 'timestamp', 'department', 'product', 'related_formulation',
        #     'message', 'progress_status', 'contact_department_lead', 'details'
        # ]
        exclude = ['received_id']


class Foreign_receivable_form(BootStrapModelForm):
    """应收账款明细（外贸部）"""

    class Meta:
        model = models.Foreign_receivable

        exclude = ['foreign_trade_ledger_id']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置已填充字段为禁用状态
        self.fields['transaction_date'].widget.attrs['disabled'] = True
        self.fields['customer_name'].widget.attrs['disabled'] = True
        self.fields['salesperson'].widget.attrs['disabled'] = True
        self.fields['accounts_receivable_usd'].widget.attrs['disabled'] = True
        self.fields['accounts_receivable_rmb'].widget.attrs['disabled'] = True

        # 将以下字段设置为非必填项
        self.fields['transaction_date'].required = False
        self.fields['customer_name'].required = False
        self.fields['salesperson'].required = False
        self.fields['accounts_receivable_usd'].required = False
        self.fields['accounts_receivable_rmb'].required = False


class Complaint_summary_form(BootStrapModelForm):
    """全国客诉汇总"""

    class Meta:
        model = models.ComplaintSummary
        fields = '__all__'


class Sales_Visit_Form(BootStrapModelForm):
    """销售客户拜访报告"""

    class Meta:
        model = models.SalesVisitReport
        fields = '__all__'


class Sales_Forecast_Form(BootStrapModelForm):
    """预算详情表"""

    class Meta:
        model = models.SalesForecast
        fields = '__all__'


class Medicine_Form(BootStrapModelForm):
    """仿制药参比制剂目录"""

    class Meta:
        model = models.Medicine
        exclude = ['id']


class CustomerAudit_Form(BootStrapModelForm):
    """客户审计表"""

    class Meta:
        model = models.CustomerAudit
        fields = '__all__'


class PreparationNew_Form(BootStrapModelForm):
    """已有变更"""

    class Meta:
        model = models.preparation_new
        fields = '__all__'


class PreparationDescription_Form(BootStrapModelForm):
    """已有变更进度描述"""

    class Meta:
        model = models.PreparationDescription
        fields = ['date', 'description']  # 根据你的模型字段调整


class ProductNew_Form(BootStrapModelForm):
    """新品开发"""

    class Meta:
        model = models.product_new
        fields = '__all__'
