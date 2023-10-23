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


class CustomerProfile(models.Model):
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


class (models.Model):
    serial_number = models.AutoField(primary_key=True)
    order_date = models.CharField(max_length=255, blank=True, null=True)
    sales_date = models.CharField(max_length=255, blank=True, null=True)
    contract_number = models.CharField(max_length=255, blank=True, null=True)
    customs_declaration = models.CharField(max_length=255, blank=True, null=True)
    other_details = models.CharField(max_length=255, blank=True, null=True)
    country_province = models.CharField(max_length=255, blank=True, null=True)
    nature = models.CharField(max_length=255, blank=True, null=True)
    development_date = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    model = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    specification = models.CharField(max_length=255, blank=True, null=true)
    cash_sales_quantity = models.CharField(max_length=255, blank=true, null=true)
    cash_sales_price_usd = models.CharField(max_length=255, blank=true, null=true)
    cash_sales_price_cny = models.CharField(max_length=255, blank=true, null=true)
    cash_sales_total_usd = models.CharField(max_length=255, blank=true, null=true)
    cash_sales_total_cny = models.CharField(max_length=255, blank=true, null=true)
    accounts_receivable_sales_quantity = models.CharField(max_length=255, blank=true, null=true)
    accounts_receivable_sales_price_usd = models.CharField(max_length=255, blank=true, null=true)
    accounts_receivable_sales_price_cny = models.CharField(max_length=255, blank=true, null=true)
    accounts_receivable_sales_total_usd = models.CharField(max_length=255, blank=true, null=true)
    accounts_receivable_sales_total_cny = models.CharField(max_length=255, blank=true, null=true)
    accounts_receivable_debit_usd = models.CharField(max_length=255, blank=true, null=true)
    accounts_receivable_debit_cny = models.CharField(max_length=255, blank=true, null=true)
    accounts_receivable_credit_usd = models.CharField(max_length=255, blank=true, null=true)
    accounts_receivable_credit_cny = models.CharField(max_length=255, blank=true, null=true)
    accounts_receivable_balance_usd = models.CharField(max_length=255, blank=true, null=true)
    accounts_receivable_balance_cny = models.CharField(max_length=255, blank=true, null=true)
    order_amount_usd = models.CharField(max_length=255, blank=true, null=true)
    order_amount_cny = models.CharField(max_length=255, blank=true, null=true)
    payment_received_usd = models.CharField(max_length=255, blank=true, null=true)
    payment_received_cny = models.CharField(max_length=255, blank=true, null=true)
    first_occurrence = models.CharField(max_length=255, blank=true, null=true)
    customer_type = models.CharField(max_length=255, blank=true, null=true)
    unreceived_payment_usd = models.CharField(max_length=255, blank=true, null=true)
    unreceived_payment_cny = models.CharField(max_length=255, blank=true, null=true)
    salesperson = models.CharField(max_length=255, blank=true, null=true)
    payment_usd = models.CharField(max_length=255, blank=true, null=true)
    payment_cny = models.CharField(max_length=255, blank=true, null=true)
    payment_date = models.CharField(max_length=255, blank=true, null=true)
    invoice_number = models.CharField(max_length=255, blank=true, null=true)
    invoice_receipt_number = models.CharField(max_length=255, blank=true, null=true)
    sales_month = models.CharField(max_length=255, blank=true, null=true)
    international_freight_rmb = models.CharField(max_length=255, blank=true, null=true)
    international_freight_usd = models.CharField(max_length=255, blank=true, null=true)
    miscellaneous_fees = models.CharField(max_length=255, blank=true, null=true)
    total_amount = models.CharField(max_length=255, blank=true, null=true)
    logistics_shipping_date = models.CharField(max_length=255, blank=true, null=true)
    waybill_number = models.CharField(max_length=255, blank=true, null=true)
    price_below_current_price_list = models.CharField(max_length=255, blank=true, null=true)
    tax_refund_amount = models.CharField(max_length=255, blank=true, null=true)
    exchange_rate = models.CharField(max_length=255, blank=true, null=true)

    class Meta:
        managed = False
        db_table = '外贸部台账'

class (models.Model):
    部门 = models.CharField(max_length=255, blank=True, null=True)
    姓名 = models.CharField(max_length=255, blank=True, null=True)
    性别 = models.CharField(max_length=255, blank=True, null=True)
    职位 = models.CharField(max_length=255, blank=True, null=True)
    工号 = models.CharField(primary_key=True, max_length=255)
    状态 = models.CharField(max_length=255, blank=True, null=True)
    密码 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '员工信息表'








class (models.Model):
    序号 = models.AutoField(primary_key=True)
    企业名称 = models.CharField(max_length=255, blank=True, null=True)
    省份 = models.CharField(max_length=255, blank=True, null=True)
    城市 = models.CharField(max_length=255, blank=True, null=True)
    部门 = models.CharField(max_length=255, blank=True, null=True)
    具体部门 = models.CharField(max_length=255, blank=True, null=True)
    负责人 = models.CharField(max_length=255, blank=True, null=True)
    客户名称 = models.CharField(max_length=255, blank=True, null=True)
    客户来源 = models.CharField(max_length=255, blank=True, null=True)
    产品 = models.CharField(max_length=255, blank=True, null=True)
    对应规格编码 = models.CharField(max_length=255, blank=True, null=True)
    特殊需求 = models.CharField(max_length=255, blank=True, null=True)
    预估年用量 = models.CharField(max_length=255, blank=True, null=True)
    现用厂家 = models.CharField(max_length=255, blank=True, null=True)
    级别_药用级_化工级_field = models.CharField(db_column='级别（药用级/化工级）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    型号_如有_field = models.CharField(db_column='型号\n（如有）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    单价_kg_field = models.CharField(db_column='单价\n（kg）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    申样_销售 = models.CharField(db_column='申样/销售', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    是否重复项目 = models.CharField(max_length=255, blank=True, null=True)
    初次报价 = models.CharField(max_length=255, blank=True, null=True)
    数量 = models.CharField(max_length=255, blank=True, null=True)
    单价 = models.CharField(max_length=255, blank=True, null=True)
    金额 = models.CharField(max_length=255, blank=True, null=True)
    制剂名称 = models.CharField(max_length=255, blank=True, null=True)
    是否一致性评价品种 = models.CharField(max_length=255, blank=True, null=True)
    辅料用途 = models.CharField(max_length=255, blank=True, null=True)
    处方用量 = models.CharField(max_length=255, blank=True, null=True)
    开发日期 = models.CharField(max_length=255, blank=True, null=True)
    客户重要程度 = models.CharField(max_length=255, blank=True, null=True)
    前期洽谈 = models.CharField(max_length=255, blank=True, null=True)
    提出供应商变更申请 = models.CharField(max_length=255, blank=True, null=True)
    供应商审计 = models.CharField(max_length=255, blank=True, null=True)
    连续3批辅料小样检测 = models.CharField(max_length=255, blank=True, null=True)
    首次生产3批 = models.CharField(max_length=255, blank=True, null=True)
    稳定性考察 = models.CharField(max_length=255, blank=True, null=True)
    补充申请备案完成变更 = models.CharField(max_length=255, blank=True, null=True)
    正式合同签订 = models.CharField(max_length=255, blank=True, null=True)
    发货 = models.CharField(max_length=255, blank=True, null=True)
    进行中 = models.CharField(max_length=255, blank=True, null=True)
    备注 = models.CharField(max_length=255, blank=True, null=True)
    中试前 = models.CharField(max_length=255, blank=True, null=True)
    申报前 = models.CharField(max_length=255, blank=True, null=True)
    开具时间 = models.CharField(max_length=255, blank=True, null=True)
    落地企业名称 = models.CharField(max_length=255, blank=True, null=True)
    联系人 = models.CharField(max_length=255, blank=True, null=True)
    移交销售经理 = models.CharField(max_length=255, blank=True, null=True)
    移交时间 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '已有制剂已完成进度表'


class (models.Model):
    序号 = models.AutoField(primary_key=True)
    企业名称 = models.CharField(max_length=255, blank=True, null=True)
    省份 = models.CharField(max_length=255, blank=True, null=True)
    城市 = models.CharField(max_length=255, blank=True, null=True)
    部门 = models.CharField(max_length=255, blank=True, null=True)
    具体部门 = models.CharField(max_length=255, blank=True, null=True)
    负责人 = models.CharField(max_length=255, blank=True, null=True)
    客户名称 = models.CharField(max_length=255, blank=True, null=True)
    客户来源 = models.CharField(max_length=255, blank=True, null=True)
    产品 = models.CharField(max_length=255, blank=True, null=True)
    对应规格编码 = models.CharField(max_length=255, blank=True, null=True)
    特殊需求 = models.CharField(max_length=255, blank=True, null=True)
    预估年用量 = models.CharField(max_length=255, blank=True, null=True)
    现用厂家 = models.CharField(max_length=255, blank=True, null=True)
    级别_药用级_化工级_field = models.CharField(db_column='级别（药用级/化工级）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    型号_如有_field = models.CharField(db_column='型号\n（如有）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    单价_kg_field = models.CharField(db_column='单价\n（kg）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    申样_销售 = models.CharField(db_column='申样/销售', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    是否重复项目 = models.CharField(max_length=255, blank=True, null=True)
    初次报价 = models.CharField(max_length=255, blank=True, null=True)
    数量 = models.CharField(max_length=255, blank=True, null=True)
    单价 = models.CharField(max_length=255, blank=True, null=True)
    金额 = models.CharField(max_length=255, blank=True, null=True)
    制剂名称 = models.CharField(max_length=255, blank=True, null=True)
    是否一致性评价品种 = models.CharField(max_length=255, blank=True, null=True)
    辅料用途 = models.CharField(max_length=255, blank=True, null=True)
    处方用量 = models.CharField(max_length=255, blank=True, null=True)
    开发日期 = models.CharField(max_length=255, blank=True, null=True)
    客户重要程度 = models.CharField(max_length=255, blank=True, null=True)
    前期洽谈 = models.CharField(max_length=255, blank=True, null=True)
    提出供应商变更申请 = models.CharField(max_length=255, blank=True, null=True)
    供应商审计 = models.CharField(max_length=255, blank=True, null=True)
    连续3批辅料小样检测 = models.CharField(max_length=255, blank=True, null=True)
    首次生产3批 = models.CharField(max_length=255, blank=True, null=True)
    稳定性考察 = models.CharField(max_length=255, blank=True, null=True)
    补充申请备案完成变更 = models.CharField(max_length=255, blank=True, null=True)
    正式合同签订 = models.CharField(max_length=255, blank=True, null=True)
    发货 = models.CharField(max_length=255, blank=True, null=True)
    进行中 = models.CharField(max_length=255, blank=True, null=True)
    备注 = models.CharField(max_length=255, blank=True, null=True)
    中试前 = models.CharField(max_length=255, blank=True, null=True)
    申报前 = models.CharField(max_length=255, blank=True, null=True)
    开具时间 = models.CharField(max_length=255, blank=True, null=True)
    落地企业名称 = models.CharField(max_length=255, blank=True, null=True)
    联系人 = models.CharField(max_length=255, blank=True, null=True)
    移交销售经理 = models.CharField(max_length=255, blank=True, null=True)
    移交时间 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '已有制剂开发中进度表'


class (models.Model):
    序号 = models.AutoField(primary_key=True)
    企业名称 = models.CharField(max_length=255, blank=True, null=True)
    省份 = models.CharField(max_length=255, blank=True, null=True)
    城市 = models.CharField(max_length=255, blank=True, null=True)
    部门 = models.CharField(max_length=255, blank=True, null=True)
    具体部门 = models.CharField(max_length=255, blank=True, null=True)
    负责人 = models.CharField(max_length=255, blank=True, null=True)
    客户名称 = models.CharField(max_length=255, blank=True, null=True)
    客户来源 = models.CharField(max_length=255, blank=True, null=True)
    产品 = models.CharField(max_length=255, blank=True, null=True)
    对应规格编码 = models.CharField(max_length=255, blank=True, null=True)
    特殊需求 = models.CharField(max_length=255, blank=True, null=True)
    预估年用量 = models.CharField(max_length=255, blank=True, null=True)
    现用厂家 = models.CharField(max_length=255, blank=True, null=True)
    级别_药用级_化工级_field = models.CharField(db_column='级别（药用级/化工级）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    型号_如有_field = models.CharField(db_column='型号\n（如有）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    单价_kg_field = models.CharField(db_column='单价\n（kg）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    申样_销售 = models.CharField(db_column='申样/销售', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    是否重复项目 = models.CharField(max_length=255, blank=True, null=True)
    初次报价 = models.CharField(max_length=255, blank=True, null=True)
    数量 = models.CharField(max_length=255, blank=True, null=True)
    单价 = models.CharField(max_length=255, blank=True, null=True)
    金额 = models.CharField(max_length=255, blank=True, null=True)
    制剂名称 = models.CharField(max_length=255, blank=True, null=True)
    是否一致性评价品种 = models.CharField(max_length=255, blank=True, null=True)
    辅料用途 = models.CharField(max_length=255, blank=True, null=True)
    处方用量 = models.CharField(max_length=255, blank=True, null=True)
    开发日期 = models.CharField(max_length=255, blank=True, null=True)
    客户重要程度 = models.CharField(max_length=255, blank=True, null=True)
    前期洽谈 = models.CharField(max_length=255, blank=True, null=True)
    提出供应商变更申请 = models.CharField(max_length=255, blank=True, null=True)
    供应商审计 = models.CharField(max_length=255, blank=True, null=True)
    连续3批辅料小样检测 = models.CharField(max_length=255, blank=True, null=True)
    首次生产3批 = models.CharField(max_length=255, blank=True, null=True)
    稳定性考察 = models.CharField(max_length=255, blank=True, null=True)
    补充申请备案完成变更 = models.CharField(max_length=255, blank=True, null=True)
    正式合同签订 = models.CharField(max_length=255, blank=True, null=True)
    发货 = models.CharField(max_length=255, blank=True, null=True)
    进行中 = models.CharField(max_length=255, blank=True, null=True)
    备注 = models.CharField(max_length=255, blank=True, null=True)
    中试前 = models.CharField(max_length=255, blank=True, null=True)
    申报前 = models.CharField(max_length=255, blank=True, null=True)
    开具时间 = models.CharField(max_length=255, blank=True, null=True)
    落地企业名称 = models.CharField(max_length=255, blank=True, null=True)
    联系人 = models.CharField(max_length=255, blank=True, null=True)
    移交销售经理 = models.CharField(max_length=255, blank=True, null=True)
    移交时间 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '已有制剂待开发进度表'


class (models.Model):
    时间 = models.CharField(max_length=255, blank=True, null=True)
    描述 = models.CharField(max_length=255, blank=True, null=True)
    状态 = models.CharField(max_length=255, blank=True, null=True)
    隶属序号 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '已有制剂进度描述表'





class (models.Model):
    序号 = models.AutoField(primary_key=True)
    企业名称 = models.CharField(max_length=255, blank=True, null=True)
    省份 = models.CharField(max_length=255, blank=True, null=True)
    城市 = models.CharField(max_length=255, blank=True, null=True)
    部门 = models.CharField(max_length=255, blank=True, null=True)
    具体部门 = models.CharField(max_length=255, blank=True, null=True)
    负责人 = models.CharField(max_length=255, blank=True, null=True)
    客户名称 = models.CharField(max_length=255, blank=True, null=True)
    客户来源 = models.CharField(max_length=255, blank=True, null=True)
    产品 = models.CharField(max_length=255, blank=True, null=True)
    规格编码 = models.CharField(max_length=255, blank=True, null=True)
    特殊需求 = models.CharField(max_length=255, blank=True, null=True)
    申样_销售 = models.CharField(db_column='申样/销售', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    是否重复项目 = models.CharField(max_length=255, blank=True, null=True)
    初次报价 = models.CharField(max_length=255, blank=True, null=True)
    数量 = models.CharField(max_length=255, blank=True, null=True)
    单价 = models.CharField(max_length=255, blank=True, null=True)
    金额 = models.CharField(max_length=255, blank=True, null=True)
    制剂名称 = models.CharField(max_length=255, blank=True, null=True)
    是否一致性评价品种 = models.CharField(max_length=255, blank=True, null=True)
    辅料用途 = models.CharField(max_length=255, blank=True, null=True)
    处方用量 = models.CharField(max_length=255, blank=True, null=True)
    起始开发日期 = models.CharField(max_length=255, blank=True, null=True)
    客户重要程度 = models.CharField(max_length=255, blank=True, null=True)
    辅料检验 = models.CharField(max_length=255, blank=True, null=True)
    处方筛选 = models.CharField(max_length=255, blank=True, null=True)
    初步验证工艺_小试_field = models.CharField(db_column='初步验证工艺（小试）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    中试验证 = models.CharField(max_length=255, blank=True, null=True)
    工艺验证 = models.CharField(max_length=255, blank=True, null=True)
    临床 = models.CharField(max_length=255, blank=True, null=True)
    拿到批文 = models.CharField(max_length=255, blank=True, null=True)
    正常采购 = models.CharField(max_length=255, blank=True, null=True)
    是否回复 = models.CharField(max_length=255, blank=True, null=True)
    进行中 = models.CharField(max_length=255, blank=True, null=True)
    备注 = models.CharField(max_length=255, blank=True, null=True)
    中试前 = models.CharField(max_length=255, blank=True, null=True)
    申报前 = models.CharField(max_length=255, blank=True, null=True)
    开具时间 = models.CharField(max_length=255, blank=True, null=True)
    落地企业名称 = models.CharField(max_length=255, blank=True, null=True)
    联系人 = models.CharField(max_length=255, blank=True, null=True)
    移交销售经理 = models.CharField(max_length=255, blank=True, null=True)
    移交时间 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '新品已完成进度表'


class (models.Model):
    序号 = models.AutoField(primary_key=True)
    企业名称 = models.CharField(max_length=255, blank=True, null=True)
    省份 = models.CharField(max_length=255, blank=True, null=True)
    城市 = models.CharField(max_length=255, blank=True, null=True)
    部门 = models.CharField(max_length=255, blank=True, null=True)
    具体部门 = models.CharField(max_length=255, blank=True, null=True)
    负责人 = models.CharField(max_length=255, blank=True, null=True)
    客户名称 = models.CharField(max_length=255, blank=True, null=True)
    客户来源 = models.CharField(max_length=255, blank=True, null=True)
    产品 = models.CharField(max_length=255, blank=True, null=True)
    规格编码 = models.CharField(max_length=255, blank=True, null=True)
    特殊需求 = models.CharField(max_length=255, blank=True, null=True)
    申样_销售 = models.CharField(db_column='申样/销售', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    是否重复项目 = models.CharField(max_length=255, blank=True, null=True)
    初次报价 = models.CharField(max_length=255, blank=True, null=True)
    数量 = models.CharField(max_length=255, blank=True, null=True)
    单价 = models.CharField(max_length=255, blank=True, null=True)
    金额 = models.CharField(max_length=255, blank=True, null=True)
    制剂名称 = models.CharField(max_length=255, blank=True, null=True)
    是否一致性评价品种 = models.CharField(max_length=255, blank=True, null=True)
    辅料用途 = models.CharField(max_length=255, blank=True, null=True)
    处方用量 = models.CharField(max_length=255, blank=True, null=True)
    起始开发日期 = models.CharField(max_length=255, blank=True, null=True)
    客户重要程度 = models.CharField(max_length=255, blank=True, null=True)
    辅料检验 = models.CharField(max_length=255, blank=True, null=True)
    处方筛选 = models.CharField(max_length=255, blank=True, null=True)
    初步验证工艺_小试_field = models.CharField(db_column='初步验证工艺（小试）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    中试验证 = models.CharField(max_length=255, blank=True, null=True)
    工艺验证 = models.CharField(max_length=255, blank=True, null=True)
    临床 = models.CharField(max_length=255, blank=True, null=True)
    拿到批文 = models.CharField(max_length=255, blank=True, null=True)
    正常采购 = models.CharField(max_length=255, blank=True, null=True)
    是否回复 = models.CharField(max_length=255, blank=True, null=True)
    进行中 = models.CharField(max_length=255, blank=True, null=True)
    备注 = models.CharField(max_length=255, blank=True, null=True)
    中试前 = models.CharField(max_length=255, blank=True, null=True)
    申报前 = models.CharField(max_length=255, blank=True, null=True)
    开具时间 = models.CharField(max_length=255, blank=True, null=True)
    落地企业名称 = models.CharField(max_length=255, blank=True, null=True)
    联系人 = models.CharField(max_length=255, blank=True, null=True)
    移交销售经理 = models.CharField(max_length=255, blank=True, null=True)
    移交时间 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '新品开发中进度表'


class (models.Model):
    时间 = models.CharField(max_length=255, blank=True, null=True)
    进度 = models.CharField(max_length=255, blank=True, null=True)
    状态 = models.CharField(max_length=255, blank=True, null=True)
    隶属编号 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '新品开发进度描述表'


class (models.Model):
    序号 = models.AutoField(primary_key=True)
    销售部 = models.CharField(max_length=255, blank=True, null=True)
    省份 = models.CharField(max_length=255, blank=True, null=True)
    研发实力 = models.CharField(max_length=255, blank=True, null=True)
    企业名称 = models.CharField(max_length=255, blank=True, null=True)
    法人 = models.CharField(max_length=255, blank=True, null=True)
    总经理 = models.CharField(max_length=255, blank=True, null=True)
    许可证号 = models.CharField(max_length=255, blank=True, null=True)
    ｇｍｐ证书 = models.CharField(db_column='ＧＭＰ证书', max_length=255, blank=True, null=True)  # Field name made lowercase.
    企业性质 = models.CharField(max_length=255, blank=True, null=True)
    研究范围 = models.CharField(max_length=255, blank=True, null=True)
    药品 = models.CharField(max_length=255, blank=True, null=True)
    经营规模 = models.CharField(max_length=255, blank=True, null=True)
    员工人数 = models.CharField(max_length=255, blank=True, null=True)
    其他描述 = models.CharField(max_length=255, blank=True, null=True)
    客户姓名 = models.CharField(max_length=255, blank=True, null=True)
    客户手机 = models.CharField(max_length=255, blank=True, null=True)
    客户部门 = models.CharField(max_length=255, blank=True, null=True)
    客户职级评估_abc_field = models.CharField(db_column='客户职级评估\n（ABC）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    客户初始联系时间 = models.CharField(max_length=255, blank=True, null=True)
    客户地址 = models.CharField(max_length=255, blank=True, null=True)
    赠样时间 = models.CharField(max_length=255, blank=True, null=True)
    赠样产品 = models.CharField(max_length=255, blank=True, null=True)
    赠样型号 = models.CharField(max_length=255, blank=True, null=True)
    赠样数量_ｇ_field = models.CharField(db_column='赠样数量（ｇ）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    样品用途 = models.CharField(max_length=255, blank=True, null=True)
    样品进展 = models.CharField(max_length=255, blank=True, null=True)
    销售时间 = models.CharField(max_length=255, blank=True, null=True)
    销售产品 = models.CharField(max_length=255, blank=True, null=True)
    销售规格 = models.CharField(max_length=255, blank=True, null=True)
    销售单价_元_field = models.CharField(db_column='销售单价（元）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    销售数量_kg_field = models.CharField(db_column='销售数量（Kg）', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    销售金额 = models.CharField(max_length=255, blank=True, null=True)
    销售用途 = models.CharField(max_length=255, blank=True, null=True)
    销售进展 = models.CharField(max_length=255, blank=True, null=True)
    电话销售_拜访记录_情况描述_field = models.TextField(db_column='电话销售＼拜访记录（情况描述）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = '研发部客户档案表'


class (models.Model):
    对接编号 = models.AutoField(primary_key=True)
    记录人 = models.CharField(max_length=255, blank=True, null=True)
    主动_被动对接 = models.CharField(db_column='主动/被动对接', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    企业名称 = models.CharField(max_length=255, blank=True, null=True)
    企业分类 = models.CharField(max_length=255, blank=True, null=True)
    客户姓名 = models.CharField(max_length=255, blank=True, null=True)
    客户分类 = models.CharField(max_length=255, blank=True, null=True)
    产品咨询 = models.CharField(max_length=255, blank=True, null=True)
    价格咨询 = models.CharField(max_length=255, blank=True, null=True)
    申样 = models.CharField(max_length=255, blank=True, null=True)
    采购 = models.CharField(max_length=255, blank=True, null=True)
    电子资料提供 = models.CharField(max_length=255, blank=True, null=True)
    纸质资料准备 = models.CharField(max_length=255, blank=True, null=True)
    申样追踪 = models.CharField(max_length=255, blank=True, null=True)
    使用咨询_问题咨询 = models.CharField(db_column='使用咨询/问题咨询', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    产品名称 = models.CharField(max_length=255, blank=True, null=True)
    规格编码 = models.CharField(max_length=255, blank=True, null=True)
    重量 = models.CharField(max_length=255, blank=True, null=True)
    制剂_制剂大类 = models.CharField(db_column='制剂/制剂大类', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    问题 = models.CharField(max_length=255, blank=True, null=True)
    是否解决 = models.CharField(max_length=255, blank=True, null=True)
    解决方案 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = '研部客户对接表'


class (models.Model):
    研部客户流水号 = models.CharField(primary_key=True, max_length=255)
    销售部 = models.CharField(max_length=255)
    省份 = models.CharField(max_length=255, blank=True, null=True)
    城市 = models.CharField(max_length=255, blank=True, null=True)
    企业名 = models.CharField(max_length=255, blank=True, null=True)
    企业性质 = models.CharField(max_length=255, blank=True, null=True)
    企业规模 = models.CharField(max_length=255, blank=True, null=True)
    公司地址 = models.CharField(max_length=255, blank=True, null=True)
    客户姓名 = models.CharField(max_length=255, blank=True, null=True)
    电话 = models.CharField(max_length=255, blank=True, null=True)
    标签 = models.CharField(max_length=255, blank=True, null=True)
    部门 = models.CharField(max_length=255, blank=True, null=True)
    职位 = models.CharField(max_length=255, blank=True, null=True)
    职级评估 = models.CharField(max_length=255, blank=True, null=True)
    是否申样_采购 = models.CharField(db_column='是否申样/采购', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    联系紧密程度 = models.CharField(max_length=255, blank=True, null=True)
    联系人 = models.CharField(max_length=255, blank=True, null=True)
    是否重叠 = models.CharField(max_length=255, blank=True, null=True)
    联系方式 = models.CharField(max_length=255, blank=True, null=True)
    初始联系时间 = models.CharField(max_length=255, blank=True, null=True)
    首次宣传资料 = models.CharField(max_length=255, blank=True, null=True)
    number_2021夏季风扇礼 = models.CharField(db_column='2021夏季风扇礼', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2021注射剂书籍 = models.CharField(db_column='2021注射剂书籍', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2021年终礼寄送 = models.CharField(db_column='2021年终礼寄送', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2022夏季礼 = models.CharField(db_column='2022夏季礼', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2022书籍 = models.CharField(db_column='2022书籍', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2022大客户礼 = models.CharField(db_column='2022大客户礼', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_2022年终礼 = models.CharField(db_column='2022年终礼', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    曾就职单位 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '研部客户流水表'





class (models.Model):
    序号 = models.AutoField(primary_key=True)
    时间 = models.CharField(max_length=255, blank=True, null=True)
    部门 = models.CharField(max_length=255, blank=True, null=True)
    产品 = models.CharField(max_length=255, blank=True, null=True)
    对应制剂 = models.CharField(max_length=255, blank=True, null=True)
    信息 = models.CharField(max_length=255, blank=True, null=True)
    解决进度_解决状态_field = models.CharField(db_column='解决进度（解决状态）', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    对接部门_负责人 = models.CharField(db_column='对接部门-负责人', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    详情 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '问题反馈表'
