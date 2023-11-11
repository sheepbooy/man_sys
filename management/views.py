from django import forms
from django.shortcuts import render, redirect
from django.core.validators import RegexValidator
from management import models
from django.db.models import Q
from management.utils.pagination import Pagination


class EmployeesForm(forms.ModelForm):
    """员工信息表类"""

    class Meta:
        model = models.Employees
        # fields = ['na/me', 'password', 'department', 'gender', 'position', 'work_id', 'status']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class inner_trade_ledger_form(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class foreign_trade_ledger_form(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class foreign_customer_form(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class ExistingFormulationToDevelop_form(forms.ModelForm):
    """已有制剂待开发表"""

    class Meta:
        model = models.ExistingFormulationToDevelop
        # fields = [
        #     'serial_number', 'enterprise_name', 'province', 'city', 'department', 'specific_department',
        #     'responsible_person', 'customer_name', 'customer_source', 'product', 'corresponding_specification_code',
        #     'special_requirements', 'estimated_annual_consumption', 'current_manufacturer', 'product_level',
        #     'model_number',
        #     'price_per_kg', 'sample_sales', 'is_repeated_project', 'first_quotation', 'quantity', 'unit_price',
        #     'amount',
        #     'formulation_name', 'is_consistency_evaluation_product', 'auxiliary_material_usage', 'prescription_dosage',
        #     'development_date', 'customer_importance', 'initial_negotiation', 'supplier_change_request',
        #     'supplier_audit',
        #     'continuous_batch_sample_testing', 'first_production_of_3_batches', 'stability_study',
        #     'additional_application_record_change', 'formal_contract_signing', 'delivery', 'in_progress', 'notes',
        #     'before_pilot_scale_up', 'before_submission', 'issuing_time', 'landing_enterprise_name', 'contact_person',
        #     'handover_sales_manager', 'handover_time'
        # ]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class ExistingFormulationDeveloping_form(forms.ModelForm):
    """已有制剂开发中表"""

    class Meta:
        model = models.ExistingFormulationDeveloping
        # fields = [
        #     'serial_number', 'enterprise_name', 'province', 'city', 'department', 'specific_department',
        #     'responsible_person', 'customer_name', 'customer_source', 'product', 'corresponding_specification_code',
        #     'special_requirements', 'estimated_annual_consumption', 'current_manufacturer', 'product_level',
        #     'model_number',
        #     'price_per_kg', 'sample_sales', 'is_repeated_project', 'first_quotation', 'quantity', 'unit_price',
        #     'amount',
        #     'formulation_name', 'is_consistency_evaluation_product', 'auxiliary_material_usage', 'prescription_dosage',
        #     'development_date', 'customer_importance', 'initial_negotiation', 'supplier_change_request',
        #     'supplier_audit',
        #     'continuous_batch_sample_testing', 'first_production_of_3_batches', 'stability_study',
        #     'additional_application_record_change', 'formal_contract_signing', 'delivery', 'in_progress', 'notes',
        #     'before_pilot_scale_up', 'before_submission', 'issuing_time', 'landing_enterprise_name', 'contact_person',
        #     'handover_sales_manager', 'handover_time'
        # ]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class ExistingProductCompleted_form(forms.ModelForm):
    """已有制剂开发完成表"""

    class Meta:
        model = models.ExistingProductCompleted
        # fields = [
        #     'serial_number', 'enterprise_name', 'province', 'city', 'department', 'specific_department',
        #     'responsible_person',
        #     'customer_name', 'customer_source', 'product', 'corresponding_specification_code', 'special_requirements',
        #     'estimated_annual_consumption', 'current_manufacturer', 'product_level', 'model_number', 'price_per_kg',
        #     'sample_sales',
        #     'is_repeated_project', 'first_quotation', 'quantity', 'unit_price', 'amount', 'formulation_name',
        #     'is_consistency_evaluation_product', 'auxiliary_material_usage', 'prescription_dosage', 'development_date',
        #     'customer_importance', 'initial_negotiation', 'supplier_change_request', 'supplier_audit',
        #     'continuous_batch_sample_testing', 'first_production_of_3_batches', 'stability_study',
        #     'additional_application_record_change', 'formal_contract_signing', 'delivery', 'in_progress', 'notes',
        #     'before_pilot_scale_up', 'before_submission', 'issuing_time', 'landing_enterprise_name', 'contact_person',
        #     'handover_sales_manager', 'handover_time'
        # ]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class authorization_form(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class NewProductDeveloping_form(forms.ModelForm):
    """新品开发中表"""

    class Meta:
        model = models.NewProductDevelopingProgress
        # fields = [
        #     'serial_number', 'company_name', 'province', 'city', 'department',
        #     'specific_department', 'manager', 'customer_name', 'customer_source', 'product',
        #     'specification_code', 'special_requirements', 'sample_or_sale', 'is_duplicate_project',
        #     'initial_quote', 'quantity', 'unit_price', 'amount', 'formulation_name',
        #     'is_consistency_evaluation_product', 'excipient_purpose', 'prescription_quantity',
        #     'start_development_date', 'customer_importance', 'excipient_inspection',
        #     'prescription_selection', 'preliminary_process_validation_small_scale', 'pilot_scale_verification',
        #     'process_verification', 'clinical_trials', 'approval_received', 'regular_purchase',
        #     'response_needed', 'in_progress', 'notes', 'before_pilot_scale', 'before_submission',
        #     'issuance_date', 'landing_company_name', 'contact_person', 'transfer_to_sales_manager', 'transfer_date'
        # ]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class NewProductCompleted_form(forms.ModelForm):
    """新品已完成"""

    class Meta:
        model = models.NewProductCompleted
        # fields = [
        #     'serial_number', 'company_name', 'province', 'city', 'department',
        #     'specific_department', 'manager', 'customer_name', 'customer_source', 'product',
        #     'specification_code', 'special_requirements', 'sample_or_sale', 'is_duplicate_project',
        #     'initial_quote', 'quantity', 'unit_price', 'amount', 'formulation_name',
        #     'is_consistency_evaluation_product', 'excipient_purpose', 'prescription_quantity',
        #     'start_development_date', 'customer_importance', 'excipient_inspection',
        #     'prescription_selection', 'preliminary_process_validation_small_scale', 'pilot_scale_verification',
        #     'process_verification', 'clinical_trials', 'approval_received', 'regular_purchase',
        #     'response_needed', 'in_progress', 'notes', 'before_pilot_scale', 'before_submission',
        #     'issuance_date', 'landing_company_name', 'contact_person', 'transfer_to_sales_manager', 'transfer_date'
        # ]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class NewProductDevelopment_form(forms.ModelForm):
    """新品进度描述表"""

    class Meta:
        model = models.NewProductDevelopment
        # fields = [
        #     'id', 'timestamp', 'progress', 'status', 'subordinate_id',
        # ]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class ExistingFormulationProgressDescription_form(forms.ModelForm):
    """已有制剂仅需描述表"""

    class Meta:
        model = models.ExistingFormulationProgressDescription
        # fields = [
        #     'id', 'timestamp', 'progress', 'status', 'subordinate_id',
        # ]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class CustomerProfile_form(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class CustomerEngagement_form(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class CustomerFlow_form(forms.ModelForm):
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class Products_form(forms.ModelForm):
    """辅料表"""

    class Meta:
        model = models.Products
        # fields = [
        #     'category', 'product_name', 'specification', 'specification_features',
        #     'requirements', 'labels', 'spec_code'
        # ]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class Feedback_form(forms.ModelForm):
    """问题反馈表"""

    class Meta:
        model = models.Feedback
        # fields = [
        #     'id', 'timestamp', 'department', 'product', 'related_formulation',
        #     'message', 'progress_status', 'contact_department_lead', 'details'
        # ]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                # 为该字段应用时间选择插件
                field.widget.attrs['class'] = 'datepicker form-control'
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


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


def employees_list(request):
    """所有员工信息表"""
    value = request.GET.get('q', '')
    # 创建一个空的Q对象
    if value is not None:
        query = Q()
        # 获取模型的字段列表
        fields = models.Employees._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "id":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.Employees.objects.filter(query)
    else:
        query_set = models.Employees.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }

    return render(request, 'employees_list.html', context)


def inner_trade_ledger(request):
    """内贸部台账表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.InternalTradeLedger._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "id":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.InternalTradeLedger.objects.filter(query)
    else:
        query_set = models.InternalTradeLedger.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'inner_trade_ledger.html', context)


def foreign_trade_ledger(request):
    """外贸部台账表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.ForeignTradeLedger._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "serial_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.ForeignTradeLedger.objects.filter(query)
    else:
        query_set = models.ForeignTradeLedger.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'foreign_trade_ledger.html', context)


def foreign_customer(request):
    """外贸部客户档案"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.ForeignCustomerProfile._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.ForeignCustomerProfile.objects.filter(query)
    else:
        query_set = models.ForeignCustomerProfile.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'foreign_customer_list.html', context)


def preparation(request, _type):
    """已有制剂的已完成，待开发，开发中进度表"""
    model_map = {
        'completed': models.ExistingProductCompleted,
        'ing': models.ExistingFormulationDeveloping,
        'todev': models.ExistingFormulationToDevelop
    }

    value = request.GET.get('q', '')
    model = model_map.get(_type)  # 定义一个默认的model

    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        if model:
            # 获取模型的字段列表
            fields = model._meta.fields
            for field in fields:
                if field.name != "serial_number":  # 排除默认的AutoField "id"字段
                    # 创建Q对象，并将字段名和搜索值拼接成查询条件
                    q = Q(**{f"{field.name}__icontains": value})
                    # 使用|操作符将Q对象添加到主查询中
                    query |= q

            query_set = model.objects.filter(query)
        else:
            query_set = None
    else:
        query_set = model.objects.all() if model else None

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value,
        'type': _type,
    }
    return render(request, 'preparation.html', context)


def authorization(request):
    """授权书总表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.Authorization._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.Authorization.objects.filter(query)
    else:
        query_set = models.Authorization.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'authorization.html', context)


def new(request, _type):
    """新品开发中，已完成进度表"""
    model_map = {
        'ing': models.NewProductDevelopingProgress,
        'completed': models.NewProductCompleted
    }

    value = request.GET.get('q', '')
    model = model_map.get(_type)  # 获取相应的模型

    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        if model:
            # 获取模型的字段列表
            fields = model._meta.fields
            for field in fields:
                if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                    # 创建Q对象，并将字段名和搜索值拼接成查询条件
                    q = Q(**{f"{field.name}__icontains": value})
                    # 使用|操作符将Q对象添加到主查询中
                    query |= q

            query_set = model.objects.filter(query)
        else:
            query_set = None
    else:
        query_set = model.objects.all() if model else None

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value,
        'type': _type
    }
    return render(request, 'new_product.html', context)


def progress(request, _type):
    """新品，已有制剂进度描述表"""
    model_map = {
        'new': models.NewProductDevelopment,
        'preparation': models.ExistingFormulationProgressDescription
    }

    value = request.GET.get('q', '')
    model = model_map.get(_type)  # 获取相应的模型

    if value is not None:
        query = Q(subordinate_id__icontains=value)
        query_set = model.objects.filter(query) if model else None
    else:
        query_set = model.objects.all() if model else None

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value,
        'type': _type,
    }
    return render(request, 'progress.html', context)


def dev_custom(request):
    """研发部客户档案表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.CustomerProfile._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.CustomerProfile.objects.filter(query)
    else:
        query_set = models.CustomerProfile.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'dev_custom.html', context)


def butting(request):
    """研发部客户对接表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.CustomerEngagement._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.CustomerEngagement.objects.filter(query)
    else:
        query_set = models.CustomerEngagement.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'butting.html', context)


def turnover(request):
    """研发部客户流水表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.CustomerFlow._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.CustomerFlow.objects.filter(query)
    else:
        query_set = models.CustomerFlow.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'turnover.html', context)


def product(request):
    """辅料表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.Products._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.Products.objects.filter(query)
    else:
        query_set = models.Products.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'product.html', context)


def question(request):
    """问题调查表"""
    value = request.GET.get('q', '')
    if value is not None:
        # 创建一个空的Q对象
        query = Q()
        # 获取模型的字段列表
        fields = models.Feedback._meta.fields
        # 遍历字段列表并创建相应的Q对象
        for field in fields:
            if field.name != "customer_profile_number":  # 排除默认的AutoField "id"字段
                # 创建Q对象，并将字段名和搜索值拼接成查询条件
                q = Q(**{f"{field.name}__icontains": value})
                # 使用|操作符将Q对象添加到主查询中
                query |= q
        query_set = models.Feedback.objects.filter(query)
    else:
        query_set = models.Feedback.objects.all()

    page_object = Pagination(request, query_set)
    page_object.html()

    context = {
        'page_queryset': page_object.page_queryset,
        'page_string': page_object.page_string,
        'value': value
    }
    return render(request, 'question.html', context)


def emplo_detail(request, _id):
    """用户详情页"""
    employee = models.Employees.objects.filter(work_id=_id).first()
    return render(request, 'emplo_detail.html', {'employee': employee})


# 增加功能
# ----------------------------------------------------------------
def employees_add(request):
    """员工信息添加"""
    if request.method == 'GET':
        form = EmployeesForm()
        return render(request, 'employees_add.html', {'form': form})

    form = EmployeesForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/employees/')

    return render(request, 'employees_add.html', {'form': form})


def inner_trade_ledger_add(request):
    """内贸部台账表添加"""
    if request.method == 'GET':
        form = inner_trade_ledger_form()
        return render(request, 'inner_trade_ledger_add.html', {'form': form})

    form = inner_trade_ledger_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/innertrade/ledger/')

    return render(request, 'inner_trade_ledger_add.html', {'form': form})


def foreign_trade_ledger_add(request):
    """外贸部台账添加"""
    if request.method == 'GET':
        form = foreign_trade_ledger_form()
        return render(request, 'foreign_trade_ledger_add.html', {'form': form})

    form = foreign_trade_ledger_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/foreign/ledger/')

    return render(request, 'foreign_trade_ledger_add.html', {'form': form})


def foreign_customer_add(request):
    """外贸部客户添加"""
    if request.method == 'GET':
        form = foreign_customer_form()
        return render(request, 'foreign_customer_add.html', {'form': form})

    form = foreign_customer_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/foreign/customer/')

    return render(request, 'foreign_customer_add.html', {'form': form})


def preparation_add(request, _type):
    """已有制剂（待开发，开发中，已完成）添加"""
    form_cls = {
        'completed': ExistingProductCompleted_form,
        'ing': ExistingFormulationDeveloping_form,
        'todev': ExistingFormulationToDevelop_form,
    }.get(_type)
    template_cls = {
        'completed': 'ExistingFormulationCompleted',
        'ing': 'ExistingFormulationDeveloping',
        'todev': 'ExistingFormulationToDevelop',
    }.get(_type)
    if request.method == 'GET':
        form = form_cls()
        return render(request, f'{template_cls}_add.html', {'form': form})
    form = form_cls(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(f'/preparation/{_type}/')
    return render(request, f'{template_cls}_add.html', {'form': form})


def authorization_add(request):
    """授权书添加"""
    if request.method == 'GET':
        form = authorization_form()
        return render(request, 'authorization_add.html', {'form': form})

    form = authorization_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/authorization/')

    return render(request, 'authorization_add.html', {'form': form})


def new_add(request, _type):
    """新品（已完成，开发中）添加"""
    form_cls = {
        'completed': NewProductCompleted_form,
        'ing': NewProductDeveloping_form,
    }.get(_type)
    template_cls = {
        'completed': 'NewProductCompleted',
        'ing': 'NewProductDeveloping',
    }.get(_type)
    if request.method == 'GET':
        form = form_cls()
        return render(request, f'{template_cls}_add.html', {'form': form})
    form = form_cls(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(f'/new/{_type}/')
    return render(request, f'{template_cls}_add.html', {'form': form})


def progress_add(request, _type):
    """添加新品或已有制剂的进度描述"""
    form_cls = {
        'new': NewProductDevelopment_form,
        'preparation': ExistingFormulationProgressDescription_form,
    }.get(_type)
    template_cls = {
        'new': 'NewProductDevelopment',
        'preparation': 'ExistingFormulationProgressDescription',
    }.get(_type)

    if request.method == 'GET':
        form = form_cls()
        return render(request, f'{template_cls}_add.html', {'form': form})
    form = form_cls(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(f'/progress/{_type}/')
    return render(request, f'{template_cls}_add.html', {'form': form})


def dev_custom_add(request):
    """研发部客户档案添加"""
    if request.method == 'GET':
        form = CustomerProfile_form()
        return render(request, 'dev_custom_add.html', {'form': form})

    form = CustomerProfile_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/develop/customer/')

    return render(request, 'dev_custom_add.html', {'form': form})


def butting_add(request):
    """研发部客户对接表添加"""
    if request.method == 'GET':
        form = CustomerEngagement_form()
        return render(request, 'butting_add.html', {'form': form})

    form = CustomerEngagement_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/develop/butting/')

    return render(request, 'butting_add.html', {'form': form})


def turnover_add(request):
    """研发部客户流水表添加"""
    if request.method == 'GET':
        form = CustomerFlow_form()
        return render(request, 'turnover_add.html', {'form': form})

    form = CustomerFlow_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/develop/turnover/')

    return render(request, 'turnover_add.html', {'form': form})


def product_add(request):
    """辅料表添加"""
    if request.method == 'GET':
        form = Products_form()
        return render(request, 'product_add.html', {'form': form})

    form = Products_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/product/')

    return render(request, 'product_add.html', {'form': form})


def question_add(request):
    """问题反馈表添加"""
    if request.method == 'GET':
        form = Feedback_form()
        return render(request, 'question_add.html', {'form': form})

    form = Feedback_form(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/question/')

    return render(request, 'question_add.html', {'form': form})


# 编辑功能
# ----------------------------------------------------------------
def employees_edit(request, _id):
    """编辑员工信息"""
    row_object = models.Employees.objects.filter(work_id=_id).first()

    if request.method == 'GET':
        form = EmployeesForm(instance=row_object)
        return render(request, 'employees_edit.html', {'form': form})

    form = EmployeesForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/employees/')

    return render(request, 'employees_add.html', {'form': form})


def inner_trade_ledger_edit(request, _id):
    """编辑内贸部台账信息"""
    row_object = models.InternalTradeLedger.objects.filter(id=_id).first()

    if request.method == 'GET':
        form = inner_trade_ledger_form(instance=row_object)
        return render(request, 'inner_trade_ledger_edit.html', {'form': form})

    form = inner_trade_ledger_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/innertrade/ledger/')

    return render(request, 'inner_trade_ledger_edit.html', {'form': form})


def foreign_trade_ledger_edit(request, _id):
    """编辑外贸部台账表"""
    row_object = models.ForeignTradeLedger.objects.filter(serial_number=_id).first()
    if request.method == 'GET':
        form = foreign_trade_ledger_form(instance=row_object)
        return render(request, 'foreign_trade_ledger_edit.html', {'form': form})

    form = foreign_trade_ledger_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/foreign/ledger/')

    return render(request, 'foreign_trade_ledger_edit.html', {'form': form})


def foreign_customer_edit(request, _id):
    """编辑外贸部客户信息"""
    row_object = models.ForeignCustomerProfile.objects.filter(customer_profile_number=_id).first()
    if request.method == 'GET':
        form = foreign_customer_form(instance=row_object)
        return render(request, 'foreign_customer_edit.html', {'form': form})

    form = foreign_customer_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/foreign/customer/')

    return render(request, 'foreign_customer_edit.html', {'form': form})


def preparation_edit(request, _type, _id):
    """已有制剂开发表"""
    form_cls = {
        'completed': ExistingProductCompleted_form,
        'ing': ExistingFormulationDeveloping_form,
        'todev': ExistingFormulationToDevelop_form,
    }.get(_type)
    template_cls = {
        'completed': 'ExistingFormulationCompleted',
        'ing': 'ExistingFormulationDeveloping',
        'todev': 'ExistingFormulationToDevelop',
    }.get(_type)
    if _type == 'completed':
        row_object = models.ExistingProductCompleted.objects.filter(serial_number=_id).first()
    elif _type == 'todev':
        row_object = models.ExistingFormulationToDevelop.objects.filter(serial_number=_id).first()
    elif _type == 'ing':
        row_object = models.ExistingFormulationDeveloping.objects.filter(serial_number=_id).first()
    if request.method == 'GET':
        form = form_cls(instance=row_object)
        return render(request, f'{template_cls}_edit.html', {'form': form})
    form = form_cls(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect(f'/preparation/{_type}/')
    return render(request, f'{template_cls}_edit.html', {'form': form})


def authorization_edit(request, _id):
    """编辑授权书总表"""
    row_object = models.Authorization.objects.filter(authorization_number=_id).first()
    if request.method == 'GET':
        form = authorization_form(instance=row_object)
        return render(request, 'authorization_edit.html', {'form': form})

    form = authorization_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/authorization/')

    return render(request, 'authorization_edit.html', {'form': form})


def new_edit(request, _type, _id):
    """编辑新品开发表"""
    if _type == 'ing':
        row_object = models.NewProductDevelopingProgress.objects.filter(serial_number=_id).first()
    elif _type == 'completed':
        row_object = models.NewProductCompleted.objects.filter(serial_number=_id).first()
    form_cls = {
        'completed': NewProductCompleted_form,
        'ing': NewProductDeveloping_form,
    }.get(_type)
    template_cls = {
        'completed': 'NewProductCompleted',
        'ing': 'NewProductDeveloping',
    }.get(_type)
    if request.method == 'GET':
        form = form_cls(instance=row_object)
        return render(request, f'{template_cls}_edit.html', {'form': form})
    form = form_cls(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect(f'/new/{_type}/')
    return render(request, f'{template_cls}_edit.html', {'form': form})


def progress_edit(request, _type, _id):
    """新品和已有制剂进度描述信息"""
    if _type == 'new':
        row_object = models.NewProductDevelopment.objects.filter(id=_id).first()
    elif _type == 'preparation':
        row_object = models.ExistingFormulationProgressDescription.objects.filter(id=_id).first()
    form_cls = {
        'new': NewProductDevelopment_form,
        'preparation': ExistingFormulationProgressDescription_form,
    }.get(_type)
    template_cls = {
        'new': 'NewProductDevelopment',
        'preparation': 'ExistingFormulationProgressDescription',
    }.get(_type)

    if request.method == 'GET':
        form = form_cls(instance=row_object)
        return render(request, f'{template_cls}_edit.html', {'form': form})
    form = form_cls(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect(f'/progress/{_type}/')
    return render(request, f'{template_cls}_edit.html', {'form': form})


def dev_custom_edit(request, _id):
    """编辑研发部客户档案"""
    row_object = models.CustomerProfile.objects.filter(customer_id=_id).first()
    if request.method == 'GET':
        form = CustomerProfile_form(instance=row_object)
        return render(request, 'dev_custom_edit.html', {'form': form})

    form = CustomerProfile_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/develop/customer/')

    return render(request, 'dev_custom_edit.html', {'form': form})


def butting_edit(request, _id):
    """编辑研发部客户对接表"""
    row_object = models.CustomerEngagement.objects.filter(engagement_number=_id).first()
    if request.method == 'GET':
        form = CustomerEngagement_form(instance=row_object)
        return render(request, 'butting_edit.html', {'form': form})

    form = CustomerEngagement_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/develop/butting/')

    return render(request, 'butting_edit.html', {'form': form})


def turnover_edit(request, _id):
    """编辑研发部客户流水表"""
    row_object = models.CustomerFlow.objects.filter(customer_id=_id).first()
    if request.method == 'GET':
        form = CustomerFlow_form(instance=row_object)
        return render(request, 'turnover_edit.html', {'form': form})

    form = CustomerFlow_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/develop/turnover/')

    return render(request, 'turnover_edit.html', {'form': form})


def product_edit(request, _id):
    """编辑药用辅料表"""
    row_object = models.Products.objects.filter(spec_code=_id).first()
    if request.method == 'GET':
        form = Products_form(instance=row_object)
        return render(request, 'product_edit.html', {'form': form})

    form = Products_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/product/')

    return render(request, 'product_edit.html', {'form': form})


def question_edit(request, _id):
    """编辑问题反馈表"""
    row_object = models.Feedback.objects.filter(id=_id).first()
    if request.method == 'GET':
        form = Feedback_form(instance=row_object)
        return render(request, 'question_edit.html', {'form': form})

    form = Feedback_form(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/question/')

    return render(request, 'question_edit.html', {'form': form})


# 删除功能
# ----------------------------------------------------------------
def employees_delete(request, _id):
    """用户删除"""
    models.Employees.objects.filter(work_id=_id).delete()
    return redirect('/employees/')


def inner_trade_ledger_delete(request, _id):
    """内贸部台账表删除"""
    models.InternalTradeLedger.objects.filter(id=_id).delete()
    return redirect('/innertrade/ledger/')


def foreign_trade_ledger_delete(request, _id):
    """外贸部台账删除"""
    models.ForeignTradeLedger.objects.filter(serial_number=_id).delete()
    return redirect('/foreign/ledger/')


def foreign_customer_delete(request, _id):
    """外贸部客户删除"""
    models.ForeignCustomerProfile.objects.filter(customer_profile_number=_id).delete()
    return redirect('/foreign/customer/')


def preparation_delete(request, _type, _id):
    """删除已有制剂开发表"""
    if _type == 'completed':
        models.ExistingProductCompleted.objects.filter(serial_number=_id).delete()
    elif _type == 'ing':
        models.ExistingFormulationDeveloping.objects.filter(serial_number=_id).delete()
    elif _type == 'todev':
        models.ExistingFormulationToDevelop.objects.filter(serial_number=_id).delete()
    return redirect(f'/preparation/{_type}/')


def authorization_delete(request, _id):
    """授权表删除"""
    row_object = models.Authorization.objects.filter(authorization_number=_id).delete()
    return redirect('/authorization/')


def new_delete(request, _type, _id):
    """删除新品开发表"""
    if _type == 'ing':
        models.NewProductDevelopingProgress.objects.filter(serial_number=_id).delete()
    elif _type == 'completed':
        models.NewProductCompleted.objects.filter(serial_number=_id).delete()
    return redirect(f'/new/{_type}/')


def progress_delete(request, _type, _id):
    """编辑进度描述信息"""
    if _type == 'new':
        models.NewProductDevelopment.objects.filter(id=_id).delete()
    elif _type == 'preparation':
        models.ExistingFormulationProgressDescription.objects.filter(id=_id).delete()
    return redirect(f'/progress/{_type}/')


def dev_custom_delete(request, _id):
    """删除研发部客户信息"""
    models.CustomerProfile.objects.filter(customer_id=_id).delete()
    return redirect('/develop/customer/')


def butting_delete(request, _id):
    """删除研发部客户对接信息"""
    models.CustomerEngagement.objects.filter(engagement_number=_id).delete()
    return redirect('/develop/butting/')


def turnover_delete(request, _id):
    """删除研发部客户流水信息"""
    models.CustomerFlow.objects.filter(customer_id=_id).delete()
    return redirect('/develop/turnover/')


def product_delete(request, _id):
    """删除辅料信息"""
    models.Products.objects.filter(spec_code=_id).delete()
    return redirect('/product/')


def question_delete(request, _id):
    """编辑问题反馈信息"""
    models.Feedback.objects.filter(id=_id).delete()
    return redirect('/question/')
