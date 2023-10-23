from django.db import models
# Create your models here.


class Products(models.Model):
    category = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    specification = models.CharField(max_length=255, blank=True, null=True)
    specification_features = models.CharField(max_length=255, blank=True, null=True)
    requirements = models.CharField(max_length=255, blank=True, null=True)
    labels = models.CharField(max_length=255, blank=True, null=True)
    spec_code = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = '辅料'


class InternalTradeLedger(models.Model):
    id = models.AutoField(primary_key=True)
    order_date = models.CharField(max_length=255, blank=True, null=True)
    sales_date = models.CharField(max_length=255, blank=True, null=True)
    contract_number = models.CharField(max_length=255, blank=True, null=True)
    contract_returned = models.CharField(max_length=255, blank=True, null=True)
    region_department = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    month = models.CharField(max_length=255, blank=True, null = True)
    industry_category = models.CharField(max_length=255, blank=True, null=True)
    product_usage = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    specification = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.CharField(max_length=255, blank=True, null=True)
    total_amount = models.CharField(max_length=255, blank=True, null=True)
    quantity1 = models.CharField(max_length=255, blank=True, null=True)
    unit_price1 = models.CharField(max_length=255, blank=True, null=True)
    increase_debit = models.CharField(max_length=255, blank=True, null=True)
    decrease_credit = models.CharField(max_length=255, blank=True, null=True)
    balance = models.CharField(max_length=255, blank=True, null=True)
    f26 = models.CharField(max_length=255, blank=True, null=True)
    f27 = models.CharField(max_length=255, blank=True, null=True)
    first_occurrence = models.CharField(max_length=255, blank=True, null=True)
    new = models.CharField(max_length=255, blank=True, null=True)
    second_occurrence = models.CharField(max_length=255, blank=True, null=True)
    unreceived_payment = models.CharField(max_length=255, blank=True, null=True)
    payment_date = models.CharField(max_length=255, blank=True, null=True)
    old = models.CharField(max_length=255, blank=True, null=True)
    salesperson = models.CharField(max_length=255, blank=True, null=True)
    acceptance_amount = models.CharField(max_length=255, blank=True, null=True)
    cash = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    invoice_number = models.CharField(max_length=255, blank=True, null=True)
    invoice_receipt_number = models.CharField(max_length=255, blank=True, null=True)
    sales_month = models.CharField(max_length=255, blank=True, null=True)
    customer_type = models.CharField(max_length=255, blank=True, null=True)
    logistics_shipment_date = models.CharField(max_length=255, blank=True, null=True)
    waybill_number = models.CharField(max_length=255, blank=True, null=True)
    unit_price_below_current_price_list = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '内贸部台账'


class Authorization(models.Model):
    authorization_number = models.AutoField(primary_key=True)
    issuance_month = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    registration_number = models.CharField(max_length=255, blank=True, null=True)
    registration_status = models.CharField(max_length=255, blank=True, null=True)
    related_manufacturer = models.CharField(max_length=255, blank=True, null=True)
    related_product_name = models.CharField(max_length=255, blank=True, null=True)
    administration_route = models.CharField(max_length=255, blank=True, null=True)
    follow_up_person = models.CharField(max_length=255, blank=True, null=True)
    review_status = models.CharField(max_length=255, blank=True, null=True)
    acceptance_month = models.CharField(max_length=255, blank=True, null=True)
    during_review_month = models.CharField(max_length=255, blank=True, null=True)
    disappearing_month = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '授权书总表'


class ForeignCustomerProfile(models.Model):
    customer_profile_number = models.AutoField(primary_key=True)
    salesperson = models.CharField(max_length=255, blank=True, null=True)
    classification = models.CharField(max_length=255, blank=True, null=True)
    development_date = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    media = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    specification_code = models.CharField(max_length=255, blank=True, null=True)
    specification_code_notes = models.CharField(max_length=255, blank=True, null=True)
    usage = models.CharField(max_length=255, blank=True, null=True)
    follow_up_record = models.CharField(max_length=255, blank=True, null=True)
    company_type = models.CharField(max_length=255, blank=True, null=True)
    company_profile = models.TextField(blank=True, null=True)
    customer_contact = models.CharField(max_length=255, blank=True, null=True)
    customer_email = models.CharField(max_length=255, blank=True, null=True)
    customer_phone = models.CharField(max_length=255, blank=True, null=True)
    customer_website = models.CharField(max_length=255, blank=True, null=True)
    preliminary_negotiation = models.CharField(max_length=255, blank=True, null=True)
    samples = models.CharField(max_length=255, blank=True, null=True)
    questionnaire = models.CharField(max_length=255, blank=True, null=True)
    deal = models.CharField(max_length=255, blank=True, null=True)
    supplier_audit = models.CharField(max_length=255, blank=True, null=True)
    estimated_annual_usage = models.CharField(max_length=255, blank=True, null=True)
    current_supplier = models.CharField(max_length=255, blank=True, null=True)
    level = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.CharField(max_length=255, blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    progress_description = models.TextField(blank=True, null=True)


    class Meta:
            managed = False
            db_table = '外贸部客户档案表'


class ForeignTradeLedger(models.Model):
    serial_number  = models.AutoField(primary_key=True)
    order_date  = models.CharField(max_length=255, blank=True, null=True)
    sales_date  = models.CharField(max_length=255, blank=True, null=True)
    contract_number  = models.CharField(max_length=255, blank=True, null=True)
    customs_declaration  = models.CharField(max_length=255, blank=True, null=True)
    other_details  = models.CharField(max_length=255, blank=True, null=True)
    country_province  = models.CharField(db_column='国家/省份', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nature  = models.CharField(max_length=255, blank=True, null=True)
    development_date  = models.CharField(max_length=255, blank=True, null=True)
    company_name  = models.CharField(max_length=255, blank=True, null=True)
    product_name  = models.CharField(max_length=255, blank=True, null=True)
    model  = models.CharField(max_length=255, blank=True, null=True)
    code  = models.CharField(max_length=255, blank=True, null=True)
    specification  = models.CharField(max_length=255, blank=True, null=True)
    cash_sales_quantity  = models.CharField(max_length=255, blank=True, null=True)
    cash_sales_price_usd  = models.CharField(db_column='现款销售单价（USD）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cash_sales_price_cny  = models.CharField(db_column='现款销售单价（人民币）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cash_sales_total_usd  = models.CharField(db_column='现款销售总额（USD）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cash_sales_total_cny  = models.CharField(db_column='现款销售总额（人民币）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    accounts_receivable_sales_quantity  = models.CharField(max_length=255, blank=True, null=True)
    accounts_receivable_sales_price_usd  = models.CharField(db_column='应收账款销售单价（USD）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    accounts_receivable_sales_price_cny  = models.CharField(db_column='应收账款销售单价（人民币）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    accounts_receivable_sales_total_usd  = models.CharField(db_column='应收账款销售总额借（USD）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    accounts_receivable_sales_total_cny  = models.CharField(db_column='应收账款销售总额借（人民币）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    accounts_receivable_debit_usd  = models.CharField(db_column='应收账款销售总额贷（USD）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    accounts_receivable_debit_cny  = models.CharField(db_column='应收账款销售总额贷（人民币）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    accounts_receivable_credit_usd  = models.CharField(db_column='应收账款销售余额（USD）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    accounts_receivable_credit_cny  = models.CharField(db_column='应收账款销售余额（人民币）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    order_amount_usd  = models.CharField(db_column='订单金额（USD）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    order_amount_cny  = models.CharField(db_column='订单金额（人民币）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    payment_received_usd  = models.CharField(db_column='回款金额（USD）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    payment_received_cny  = models.CharField(db_column='回款金额（人民币）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    first_occurrence  = models.CharField(max_length=255, blank=True, null=True)
    customer_type  = models.CharField(max_length=255, blank=True, null=True)
    unreceived_payment_usd  = models.CharField(db_column='未收款（USD）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    unreceived_payment_cny  = models.CharField(db_column='未收款（人民币）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    salesperson  = models.CharField(max_length=255, blank=True, null=True)
    payment_usd  = models.CharField(db_column='收款（USD）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    payment_cny  = models.CharField(db_column='收款（人民币）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    payment_date  = models.CharField(max_length=255, blank=True, null=True)
    invoice_number  = models.CharField(max_length=255, blank=True, null=True)
    invoice_receipt_number  = models.CharField(max_length=255, blank=True, null=True)
    sales_month  = models.CharField(max_length=255, blank=True, null=True)
    international_freight_rmb  = models.CharField(db_column='国际运费（RMB)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    international_freight_usd  = models.CharField(db_column='国际运费（USD)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    miscellaneous_fees  = models.CharField(max_length=255, blank=True, null=True)
    total_amount  = models.CharField(max_length=255, blank=True, null=True)
    logistics_shipping_date  = models.CharField(max_length=255, blank=True, null=True)
    waybill_number  = models.CharField(max_length=255, blank=True, null=True)
    price_below_current_price_list  = models.CharField(db_column='单价低于当期版本价目表\n标“低”标识', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tax_refund_amount  = models.CharField(max_length=255, blank=True, null=True)
    exchange_rate  = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '外贸部台账'



class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    related_formulation = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    progress_status = models.CharField(max_length=255, blank=True, null=True)
    contact_department_lead = models.CharField(max_length=255, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '问题反馈表'


class NewProductDevelopment(models.Model):
    timestamp = models.CharField(max_length=255, blank=True, null=True)
    progress = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    subordinate_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '新品开发进度描述表'


class NewProductDevelopingProgress(models.Model):
    serial_number = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    specific_department = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_source = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    specification_code = models.CharField(max_length=255, blank=True, null=True)
    special_requirements = models.CharField(max_length=255, blank=True, null=True)
    sample_or_sale = models.CharField(db_column='sample/sale', max_length=255, blank=True,
                                      null=True)  # Field renamed to remove unsuitable characters.
    is_duplicate_project = models.CharField(max_length=255, blank=True, null=True)
    initial_quote = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    formulation_name = models.CharField(max_length=255, blank=True, null=True)
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True, null=True)
    excipient_purpose = models.CharField(max_length=255, blank=True, null=True)
    prescription_quantity = models.CharField(max_length=255, blank=True, null=True)
    start_development_date = models.CharField(max_length=255, blank=True, null=True)
    customer_importance = models.CharField(max_length=255, blank=True, null=True)
    excipient_inspection = models.CharField(max_length=255, blank=True, null=True)
    prescription_selection = models.CharField(max_length=255, blank=True, null=True)
    preliminary_process_validation_small_scale = models.CharField(
        db_column='preliminary_process_validation_small_scale', max_length=255, blank=True, null=True)
    pilot_scale_verification = models.CharField(max_length=255, blank=True, null=True)
    process_verification = models.CharField(max_length=255, blank=True, null=True)
    clinical_trials = models.CharField(max_length=255, blank=True, null=True)
    approval_received = models.CharField(max_length=255, blank=True, null=True)
    regular_purchase = models.CharField(max_length=255, blank=True, null=True)
    response_needed = models.CharField(max_length=255, blank=True, null=True)
    in_progress = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    before_pilot_scale = models.CharField(max_length=255, blank=True, null=True)
    before_submission = models.CharField(max_length=255, blank=True, null=True)
    issuance_date = models.CharField(max_length=255, blank=True, null=True)
    landing_company_name = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    transfer_to_sales_manager = models.CharField(max_length=255, blank=True, null=True)
    transfer_date = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
            managed = False
            db_table = '新品开发中进度表'


class NewProductCompleted(models.Model):
    serial_number = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    specific_department = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_source = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    specification_code = models.CharField(max_length=255, blank=True, null=True)
    special_requirements = models.CharField(max_length=255, blank=True, null=True)
    sample_or_sale = models.CharField(db_column='sample/sale', max_length=255, blank=True,
                                      null=True)  # Field renamed to remove unsuitable characters.
    is_duplicate_project = models.CharField(max_length=255, blank=True, null=True)
    initial_quote = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    formulation_name = models.CharField(max_length=255, blank=True, null=True)
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True, null=True)
    excipient_purpose = models.CharField(max_length=255, blank=True, null=True)
    prescription_quantity = models.CharField(max_length=255, blank=True, null=True)
    start_development_date = models.CharField(max_length=255, blank=True, null=True)
    customer_importance = models.CharField(max_length=255, blank=True, null=True)
    excipient_inspection = models.CharField(max_length=255, blank=True, null=True)
    prescription_selection = models.CharField(max_length=255, blank=True, null=True)
    preliminary_process_validation_small_scale = models.CharField(
        db_column='preliminary_process_validation_small_scale', max_length=255, blank=True, null=True)
    pilot_scale_verification = models.CharField(max_length=255, blank=True, null=True)
    process_verification = models.CharField(max_length=255, blank=True, null=True)
    clinical_trials = models.CharField(max_length=255, blank=True, null=True)
    approval_received = models.CharField(max_length=255, blank=True, null=True)
    regular_purchase = models.CharField(max_length=255, blank=True, null=True)
    response_needed = models.CharField(max_length=255, blank=True, null=True)
    in_progress = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    before_pilot_scale = models.CharField(max_length=255, blank=True, null=True)
    before_submission = models.CharField(max_length=255, blank=True, null=True)
    issuance_date = models.CharField(max_length=255, blank=True, null=True)
    landing_company_name = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    transfer_to_sales_manager = models.CharField(max_length=255, blank=True, null=True)
    transfer_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '新品已完成进度表'


class CustomerEngagement(models.Model):
    engagement_number = models.AutoField(primary_key=True)
    recorder = models.CharField(max_length=255, blank=True, null=True)
    proactive_or_passive_engagement = models.CharField(db_column='proactive/passive_engagement', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_category = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_category = models.CharField(max_length=255, blank=True, null=True)
    product_inquiry = models.CharField(max_length=255, blank=True, null=True)
    price_inquiry = models.CharField(max_length=255, blank=True)
    sample_request = models.CharField(max_length=255, blank=True, null=True)
    purchase = models.CharField(max_length=255, blank=True, null=True)
    electronic_material_provision = models.CharField(max_length=255, blank=True, null=True)
    physical_material_preparation = models.CharField(max_length=255, blank=True, null=True)
    sample_tracking = models.CharField(max_length=255, blank=True, null=True)
    product_use_or_question_inquiry = models.CharField(db_column='product_use/question_inquiry', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    product_name = models.CharField(max_length=255, blank=True, null=True)
    specification_code = models.CharField(max_length=255, blank=True, null=True)
    weight = models.CharField(max_length=255, blank=True, null=True)
    dosage_form_or_dosage_category = models.CharField(db_column='dosage_form/dosage_category', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    issue = models.CharField(max_length=255, blank=True, null=True)
    is_resolved = models.CharField(max_length=255, blank=True, null=True)
    resolution_solution = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '研部客户对接表'


class CustomerFlow(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=255)
    sales_department = models.CharField(max_length=255)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_type = models.CharField(max_length=255, blank=True, null=True)
    company_size = models.CharField(max_length=255, blank=True, null=True)
    company_address = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    job_level_assessment = models.CharField(max_length=255, blank=True, null=True)
    sample_or_purchase = models.CharField(db_column='sample/purchase', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    level_of_contact = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    overlapping_contacts = models.CharField(max_length=255, blank=True, null=True)
    contact_method = models.CharField(max_length=255, blank=True, null=True)
    initial_contact_time = models.CharField(max_length=255, blank=True, null=True)
    first_promotional_material = models.CharField(max_length=255, blank=True, null=True)
    summer_gift_2021 = models.CharField(db_column='summer_gift_2021', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    injection_books_2021 = models.CharField(db_column='injection_books_2021', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    year_end_gift_delivery_2021 = models.CharField(db_column='year_end_gift_delivery_2021', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    summer_gift_2022 = models.CharField(db_column='summer_gift_2022', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    books_2022 = models.CharField(db_column='books_2022', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    major_customer_gift_2022 = models.CharField(db_column='major_customer_gift_2022', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    year_end_gift_2022 = models.CharField(db_column='year_end_gift_2022', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    former_employer = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '研部客户流水表'


class CustomerProfile(models.Model):
    customer_id = models.AutoField(primary_key=True)
    sales_department = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    research_capacity = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    legal_representative = models.CharField(max_length=255, blank=True, null=True)
    general_manager = models.CharField(max_length=255, blank=True, null=True)
    license_number = models.CharField(max_length=255, blank=True, null=True)
    gmp_certificate = models.CharField(db_column='GMP_certificate', max_length=255, blank=True,
                                       null=True)  # Field name made lowercase.
    company_type = models.CharField(max_length=255, blank=True, null=True)
    research_scope = models.CharField(max_length=255, blank=True, null=True)
    drug = models.CharField(max_length=255, blank=True, null=True)
    business_scale = models.CharField(max_length=255, blank=True, null=True)
    number_of_employees = models.CharField(max_length=255, blank=True, null=True)
    other_description = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_mobile = models.CharField(max_length=255, blank=True, null=True)
    customer_department = models.CharField(max_length=255, blank=True, null=True)
    customer_job_level_assessment_abc = models.CharField(db_column='customer_job_level_assessment (ABC)',
                                                         max_length=255, blank=True,
                                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_contact_time = models.CharField(max_length=255, blank=True, null=True)
    customer_address = models.CharField(max_length=255, blank=True, null=True)
    sample_time = models.CharField(max_length=255, blank=True, null=True)
    sample_product = models.CharField(max_length=255, blank=True, null=True)
    sample_model = models.CharField(max_length=255, blank=True, null=True)
    sample_quantity_grams = models.CharField(db_column='sample_quantity (grams)', max_length=255, blank=True,
                                             null=True)  # Field renamed to remove unsuitable characters.
    sample_purpose = models.CharField(max_length=255, blank=True, null=True)
    sample_progress = models.CharField(max_length=255, blank=True, null=True)
    sales_time = models.CharField(max_length=255, blank=True, null=True)
    sales_product = models.CharField(max_length=255, blank=True, null=True)
    sales_specification = models.CharField(max_length=255, blank=True, null=True)
    sales_unit_price_cny = models.CharField(db_column='sales_unit_price (CNY)', max_length=255, blank=True,
                                            null=True)  # Field renamed to remove unsuitable characters.
    sales_quantity_kg = models.CharField(db_column='sales_quantity (Kg)', max_length=255, blank=True,
                                         null=True)  # Field renamed to remove unsuitable characters.
    sales_amount = models.CharField(max_length=255, blank=True, null=True)
    sales_purpose = models.CharField(max_length=255, blank=True, null=True)
    sales_progress = models.CharField(max_length=255, blank=True, null=True)
    phone_sales_visit_description = models.TextField(db_column='phone_sales/visit_description', blank=True,
                                                     null=True)  # Field renamed to remove unsuitable characters.
    class Meta:
        managed = False
        db_table = '研发部客户档案表'


class ExistingFormulationToDevelop(models.Model):
    serial_number = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    specific_department = models.CharField(max_length=255, blank=True, null=True)
    leader = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_source = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    corresponding_spec_code = models.CharField(max_length=255, blank=True, null=True)
    special_requirements = models.CharField(max_length=255, blank=True, null=True)
    estimated_annual_consumption = models.CharField(max_length=255, blank=True, null=True)
    current_manufacturer = models.CharField(max_length=255, blank=True, null=True)
    grade_pharmaceutical_grade_chemical_grade = models.CharField(db_column='grade (pharmaceutical grade/chemical grade)', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    model_if_available = models.CharField(db_column='model (if available)', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    price_per_kg = models.CharField(db_column='price per kg', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    sample_sales = models.CharField(db_column='sample/sales', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    repeat_project = models.CharField(max_length=255, blank=True, null=True)
    initial_quotation = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    preparation_name = models.CharField(max_length=255, blank=True, null=True)
    consistency_evaluation_product = models.CharField(max_length=255, blank=True, null=True)
    excipient_use = models.CharField(max_length=255, blank=True, null=True)
    prescription_dosage = models.CharField(max_length=255, blank=True, null=True)
    development_date = models.CharField(max_length=255, blank=True, null=True)
    customer_importance_level = models.CharField(max_length=255, blank=True, null=True)
    preliminary_negotiation = models.CharField(max_length=255, blank=True, null=True)
    supplier_change_application = models.CharField(max_length=255, blank=True, null=True)
    supplier_audit = models.CharField(max_length=255, blank=True, null=True)
    three_batch_excipient_sample_testing = models.CharField(max_length=255, blank=True, null=True)
    first_production_of_three_batches = models.CharField(max_length=255, blank=True, null=True)
    stability_inspection = models.CharField(max_length=255, blank=True, null=True)
    additional_application_record_completed_change = models.CharField(max_length=255, blank=True, null=True)
    formal_contract_signing = models.CharField(max_length=255, blank=True, null=True)
    delivery = models.CharField(max_length=255, blank=True, null=True)
    in_progress = models.CharField(max_length=255, blank=True, null=True)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    before_pilot = models.CharField(max_length=255, blank=True, null=True)
    before_declaration = models.CharField(max_length=255, blank=True, null=True)
    issuance_date = models.CharField(max_length=255, blank=True, null=True)
    landing_company_name = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255, blank=True, null=True)
    transfer_to_sales_manager = models.CharField(max_length=255, blank=True, null=True)
    transfer_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '已有制剂待开发进度表'


class ExistingFormulationProgressDescription(models.Model):
    time = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    subordinate_serial_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '已有制剂进度描述表'


class ExistingFormulationDeveloping(models.Model):
    serial_number = models.AutoField(primary_key=True)
    enterprise_name = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    specific_department = models.CharField(max_length=255, blank=True, null=True)
    responsible_person = models.CharField(max_length=255, blank=True, null=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_source = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    corresponding_specification_code = models.CharField(max_length=255, blank=True, null=True)
    special_requirements = models.CharField(max_length=255, blank=True, null=True)
    estimated_annual_consumption = models.CharField(max_length=255, blank=True, null=True)
    current_manufacturer = models.CharField(max_length=255, blank=True, null=True)
    product_level = models.CharField(db_column='product_level', max_length=255, blank=True, null=True)
    model_number = models.CharField(max_length=255, blank=True, null=True)
    price_per_kg = models.CharField(max_length=255, blank=True, null=True)
    sample_sales = models.CharField(max_length=255, blank=True, null=True)
    is_repeated_project = models.CharField(max_length=255, blank=True, null=True)
    first_quotation = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    formulation_name = models.CharField(max_length=255, blank=True, null=True)
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True, null=True)
    auxiliary_material_usage = models.CharField(max_length=255, blank=True, null=True)
    prescription_dosage = models.CharField(max_length=255, blank=True, null=True)
    development_date = models.CharField(max_length=255, blank=True, null=True)
    customer_importance = models.CharField(max_length=255, blank=True, null=True)
    initial_negotiation = models.CharField(max_length=255, blank=True, null=True)
    supplier_change_request = models.CharField(max_length=255, blank=True, null=True)
    supplier_audit = models.CharField(max_length=255, blank=True, null=True)
    continuous_batch_sample_testing = models.CharField(max_length=255, blank=True, null=True)
    first_production_of_3_batches = models.CharField(max_length=255, blank=True, null=True)
    stability_study = models.CharField(max_length=255, blank=True, null=True)
    additional_application_record_change = models.CharField(max_length=255, blank=True, null=True)
    formal_contract_signing = models.CharField(max_length=255, blank=True, null=True)
    delivery = models.CharField(max_length=255, blank=True, null=True)
    in_progress = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    before_pilot_scale_up = models.CharField(max_length=255, blank=True, null=True)
    before_submission = models.CharField(max_length=255, blank=True, null=True)
    issuing_time = models.CharField(max_length=255, blank=True, null=True)
    landing_enterprise_name = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    handover_sales_manager = models.CharField(max_length=255, blank=True, null=True)
    handover_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '已有制剂开发中进度表'



class (models.Model):
    serial_number  = models.AutoField(primary_key=True)
    enterprise_name  = models.CharField(max_length=255, blank=True, null=True)
    province  = models.CharField(max_length=255, blank=True, null=True)
    city  = models.CharField(max_length=255, blank=True, null=True)
    department  = models.CharField(max_length=255, blank=True, null=True)
    specific_department  = models.CharField(max_length=255, blank=True, null=True)
    responsible_person  = models.CharField(max_length=255, blank=True, null=True)
    customer_name  = models.CharField(max_length=255, blank=True, null=True)
    customer_source  = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True, null=True)
    corresponding_specification_code = models.CharField(max_length=255, blank=True, null=True)
    special_requirements = models.CharField(max_length=255, blank=True, null=True)
    estimated_annual_consumption = models.CharField(max_length=255, blank=True, null=True)
    current_manufacturer = models.CharField(max_length=255, blank=True, null=True)
    product_level = models.CharField(db_column='product_level', max_length=255, blank=True, null=True)
    model_number = models.CharField(max_length=255, blank=True, null=True)
    price_per_kg = models.CharField(max_length=255, blank=True, null=True)
    sample_sales = models.CharField(max_length=255, blank=True, null=True)
    is_repeated_project = models.CharField(max_length=255, blank=True, null=True)
    first_quotation = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.CharField(max_length=255, blank=True, null=True)
    unit_price = models.CharField(max_length=255, blank=True, null=True)
    amount = models.CharField(max_length=255, blank=True, null=True)
    formulation_name = models.CharField(max_length=255, blank=True, null=True)
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True, null=True)
    auxiliary_material_usage = models.CharField(max_length=255, blank=True, null=True)
    prescription_dosage = models.CharField(max_length=255, blank=True, null=True)
    development_date = models.CharField(max_length=255, blank=True, null=True)
    customer_importance = models.CharField(max_length=255, blank=True, null=True)
    initial_negotiation = models.CharField(max_length=255, blank=True, null=True)
    supplier_change_request = models.CharField(max_length=255, blank=True, null=True)
    supplier_audit = models.CharField(max_length=255, blank=True, null=True)
    continuous_batch_sample_testing = models.CharField(max_length=255, blank=True, null=True)
    first_production_of_3_batches = models.CharField(max_length=255, blank=True, null=True)
    stability_study = models.CharField(max_length=255, blank=True, null=True)
    additional_application_record_change = models.CharField(max_length=255, blank=True, null=True)
    formal_contract_signing = models.CharField(max_length=255, blank=True, null=True)
    delivery = models.CharField(max_length=255, blank=True, null=True)
    in_progress = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=255, blank=True, null=True)
    before_pilot_scale_up = models.CharField(max_length=255, blank=True, null=True)
    before_submission = models.CharField(max_length=255, blank=True, null=True)
    issuing_time = models.CharField(max_length=255, blank=True, null=True)
    landing_enterprise_name = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    handover_sales_manager = models.CharField(max_length=255, blank=True, null=True)
    handover_time = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = False
        db_table = '已有制剂已完成进度表'

class Employees(models.Model):
    department = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    work_id = models.CharField(primary_key=True, max_length=255)
    status = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '员工信息表'












































