from management import models
from management.utils.BootStrap import BootStrapModelForm


class EmployeesForm(BootStrapModelForm):
    """员工信息表类"""

    class Meta:
        model = models.Employees
        # fields = ['na/me', 'password', 'department', 'gender', 'position', 'work_id', 'status']
        fields = '__all__'


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


class ExistingFormulationToDevelop_form(BootStrapModelForm):
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


class ExistingFormulationDeveloping_form(BootStrapModelForm):
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


class ExistingProductCompleted_form(BootStrapModelForm):
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


class NewProductDeveloping_form(BootStrapModelForm):
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


class NewProductCompleted_form(BootStrapModelForm):
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


class NewProductDevelopment_form(BootStrapModelForm):
    """新品进度描述表"""

    class Meta:
        model = models.NewProductDevelopment
        # fields = [
        #     'id', 'timestamp', 'progress', 'status', 'subordinate_id',
        # ]
        fields = '__all__'


class ExistingFormulationProgressDescription_form(BootStrapModelForm):
    """已有制剂仅需描述表"""

    class Meta:
        model = models.ExistingFormulationProgressDescription
        # fields = [
        #     'id', 'timestamp', 'progress', 'status', 'subordinate_id',
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
        model = models.Complaint_summary
        fields = '__all__'
