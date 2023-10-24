from django.db import models


# Create your models here.


class Products(models.Model):
    category = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品类别')
    product_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品名称')
    specification = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格')
    specification_features = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格特点')
    requirements = models.CharField(max_length=255, blank=True, null=True, verbose_name='要求')
    labels = models.CharField(max_length=255, blank=True, null=True, verbose_name='标签')
    spec_code = models.CharField(primary_key=True, max_length=255, verbose_name='规格编码')

    class Meta:
        managed = False
        db_table = '辅料'


class InternalTradeLedger(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    order_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='下单日期')
    sales_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售日期')
    contract_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='合同号')
    contract_returned = models.CharField(max_length=255, blank=True, null=True, verbose_name='合同退回')
    region_department = models.CharField(max_length=255, blank=True, null=True, verbose_name='区域部门')
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name='城市')
    year = models.CharField(max_length=255, blank=True, null=True, verbose_name='年份')
    month = models.CharField(max_length=255, blank=True, null=True, verbose_name='月份')
    industry_category = models.CharField(max_length=255, blank=True, null=True, verbose_name='行业类别')
    product_usage = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品用途')
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司名称')
    product_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品名称')
    model = models.CharField(max_length=255, blank=True, null=True, verbose_name='型号')
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name='编码')
    specification = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格')
    quantity = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')
    unit_price = models.CharField(max_length=255, blank=True, null=True, verbose_name='单价')
    total_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='总金额')
    quantity1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量1')
    unit_price1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='单价1')
    increase_debit = models.CharField(max_length=255, blank=True, null=True, verbose_name='增加借方')
    decrease_credit = models.CharField(max_length=255, blank=True, null=True, verbose_name='减少贷方')
    balance = models.CharField(max_length=255, blank=True, null=True, verbose_name='余额')
    f26 = models.CharField(max_length=255, blank=True, null=True, verbose_name='F26')
    f27 = models.CharField(max_length=255, blank=True, null=True, verbose_name='F27')
    first_occurrence = models.CharField(max_length=255, blank=True, null=True, verbose_name='首次出现')
    new = models.CharField(max_length=255, blank=True, null=True, verbose_name='新')
    second_occurrence = models.CharField(max_length=255, blank=True, null=True, verbose_name='第二次出现')
    unreceived_payment = models.CharField(max_length=255, blank=True, null=True, verbose_name='未收付款')
    payment_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='付款日期')
    old = models.CharField(max_length=255, blank=True, null=True, verbose_name='老')
    salesperson = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售员')
    acceptance_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='验收金额')
    cash = models.CharField(max_length=255, blank=True, null=True, verbose_name='现金')
    date = models.CharField(max_length=255, blank=True, null=True, verbose_name='日期')
    invoice_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='发票号')
    invoice_receipt_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='发票收据号')
    sales_month = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售月份')
    customer_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户类型')
    logistics_shipment_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='物流发货日期')
    waybill_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='运单号')
    unit_price_below_current_price_list = models.CharField(max_length=255, blank=True, null=True,
                                                           verbose_name='单价低于当前价格表')

    class Meta:
        managed = False
        db_table = '内贸部台账'


class Authorization(models.Model):
    authorization_number = models.AutoField(primary_key=True, verbose_name='授权书编号')
    issuance_month = models.CharField(max_length=255, blank=True, null=True, verbose_name='签发月份')
    product_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品名称')
    registration_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='注册号')
    registration_status = models.CharField(max_length=255, blank=True, null=True, verbose_name='注册状态')
    related_manufacturer = models.CharField(max_length=255, blank=True, null=True, verbose_name='相关制造商')
    related_product_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='相关产品名称')
    administration_route = models.CharField(max_length=255, blank=True, null=True, verbose_name='管理途径')
    follow_up_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='跟进人员')
    review_status = models.CharField(max_length=255, blank=True, null=True, verbose_name='审查状态')
    acceptance_month = models.CharField(max_length=255, blank=True, null=True, verbose_name='受理月份')
    during_review_month = models.CharField(max_length=255, blank=True, null=True, verbose_name='审查中月份')
    disappearing_month = models.CharField(max_length=255, blank=True, null=True, verbose_name='消失月份')
    notes = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')

    class Meta:
        managed = False
        db_table = '授权书总表'


class ForeignCustomerProfile(models.Model):
    customer_profile_number = models.AutoField(primary_key=True, verbose_name='客户档案编号')
    salesperson = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售员工')
    classification = models.CharField(max_length=255, blank=True, null=True, verbose_name='分类')
    development_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发日期')
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司名称')
    country = models.CharField(max_length=255, blank=True, null=True, verbose_name='国家')
    media = models.CharField(max_length=255, blank=True, null=True, verbose_name='媒体渠道')
    product_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品名称')
    specification_code = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格编码')
    specification_code_notes = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格编码备注')
    usage = models.CharField(max_length=255, blank=True, null=True, verbose_name='用途')
    follow_up_record = models.CharField(max_length=255, blank=True, null=True, verbose_name='跟进记录')
    company_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司类型')
    company_profile = models.TextField(blank=True, null=True, verbose_name='公司简介')
    customer_contact = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户联系人')
    customer_email = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户邮箱')
    customer_phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户电话')
    customer_website = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户网站')
    preliminary_negotiation = models.CharField(max_length=255, blank=True, null=True, verbose_name='初步洽谈')
    samples = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品')
    questionnaire = models.CharField(max_length=255, blank=True, null=True, verbose_name='问卷')
    deal = models.CharField(max_length=255, blank=True, null=True, verbose_name='交易')
    supplier_audit = models.CharField(max_length=255, blank=True, null=True, verbose_name='供应商审计')
    estimated_annual_usage = models.CharField(max_length=255, blank=True, null=True, verbose_name='年度预估用量')
    current_supplier = models.CharField(max_length=255, blank=True, null=True, verbose_name='现有供应商')
    level = models.CharField(max_length=255, blank=True, null=True, verbose_name='级别')
    model = models.CharField(max_length=255, blank=True, null=True, verbose_name='型号')
    unit_price = models.CharField(max_length=255, blank=True, null=True, verbose_name='单价')
    time = models.CharField(max_length=255, blank=True, null=True, verbose_name='时间')
    progress_description = models.TextField(blank=True, null=True, verbose_name='进展描述')

    class Meta:
        managed = False
        db_table = '外贸部客户档案表'


class ForeignTradeLedger(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序列号')
    order_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='下单日期')
    sales_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售日期')
    contract_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='合同编号')
    customs_declaration = models.CharField(max_length=255, blank=True, null=True, verbose_name='报关')
    other_details = models.CharField(max_length=255, blank=True, null=True, verbose_name='其他细节')
    country_province = models.CharField(max_length=255, blank=True,
                                        null=True,
                                        verbose_name='国家/省份')  # Field renamed to remove unsuitable characters.
    nature = models.CharField(max_length=255, blank=True, null=True, verbose_name='性质')
    development_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发日期')
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司名称')
    product_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品名称')
    model = models.CharField(max_length=255, blank=True, null=True, verbose_name='型号')
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name='编码')
    specification = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格')
    cash_sales_quantity = models.CharField(max_length=255, blank=True, null=True, verbose_name='现款销售数量')
    cash_sales_price_usd = models.CharField(max_length=255, blank=True,
                                            null=True, verbose_name='现款销售单价（USD）')
    cash_sales_price_cny = models.CharField(max_length=255, blank=True,
                                            null=True, verbose_name='现款销售单价（人民币）')
    cash_sales_total_usd = models.CharField(max_length=255, blank=True,
                                            null=True, verbose_name='现款销售总额（USD）')
    cash_sales_total_cny = models.CharField(max_length=255, blank=True,
                                            null=True, verbose_name='现款销售总额（人民币）')
    accounts_receivable_sales_quantity = models.CharField(max_length=255, blank=True, null=True,
                                                          verbose_name='应收账款销售数量')
    accounts_receivable_sales_price_usd = models.CharField(max_length=255,
                                                           blank=True,
                                                           null=True, verbose_name='应收账款销售单价（USD）')
    accounts_receivable_sales_price_cny = models.CharField(max_length=255,
                                                           blank=True,
                                                           null=True, verbose_name='应收账款销售单价（人民币）')
    accounts_receivable_sales_total_usd = models.CharField(max_length=255,
                                                           blank=True,
                                                           null=True, verbose_name='应收账款销售总额借（USD）')
    accounts_receivable_sales_total_cny = models.CharField(max_length=255,
                                                           blank=True,
                                                           null=True, verbose_name='应收账款销售总额借（人民币）')
    accounts_receivable_debit_usd = models.CharField(max_length=255, blank=True,
                                                     null=True, verbose_name='应收账款销售总额贷（USD）')
    accounts_receivable_debit_cny = models.CharField(max_length=255, blank=True,
                                                     null=True, verbose_name='应收账款销售总额贷（人民币）')
    accounts_receivable_credit_usd = models.CharField(max_length=255, blank=True,
                                                      null=True, verbose_name='应收账款销售余额（USD）')
    accounts_receivable_credit_cny = models.CharField(max_length=255, blank=True,
                                                      null=True, verbose_name='应收账款销售余额（人民币）')
    order_amount_usd = models.CharField(max_length=255, blank=True,
                                        null=True, verbose_name='订单金额（USD）')
    order_amount_cny = models.CharField(max_length=255, blank=True,
                                        null=True, verbose_name='订单金额（人民币）')
    payment_received_usd = models.CharField(max_length=255, blank=True,
                                            null=True, verbose_name='回款金额（USD）')
    payment_received_cny = models.CharField(max_length=255, blank=True,
                                            null=True, verbose_name='回款金额（人民币）')
    first_occurrence = models.CharField(max_length=255, blank=True, null=True, verbose_name='首次发生')
    customer_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户类型')
    unreceived_payment_usd = models.CharField(max_length=255, blank=True,
                                              null=True, verbose_name='未收款（USD）')
    unreceived_payment_cny = models.CharField(max_length=255, blank=True,
                                              null=True, verbose_name='未收款（人民币）')
    salesperson = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售员工')
    payment_usd = models.CharField(max_length=255, blank=True,
                                   null=True, verbose_name='收款（USD）')
    payment_cny = models.CharField(max_length=255, blank=True,
                                   null=True, verbose_name='收款（人民币）')
    payment_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='收款日期')
    invoice_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='发票号码')
    invoice_receipt_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='发票收据号')
    sales_month = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售月份')
    international_freight_rmb = models.CharField(max_length=255, blank=True,
                                                 null=True,
                                                 verbose_name='国际运费（RMB)')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    international_freight_usd = models.CharField(max_length=255, blank=True,
                                                 null=True,
                                                 verbose_name='国际运费（USD)')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    miscellaneous_fees = models.CharField(max_length=255, blank=True, null=True, verbose_name='其他费用')
    total_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='总金额')
    logistics_shipping_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='物流发货日期')
    waybill_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='运单号')
    price_below_current_price_list = models.CharField(max_length=255,
                                                      blank=True, null=True,
                                                      verbose_name='单价低于当期版本价目表\n标“低”标识')  # Field renamed to remove unsuitable characters.
    tax_refund_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='退税金额')
    exchange_rate = models.CharField(max_length=255, blank=True, null=True, verbose_name='汇率')

    class Meta:
        managed = False
        db_table = '外贸部台账'


class Feedback(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    timestamp = models.CharField(max_length=255, blank=True, null=True, verbose_name='时间戳')
    department = models.CharField(max_length=255, blank=True, null=True, verbose_name='部门')
    product = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品')
    related_formulation = models.CharField(max_length=255, blank=True, null=True, verbose_name='相关配方')
    message = models.CharField(max_length=255, blank=True, null=True, verbose_name='留言')
    progress_status = models.CharField(max_length=255, blank=True, null=True, verbose_name='进度状态')
    contact_department_lead = models.CharField(max_length=255, blank=True, null=True, verbose_name='联系部门负责人')
    details = models.CharField(max_length=255, blank=True, null=True, verbose_name='详细信息')

    class Meta:
        managed = False
        db_table = '问题反馈表'


class NewProductDevelopment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    timestamp = models.CharField(max_length=255, blank=True, null=True, verbose_name='时间戳')
    progress = models.CharField(max_length=255, blank=True, null=True, verbose_name='进度')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='状态')
    subordinate_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='隶属ID')

    class Meta:
        managed = False
        db_table = '新品开发进度描述表'


class NewProductDevelopingProgress(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序号')
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司名称')
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name='城市')
    department = models.CharField(max_length=255, blank=True, null=True, verbose_name='部门')
    specific_department = models.CharField(max_length=255, blank=True, null=True, verbose_name='具体部门')
    manager = models.CharField(max_length=255, blank=True, null=True, verbose_name='负责人')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户名称')
    customer_source = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户来源')
    product = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品')
    specification_code = models.CharField(max_length=255, blank=True, null=True, verbose_name='对应规格编码')
    special_requirements = models.CharField(max_length=255, blank=True, null=True, verbose_name='特殊需求')
    sample_or_sale = models.CharField(max_length=255, blank=True,
                                      null=True,
                                      verbose_name='申样/销售')  # Field renamed to remove unsuitable characters.
    is_duplicate_project = models.CharField(max_length=255, blank=True, null=True, verbose_name='是否重复项目')
    initial_quote = models.CharField(max_length=255, blank=True, null=True, verbose_name='初次报价')
    quantity = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')
    unit_price = models.CharField(max_length=255, blank=True, null=True, verbose_name='单价')
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='金额')
    formulation_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='制剂名称')
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True, null=True,
                                                         verbose_name='是否一致性评价品种')
    excipient_purpose = models.CharField(max_length=255, blank=True, null=True, verbose_name='辅料用途')
    prescription_quantity = models.CharField(max_length=255, blank=True, null=True, verbose_name='处方用量')
    start_development_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发日期')
    customer_importance = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户重要程度')
    excipient_inspection = models.CharField(max_length=255, blank=True, null=True, verbose_name='前期洽谈')
    prescription_selection = models.CharField(max_length=255, blank=True, null=True, verbose_name='提出供应商变更申请')
    preliminary_process_validation_small_scale = models.CharField(
        db_column='preliminary_process_validation_small_scale', max_length=255, blank=True, null=True,
        verbose_name='供应商审计')
    pilot_scale_verification = models.CharField(max_length=255, blank=True, null=True,
                                                verbose_name='连续3批辅料小样检测')
    process_verification = models.CharField(max_length=255, blank=True, null=True, verbose_name='首次生产3批')
    clinical_trials = models.CharField(max_length=255, blank=True, null=True, verbose_name='稳定性考察')
    approval_received = models.CharField(max_length=255, blank=True, null=True, verbose_name='补充申请备案完成变更')
    regular_purchase = models.CharField(max_length=255, blank=True, null=True, verbose_name='正式合同签订')
    response_needed = models.CharField(max_length=255, blank=True, null=True, verbose_name='发货')
    in_progress = models.CharField(max_length=255, blank=True, null=True, verbose_name='进行中')
    notes = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')
    before_pilot_scale = models.CharField(max_length=255, blank=True, null=True, verbose_name='中试前')
    before_submission = models.CharField(max_length=255, blank=True, null=True, verbose_name='申报前')
    issuance_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='开具时间')
    landing_company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='落地企业名称')
    contact_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='联系人')
    transfer_to_sales_manager = models.CharField(max_length=255, blank=True, null=True,
                                                 verbose_name='移交销售经理')
    transfer_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='移交时间')

    class Meta:
        managed = False
        db_table = '新品开发中进度表'


class NewProductCompleted(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序号')
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司名称')
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name='城市')
    department = models.CharField(max_length=255, blank=True, null=True, verbose_name='部门')
    specific_department = models.CharField(max_length=255, blank=True, null=True, verbose_name='具体部门')
    manager = models.CharField(max_length=255, blank=True, null=True, verbose_name='负责人')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户名称')
    customer_source = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户来源')
    product = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品')
    specification_code = models.CharField(max_length=255, blank=True, null=True, verbose_name='对应规格编码')
    special_requirements = models.CharField(max_length=255, blank=True, null=True, verbose_name='特殊需求')
    sample_or_sale = models.CharField(max_length=255, blank=True,
                                      null=True,
                                      verbose_name='申样/销售')  # Field renamed to remove unsuitable characters.
    is_duplicate_project = models.CharField(max_length=255, blank=True, null=True, verbose_name='是否重复项目')
    initial_quote = models.CharField(max_length=255, blank=True, null=True, verbose_name='初次报价')
    quantity = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')
    unit_price = models.CharField(max_length=255, blank=True, null=True, verbose_name='单价')
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='金额')
    formulation_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='制剂名称')
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True, null=True,
                                                         verbose_name='是否一致性评价品种')
    excipient_purpose = models.CharField(max_length=255, blank=True, null=True, verbose_name='辅料用途')
    prescription_quantity = models.CharField(max_length=255, blank=True, null=True, verbose_name='处方用量')
    start_development_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发日期')
    customer_importance = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户重要程度')
    excipient_inspection = models.CharField(max_length=255, blank=True, null=True, verbose_name='前期洽谈')
    prescription_selection = models.CharField(max_length=255, blank=True, null=True, verbose_name='提出供应商变更申请')
    preliminary_process_validation_small_scale = models.CharField(
        db_column='preliminary_process_validation_small_scale', max_length=255, blank=True, null=True,
        verbose_name='供应商审计')
    pilot_scale_verification = models.CharField(max_length=255, blank=True, null=True,
                                                verbose_name='连续3批辅料小样检测')
    process_verification = models.CharField(max_length=255, blank=True, null=True, verbose_name='首次生产3批')
    clinical_trials = models.CharField(max_length=255, blank=True, null=True, verbose_name='稳定性考察')
    approval_received = models.CharField(max_length=255, blank=True, null=True, verbose_name='补充申请备案完成变更')
    regular_purchase = models.CharField(max_length=255, blank=True, null=True, verbose_name='正式合同签订')
    response_needed = models.CharField(max_length=255, blank=True, null=True, verbose_name='发货')
    in_progress = models.CharField(max_length=255, blank=True, null=True, verbose_name='进行中')
    notes = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')
    before_pilot_scale = models.CharField(max_length=255, blank=True, null=True, verbose_name='中试前')
    before_submission = models.CharField(max_length=255, blank=True, null=True, verbose_name='申报前')
    issuance_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='开具时间')
    landing_company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='落地企业名称')
    contact_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='联系人')
    transfer_to_sales_manager = models.CharField(max_length=255, blank=True, null=True,
                                                 verbose_name='移交销售经理')
    transfer_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='移交时间')

    class Meta:
        managed = False
        db_table = '新品已完成进度表'


class CustomerEngagement(models.Model):
    engagement_number = models.AutoField(primary_key=True, verbose_name='对接编号')
    recorder = models.CharField(max_length=255, blank=True, null=True, verbose_name='记录人')
    proactive_or_passive_engagement = models.CharField(max_length=255,
                                                       blank=True,
                                                       null=True,
                                                       verbose_name='主动/被动对接')  # Field renamed to remove unsuitable characters.
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司名称')
    company_category = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司类别')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户名称')
    customer_category = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户类别')
    product_inquiry = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品咨询')
    price_inquiry = models.CharField(max_length=255, blank=True, verbose_name='价格咨询')
    sample_request = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品请求')
    purchase = models.CharField(max_length=255, blank=True, null=True, verbose_name='采购')
    electronic_material_provision = models.CharField(max_length=255, blank=True, null=True,
                                                     verbose_name='电子资料提供')
    physical_material_preparation = models.CharField(max_length=255, blank=True, null=True,
                                                     verbose_name='物料准备')
    sample_tracking = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品跟踪')
    product_use_or_question_inquiry = models.CharField(max_length=255,
                                                       blank=True,
                                                       null=True,
                                                       verbose_name='产品使用/问题咨询')  # Field renamed to remove unsuitable characters.
    product_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品名称')
    specification_code = models.CharField(max_length=255, blank=True, null=True, verbose_name='规格编码')
    weight = models.CharField(max_length=255, blank=True, null=True, verbose_name='重量')
    dosage_form_or_dosage_category = models.CharField(max_length=255,
                                                      blank=True,
                                                      null=True,
                                                      verbose_name='剂型/剂量类别')  # Field renamed to remove unsuitable characters.
    issue = models.CharField(max_length=255, blank=True, null=True, verbose_name='问题')
    is_resolved = models.CharField(max_length=255, blank=True, null=True, verbose_name='问题是否解决')
    resolution_solution = models.TextField(blank=True, null=True, verbose_name='解决方案')

    class Meta:
        managed = False
        db_table = '研部客户对接表'


class CustomerFlow(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=255, verbose_name='客户编号')
    sales_department = models.CharField(max_length=255, verbose_name='销售部门')
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name='城市')
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司名称')
    company_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司类型')
    company_size = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司规模')
    company_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司地址')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户名称')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='电话')
    tags = models.CharField(max_length=255, blank=True, null=True, verbose_name='标签')
    department = models.CharField(max_length=255, blank=True, null=True, verbose_name='部门')
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name='职位')
    job_level_assessment = models.CharField(max_length=255, blank=True, null=True, verbose_name='职级评估')
    sample_or_purchase = models.CharField(max_length=255, blank=True,
                                          null=True,
                                          verbose_name='样品/购买')  # Field renamed to remove unsuitable characters.
    level_of_contact = models.CharField(max_length=255, blank=True, null=True, verbose_name='联系级别')
    contact_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='联系人')
    overlapping_contacts = models.CharField(max_length=255, blank=True, null=True, verbose_name='重叠联系人')
    contact_method = models.CharField(max_length=255, blank=True, null=True, verbose_name='联系方式')
    initial_contact_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='初次联系时间')
    first_promotional_material = models.CharField(max_length=255, blank=True, null=True, verbose_name='首次宣传资料')
    summer_gift_2021 = models.CharField(max_length=255, blank=True,
                                        null=True,
                                        verbose_name='2021年夏季礼品')  # Field renamed because it wasn't a valid Python identifier.
    injection_books_2021 = models.CharField(max_length=255, blank=True,
                                            null=True,
                                            verbose_name='2021年注射册')  # Field renamed because it wasn't a valid Python identifier.
    year_end_gift_delivery_2021 = models.CharField(max_length=255, blank=True,
                                                   null=True,
                                                   verbose_name='2021年年底礼品交付')  # Field renamed because it wasn't a valid Python identifier.
    summer_gift_2022 = models.CharField(max_length=255, blank=True,
                                        null=True,
                                        verbose_name='2022年夏季礼品')  # Field renamed because it wasn't a valid Python identifier.
    books_2022 = models.CharField(max_length=255, blank=True,
                                  null=True,
                                  verbose_name='2022年图书')  # Field renamed because it wasn't a valid Python identifier.
    major_customer_gift_2022 = models.CharField(max_length=255, blank=True,
                                                null=True,
                                                verbose_name='2022年重要客户礼品')  # Field renamed because it wasn't a valid Python identifier.
    year_end_gift_2022 = models.CharField(max_length=255, blank=True,
                                          null=True,
                                          verbose_name='2022年年底礼品')  # Field renamed because it wasn't a valid Python identifier.
    former_employer = models.CharField(max_length=255, blank=True, null=True, verbose_name='前雇主')

    class Meta:
        managed = False
        db_table = '研部客户流水表'


class CustomerProfile(models.Model):
    customer_id = models.AutoField(primary_key=True, verbose_name='客户编号')
    sales_department = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售部门')
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name='省份')
    research_capacity = models.CharField(max_length=255, blank=True, null=True, verbose_name='研发能力')
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司名称')
    legal_representative = models.CharField(max_length=255, blank=True, null=True, verbose_name='法定代表人')
    general_manager = models.CharField(max_length=255, blank=True, null=True, verbose_name='总经理')
    license_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='许可证号')
    gmp_certificate = models.CharField(db_column='GMP_certificate', max_length=255, blank=True,
                                       null=True, verbose_name='GMP证书')  # Field name made lowercase.
    company_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司类型')
    research_scope = models.CharField(max_length=255, blank=True, null=True, verbose_name='研究范围')
    drug = models.CharField(max_length=255, blank=True, null=True, verbose_name='药品')
    business_scale = models.CharField(max_length=255, blank=True, null=True, verbose_name='经营规模')
    number_of_employees = models.CharField(max_length=255, blank=True, null=True, verbose_name='员工人数')
    other_description = models.CharField(max_length=255, blank=True, null=True, verbose_name='其他描述')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户姓名')
    customer_mobile = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户手机号')
    customer_department = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户部门')
    customer_job_level_assessment_abc = models.CharField(
        max_length=255, blank=True,
        null=True,
        verbose_name='客户职级评估 (ABC)')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_contact_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='初次联系时间')
    customer_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户地址')
    sample_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品时间')
    sample_product = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品产品')
    sample_model = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品型号')
    sample_quantity_grams = models.CharField(max_length=255, blank=True,
                                             null=True,
                                             verbose_name='样品数量 (克)')  # Field renamed to remove unsuitable characters.
    sample_purpose = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品用途')
    sample_progress = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品进展')
    sales_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售时间')
    sales_product = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售产品')
    sales_specification = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售规格')
    sales_unit_price_cny = models.CharField(max_length=255, blank=True,
                                            null=True,
                                            verbose_name='销售单价 (CNY)')  # Field renamed to remove unsuitable characters.
    sales_quantity_kg = models.CharField(max_length=255, blank=True,
                                         null=True,
                                         verbose_name='销售数量 (Kg)')  # Field renamed to remove unsuitable characters.
    sales_amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售金额')
    sales_purpose = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售用途')
    sales_progress = models.CharField(max_length=255, blank=True, null=True, verbose_name='销售进度')
    phone_sales_visit_description = models.TextField(blank=True,
                                                     null=True,
                                                     verbose_name='电话销售/拜访描述')  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = '研发部客户档案表'


class ExistingFormulationToDevelop(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序列号')
    enterprise_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='企业名称')
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name='城市')
    department = models.CharField(max_length=255, blank=True, null=True, verbose_name='部门')
    specific_department = models.CharField(max_length=255, blank=True, null=True, verbose_name='具体部门')
    responsible_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='负责人')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户名称')
    customer_source = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户来源')
    product = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品')
    corresponding_specification_code = models.CharField(max_length=255, blank=True, null=True,
                                                        verbose_name='对应规格代码')
    special_requirements = models.CharField(max_length=255, blank=True, null=True, verbose_name='特殊要求')
    estimated_annual_consumption = models.CharField(max_length=255, blank=True, null=True, verbose_name='预估年消耗量')
    current_manufacturer = models.CharField(max_length=255, blank=True, null=True, verbose_name='当前制造商')
    product_level = models.CharField(db_column='product_level', max_length=255, blank=True, null=True,
                                     verbose_name='产品级别')
    model_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='型号')
    price_per_kg = models.CharField(max_length=255, blank=True, null=True, verbose_name='每公斤价格')
    sample_sales = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品销售')
    is_repeated_project = models.CharField(max_length=255, blank=True, null=True, verbose_name='重复项目')
    first_quotation = models.CharField(max_length=255, blank=True, null=True, verbose_name='首次报价')
    quantity = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')
    unit_price = models.CharField(max_length=255, blank=True, null=True, verbose_name='单价')
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='金额')
    formulation_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='配方名称')
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True, null=True,
                                                         verbose_name='是否一致性评价产品')
    auxiliary_material_usage = models.CharField(max_length=255, blank=True, null=True, verbose_name='辅料用途')
    prescription_dosage = models.CharField(max_length=255, blank=True, null=True, verbose_name='处方剂量')
    development_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发日期')
    customer_importance = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户重要性')
    initial_negotiation = models.CharField(max_length=255, blank=True, null=True, verbose_name='初步洽谈')
    supplier_change_request = models.CharField(max_length=255, blank=True, null=True, verbose_name='供应商变更申请')
    supplier_audit = models.CharField(max_length=255, blank=True, null=True, verbose_name='供应商审计')
    continuous_batch_sample_testing = models.CharField(max_length=255, blank=True, null=True,
                                                       verbose_name='连续批样品测试')
    first_production_of_3_batches = models.CharField(max_length=255, blank=True, null=True, verbose_name='首批三批生产')
    stability_study = models.CharField(max_length=255, blank=True, null=True, verbose_name='稳定性研究')
    additional_application_record_change = models.CharField(max_length=255, blank=True, null=True,
                                                            verbose_name='附加申请记录更改')
    formal_contract_signing = models.CharField(max_length=255, blank=True, null=True, verbose_name='正式合同签订')
    delivery = models.CharField(max_length=255, blank=True, null=True, verbose_name='交付')
    in_progress = models.CharField(max_length=255, blank=True, null=True, verbose_name='进行中')
    notes = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')
    before_pilot_scale_up = models.CharField(max_length=255, blank=True, null=True, verbose_name='试点规模前')
    before_submission = models.CharField(max_length=255, blank=True, null=True, verbose_name='提交前')
    issuing_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='下发时间')
    landing_enterprise_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='着陆企业名称')
    contact_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='联系人')
    handover_sales_manager = models.CharField(max_length=255, blank=True, null=True, verbose_name='交接销售经理')
    handover_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='交接时间')

    class Meta:
        managed = False
        db_table = '已有制剂待开发进度表'


class ExistingFormulationProgressDescription(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    timestamp = models.CharField(max_length=255, blank=True, null=True, verbose_name='时间戳')
    progress = models.CharField(max_length=255, blank=True, null=True, verbose_name='进度')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='状态')
    subordinate_id = models.CharField(max_length=255, blank=True, null=True, verbose_name='隶属ID')

    class Meta:
        managed = False
        db_table = '已有制剂进度描述表'


class ExistingFormulationDeveloping(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序列号')
    enterprise_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='企业名称')
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name='城市')
    department = models.CharField(max_length=255, blank=True, null=True, verbose_name='部门')
    specific_department = models.CharField(max_length=255, blank=True, null=True, verbose_name='具体部门')
    responsible_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='负责人')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户名称')
    customer_source = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户来源')
    product = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品')
    corresponding_specification_code = models.CharField(max_length=255, blank=True, null=True,
                                                        verbose_name='对应规格代码')
    special_requirements = models.CharField(max_length=255, blank=True, null=True, verbose_name='特殊要求')
    estimated_annual_consumption = models.CharField(max_length=255, blank=True, null=True, verbose_name='预估年消耗量')
    current_manufacturer = models.CharField(max_length=255, blank=True, null=True, verbose_name='当前制造商')
    product_level = models.CharField(db_column='product_level', max_length=255, blank=True, null=True,
                                     verbose_name='产品级别')
    model_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='型号')
    price_per_kg = models.CharField(max_length=255, blank=True, null=True, verbose_name='每公斤价格')
    sample_sales = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品销售')
    is_repeated_project = models.CharField(max_length=255, blank=True, null=True, verbose_name='重复项目')
    first_quotation = models.CharField(max_length=255, blank=True, null=True, verbose_name='首次报价')
    quantity = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')
    unit_price = models.CharField(max_length=255, blank=True, null=True, verbose_name='单价')
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='金额')
    formulation_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='配方名称')
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True, null=True,
                                                         verbose_name='是否一致性评价产品')
    auxiliary_material_usage = models.CharField(max_length=255, blank=True, null=True, verbose_name='辅料用途')
    prescription_dosage = models.CharField(max_length=255, blank=True, null=True, verbose_name='处方剂量')
    development_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发日期')
    customer_importance = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户重要性')
    initial_negotiation = models.CharField(max_length=255, blank=True, null=True, verbose_name='初步洽谈')
    supplier_change_request = models.CharField(max_length=255, blank=True, null=True, verbose_name='供应商变更申请')
    supplier_audit = models.CharField(max_length=255, blank=True, null=True, verbose_name='供应商审计')
    continuous_batch_sample_testing = models.CharField(max_length=255, blank=True, null=True,
                                                       verbose_name='连续批样品测试')
    first_production_of_3_batches = models.CharField(max_length=255, blank=True, null=True, verbose_name='首批三批生产')
    stability_study = models.CharField(max_length=255, blank=True, null=True, verbose_name='稳定性研究')
    additional_application_record_change = models.CharField(max_length=255, blank=True, null=True,
                                                            verbose_name='附加申请记录更改')
    formal_contract_signing = models.CharField(max_length=255, blank=True, null=True, verbose_name='正式合同签订')
    delivery = models.CharField(max_length=255, blank=True, null=True, verbose_name='交付')
    in_progress = models.CharField(max_length=255, blank=True, null=True, verbose_name='进行中')
    notes = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')
    before_pilot_scale_up = models.CharField(max_length=255, blank=True, null=True, verbose_name='试点规模前')
    before_submission = models.CharField(max_length=255, blank=True, null=True, verbose_name='提交前')
    issuing_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='下发时间')
    landing_enterprise_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='着陆企业名称')
    contact_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='联系人')
    handover_sales_manager = models.CharField(max_length=255, blank=True, null=True, verbose_name='交接销售经理')
    handover_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='交接时间')

    class Meta:
        managed = False
        db_table = '已有制剂开发中进度表'


class ExistingProductCompleted(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序列号')
    enterprise_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='企业名称')
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name='城市')
    department = models.CharField(max_length=255, blank=True, null=True, verbose_name='部门')
    specific_department = models.CharField(max_length=255, blank=True, null=True, verbose_name='具体部门')
    responsible_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='负责人')
    customer_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户名称')
    customer_source = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户来源')
    product = models.CharField(max_length=255, blank=True, null=True, verbose_name='产品')
    corresponding_specification_code = models.CharField(max_length=255, blank=True, null=True,
                                                        verbose_name='对应规格代码')
    special_requirements = models.CharField(max_length=255, blank=True, null=True, verbose_name='特殊要求')
    estimated_annual_consumption = models.CharField(max_length=255, blank=True, null=True, verbose_name='预估年消耗量')
    current_manufacturer = models.CharField(max_length=255, blank=True, null=True, verbose_name='当前制造商')
    product_level = models.CharField(db_column='product_level', max_length=255, blank=True, null=True,
                                     verbose_name='产品级别')
    model_number = models.CharField(max_length=255, blank=True, null=True, verbose_name='型号')
    price_per_kg = models.CharField(max_length=255, blank=True, null=True, verbose_name='每公斤价格')
    sample_sales = models.CharField(max_length=255, blank=True, null=True, verbose_name='样品销售')
    is_repeated_project = models.CharField(max_length=255, blank=True, null=True, verbose_name='重复项目')
    first_quotation = models.CharField(max_length=255, blank=True, null=True, verbose_name='首次报价')
    quantity = models.CharField(max_length=255, blank=True, null=True, verbose_name='数量')
    unit_price = models.CharField(max_length=255, blank=True, null=True, verbose_name='单价')
    amount = models.CharField(max_length=255, blank=True, null=True, verbose_name='金额')
    formulation_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='配方名称')
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True, null=True,
                                                         verbose_name='是否一致性评价产品')
    auxiliary_material_usage = models.CharField(max_length=255, blank=True, null=True, verbose_name='辅料用途')
    prescription_dosage = models.CharField(max_length=255, blank=True, null=True, verbose_name='处方剂量')
    development_date = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发日期')
    customer_importance = models.CharField(max_length=255, blank=True, null=True, verbose_name='客户重要性')
    initial_negotiation = models.CharField(max_length=255, blank=True, null=True, verbose_name='初步洽谈')
    supplier_change_request = models.CharField(max_length=255, blank=True, null=True, verbose_name='供应商变更申请')
    supplier_audit = models.CharField(max_length=255, blank=True, null=True, verbose_name='供应商审计')
    continuous_batch_sample_testing = models.CharField(max_length=255, blank=True, null=True,
                                                       verbose_name='连续批样品测试')
    first_production_of_3_batches = models.CharField(max_length=255, blank=True, null=True, verbose_name='首批三批生产')
    stability_study = models.CharField(max_length=255, blank=True, null=True, verbose_name='稳定性研究')
    additional_application_record_change = models.CharField(max_length=255, blank=True, null=True,
                                                            verbose_name='附加申请记录更改')
    formal_contract_signing = models.CharField(max_length=255, blank=True, null=True, verbose_name='正式合同签订')
    delivery = models.CharField(max_length=255, blank=True, null=True, verbose_name='交付')
    in_progress = models.CharField(max_length=255, blank=True, null=True, verbose_name='进行中')
    notes = models.CharField(max_length=255, blank=True, null=True, verbose_name='备注')
    before_pilot_scale_up = models.CharField(max_length=255, blank=True, null=True, verbose_name='试点规模前')
    before_submission = models.CharField(max_length=255, blank=True, null=True, verbose_name='提交前')
    issuing_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='下发时间')
    landing_enterprise_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='着陆企业名称')
    contact_person = models.CharField(max_length=255, blank=True, null=True, verbose_name='联系人')
    handover_sales_manager = models.CharField(max_length=255, blank=True, null=True, verbose_name='交接销售经理')
    handover_time = models.CharField(max_length=255, blank=True, null=True, verbose_name='交接时间')

    class Meta:
        managed = False
        db_table = '已有制剂已完成进度表'


class Employees(models.Model):
    department = models.CharField(max_length=255, blank=True, null=True, verbose_name='部门')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='姓名')
    gender = models.CharField(max_length=255, blank=True, null=True, verbose_name='性别')
    position = models.CharField(max_length=255, blank=True, null=True, verbose_name='职位')
    work_id = models.CharField(primary_key=True, max_length=255, verbose_name='工号')
    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='状态')
    password = models.CharField(max_length=255, blank=True, null=True, verbose_name='密码')

    class Meta:
        managed = False
        db_table = '员工信息表'
