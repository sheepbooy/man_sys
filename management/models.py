from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# 性别可选项
GENDER_CHOICES = [
    ('男', '男'),
    ('女', '女'),
]

# 职位状态可选项
STATUS_CHOICES = [
    ('L', 'L'),
    ('非L', '非L')
]


class Products(models.Model):
    CATEGORY_CHOICES = [
        ('固体', '固体'),
        ('液体', '液体')
    ]
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, blank=True, verbose_name='产品类别')
    product_name = models.CharField(max_length=255, blank=True, verbose_name='产品名称')
    specification = models.CharField(max_length=255, blank=True, verbose_name='规格')
    specification_features = models.CharField(max_length=255, blank=True, verbose_name='规格特点')
    requirements = models.CharField(max_length=255, blank=True, verbose_name='要求')
    labels = models.CharField(max_length=255, blank=True, verbose_name='标签')
    spec_code = models.CharField(primary_key=True, max_length=255, verbose_name='规格编码')

    class Meta:
        # managed = False
        db_table = '辅料'


class InternalTradeLedger(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    order_date = models.DateField(verbose_name='下订单日期')
    sales_date = models.DateField(verbose_name='销售日期')
    contract_number = models.CharField(max_length=255, blank=True, verbose_name='合同编号')
    contract_returned = models.CharField(max_length=255, blank=True, verbose_name='是否回传合同')
    region_department = models.CharField(max_length=255, blank=True, verbose_name='区域/部门')
    province = models.CharField(max_length=255, blank=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, verbose_name='城市')
    year = models.CharField(max_length=255, blank=True, verbose_name='开发年份')
    month = models.CharField(max_length=255, blank=True, verbose_name='开发月份')
    industry_category = models.CharField(max_length=255, blank=True, verbose_name='行业分类')
    product_usage = models.CharField(max_length=255, blank=True, verbose_name='产品使用性质')
    company_name = models.CharField(max_length=255, blank=True, verbose_name='单位名称')
    product_name = models.CharField(max_length=255, blank=True, verbose_name='品名')
    model = models.CharField(max_length=255, blank=True, verbose_name='型号')
    code = models.CharField(max_length=255, blank=True, verbose_name='编码')
    specification = models.CharField(max_length=255, blank=True, verbose_name='规格')
    cash_sales_quantity = models.IntegerField(blank=True, null=True, verbose_name='数量(现款销售)')
    cash_sales_unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                                verbose_name='单价(现款销售)')
    cash_sales_total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                                  verbose_name='总金额(现款销售)')
    receivable_sales_quantity = models.IntegerField(blank=True, null=True, verbose_name='数量(应收账款)')
    receivable_sales_unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                                      verbose_name='单价(应收账款)')
    receivable_sales_increase_debit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                                          verbose_name='增加额(应收账款)')
    receivable_sales_decrease_credit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                                           verbose_name='减少额(应收账款)')
    receivable_sales_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                                   verbose_name='余额(应收账款)')
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='订单金额')
    payback_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True,
                                         verbose_name='回款金额')
    first_occurrence = models.CharField(max_length=255, blank=True, verbose_name='一次')
    customer_type = models.CharField(max_length=255, blank=True, verbose_name="客户类型")
    unreceived_payment = models.CharField(max_length=255, blank=True, verbose_name='未收款')
    payment_date = models.DateField(verbose_name='收款日期')
    salesperson = models.CharField(max_length=255, blank=True, verbose_name='业务员')
    acceptance_amount = models.CharField(max_length=255, blank=True, verbose_name='承兑金额')
    cash = models.CharField(max_length=255, blank=True, verbose_name='现金')
    date = models.DateField(verbose_name='日期')
    invoice_number = models.CharField(max_length=255, blank=True, verbose_name='发票号')
    invoice_receipt_number = models.CharField(max_length=255, blank=True, verbose_name='发票单号')
    sales_month = models.DateField(verbose_name='销售月份')
    customer_category = models.CharField(max_length=255, blank=True, verbose_name='客户性质')
    logistics_shipment_date = models.DateField(verbose_name='物流发运日期')
    waybill_number = models.CharField(max_length=255, blank=True, verbose_name='运单号')
    unit_price_below_current_price_list = models.CharField(max_length=255, blank=True,
                                                           verbose_name='单价低于当期版本价目表')

    class Meta:
        # managed = False
        db_table = '内贸部台账'


class Authorization(models.Model):
    authorization_number = models.AutoField(primary_key=True, verbose_name='授权书编号')
    issuance_month = models.DateField(verbose_name='开具月份')
    product_name = models.CharField(max_length=255, blank=True, verbose_name='品种')
    registration_number = models.CharField(max_length=255, blank=True, verbose_name='登记号')
    registration_status = models.CharField(max_length=255, blank=True, verbose_name='登记号状态')
    related_manufacturer = models.CharField(max_length=255, blank=True, verbose_name='关联制剂厂家')
    related_product_name = models.CharField(max_length=255, blank=True, verbose_name='关联制剂名称')
    administration_route = models.CharField(max_length=255, blank=True,
                                            verbose_name='给药途径')
    follow_up_person = models.CharField(max_length=255, blank=True, verbose_name='跟进人')
    review_status = models.CharField(max_length=255, blank=True, verbose_name='受审情况')
    acceptance_month = models.DateField(verbose_name='受理月份')
    during_review_month = models.DateField(verbose_name='在审月份')
    disappearing_month = models.DateField(verbose_name='在审消失月份')
    notes = models.CharField(max_length=255, blank=True, verbose_name='备注')

    class Meta:
        # managed = False
        db_table = '授权书总表'


class ForeignCustomerProfile(models.Model):
    customer_profile_number = models.AutoField(primary_key=True, verbose_name='客户档案编号')
    salesperson = models.CharField(max_length=255, blank=True, verbose_name='业务员')
    classification = models.CharField(max_length=255, blank=True, verbose_name='分级')
    development_date = models.DateField(verbose_name='开发日期')
    company_name = models.CharField(max_length=255, blank=True, verbose_name='公司名称')
    country = models.CharField(max_length=255, blank=True, verbose_name='国家')
    media = models.CharField(max_length=255, blank=True, verbose_name='媒介')
    product_name = models.CharField(max_length=255, blank=True, verbose_name='产品名称')
    specification_code = models.CharField(max_length=255, blank=True, verbose_name='规格编码')
    specification_code_notes = models.CharField(max_length=255, blank=True, verbose_name='规格编码备注')
    usage = models.CharField(max_length=255, blank=True, verbose_name='用途')
    follow_up_record = models.CharField(max_length=255, blank=True, verbose_name='跟进记录')
    company_type = models.CharField(max_length=255, blank=True, verbose_name='公司性质')
    company_profile = models.TextField(blank=True, verbose_name='公司简介')
    customer_contact = models.CharField(max_length=255, blank=True, verbose_name='客户联系人')
    customer_email = models.CharField(max_length=255, blank=True, verbose_name='客户邮箱')
    customer_phone = models.CharField(max_length=255, blank=True, verbose_name='客户电话')
    customer_website = models.CharField(max_length=255, blank=True, verbose_name='客户网站')
    preliminary_negotiation = models.DateField(verbose_name='前期洽谈(开发进度)')
    samples = models.DateField(verbose_name='样品(开发进度)')
    questionnaire = models.DateField(verbose_name='问卷(开发进度)')
    deal = models.DateField(verbose_name='成交(开发进度)')
    supplier_audit = models.DateField(verbose_name='供应商审计(开发进度)')
    estimated_annual_usage = models.DateField(verbose_name='预估年用量(现有供应商情况描述)')
    current_supplier = models.CharField(max_length=255, blank=True, verbose_name='现用厂家(现有供应商情况描述)')
    level = models.CharField(max_length=255, blank=True, verbose_name='级别(现有供应商情况描述(药用级/化工级))')
    model = models.CharField(max_length=255, blank=True, verbose_name='型号(现有供应商情况描述)')
    unit_price = models.CharField(max_length=255, blank=True, verbose_name='单价kg(现有供应商情况描述)')
    time = models.DateField(verbose_name='时间')
    progress_description = models.TextField(blank=True, verbose_name='进展描述')

    class Meta:
        # managed = False
        db_table = '外贸部客户档案表'


class ForeignTradeLedger(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序号')
    order_date = models.DateField(verbose_name='下订单日期')
    sales_date = models.DateField(verbose_name='销售日期')
    contract_number = models.CharField(max_length=255, blank=True, verbose_name='合同编号')
    customs_declaration = models.CharField(max_length=255, blank=True, verbose_name='是否报关')
    other_details = models.CharField(max_length=255, blank=True, verbose_name='其他')
    country_province = models.CharField(max_length=255, blank=True,

                                        verbose_name='国家/省份')  # Field renamed to remove unsuitable characters.
    nature = models.CharField(max_length=255, blank=True, verbose_name='性质')
    development_date = models.CharField(max_length=255, blank=True, verbose_name='开发日期')
    company_name = models.CharField(max_length=255, blank=True, verbose_name='单位名称')
    product_name = models.CharField(max_length=255, blank=True, verbose_name='品名')
    model = models.CharField(max_length=255, blank=True, verbose_name='型号')
    code = models.CharField(max_length=255, blank=True, verbose_name='编码')
    specification = models.CharField(max_length=255, blank=True, verbose_name='规格')
    cash_sales_quantity = models.CharField(max_length=255, blank=True, verbose_name='数量(现款销售)')
    cash_sales_price_usd = models.CharField(max_length=255, blank=True,
                                            verbose_name='单价(USD)(现款销售)')
    cash_sales_price_cny = models.CharField(max_length=255, blank=True,
                                            verbose_name='单价(CNY)(现款销售)')
    cash_sales_total_usd = models.CharField(max_length=255, blank=True,
                                            verbose_name='总额(USD)(现款销售)')
    cash_sales_total_cny = models.CharField(max_length=255, blank=True,
                                            verbose_name='总额(CNY)(现款销售)')
    accounts_receivable_sales_quantity = models.CharField(max_length=255, blank=True,
                                                          verbose_name='数量(应收账款销售)')
    accounts_receivable_sales_price_usd = models.CharField(max_length=255,
                                                           blank=True,
                                                           verbose_name='单价(USD)(应收账款销售)')
    accounts_receivable_sales_price_cny = models.CharField(max_length=255,
                                                           blank=True,
                                                           verbose_name='单价(CNY)(应收账款销售)')
    accounts_receivable_sales_total_usd = models.CharField(max_length=255,
                                                           blank=True,
                                                           verbose_name='总额借(USD)(应收账款销售)')
    accounts_receivable_sales_total_cny = models.CharField(max_length=255,
                                                           blank=True,
                                                           verbose_name='总额借(人民币)(应收账款销售)')
    accounts_receivable_debit_usd = models.CharField(max_length=255, blank=True,
                                                     verbose_name='总额贷(USD)(应收账款销售)')
    accounts_receivable_debit_cny = models.CharField(max_length=255, blank=True,
                                                     verbose_name='总额贷(CNY)(应收账款销售)')
    accounts_receivable_credit_usd = models.CharField(max_length=255, blank=True,
                                                      verbose_name='余额(USD)(应收账款销售)')
    accounts_receivable_credit_cny = models.CharField(max_length=255, blank=True,
                                                      verbose_name='余额(CNY)(应收账款销售)')
    order_amount_usd = models.CharField(max_length=255, blank=True,
                                        verbose_name='订单金额(USD)')
    order_amount_cny = models.CharField(max_length=255, blank=True,
                                        verbose_name='订单金额(CNY)')
    payment_received_usd = models.CharField(max_length=255, blank=True,
                                            verbose_name='回款金额(USD)')
    payment_received_cny = models.CharField(max_length=255, blank=True,
                                            verbose_name='回款金额(CNY)')
    first_occurrence = models.CharField(max_length=255, blank=True, verbose_name='一次')
    customer_type = models.CharField(max_length=255, blank=True, verbose_name='客户类型')
    unreceived_payment_usd = models.CharField(max_length=255, blank=True,
                                              verbose_name='未收款(USD)')
    unreceived_payment_cny = models.CharField(max_length=255, blank=True,
                                              verbose_name='未收款(CNY)')
    salesperson = models.CharField(max_length=255, blank=True, verbose_name='业务员')
    payment_usd = models.CharField(max_length=255, blank=True,
                                   verbose_name='收款(USD)')
    payment_cny = models.CharField(max_length=255, blank=True,
                                   verbose_name='收款(CNY)')
    payment_date = models.DateField(verbose_name='收款日期')
    invoice_number = models.CharField(max_length=255, blank=True, verbose_name='发票号')
    invoice_receipt_number = models.CharField(max_length=255, blank=True, verbose_name='发票单号')
    sales_month = models.DateField(verbose_name='销售月份')
    international_freight_rmb = models.CharField(max_length=255, blank=True,

                                                 verbose_name='国际运费(RMB)')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    international_freight_usd = models.CharField(max_length=255, blank=True,

                                                 verbose_name='国际运费(USD)')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    miscellaneous_fees = models.CharField(max_length=255, blank=True, verbose_name='港杂费')
    total_amount = models.CharField(max_length=255, blank=True, verbose_name='合计')
    logistics_shipping_date = models.DateField(verbose_name='物流发运时间')
    waybill_number = models.CharField(max_length=255, blank=True, verbose_name='运单号')
    price_below_current_price_list = models.CharField(max_length=255,
                                                      blank=True,
                                                      verbose_name='单价低于当期版本价目表\n标“低”标识')  # Field renamed to remove unsuitable characters.
    tax_refund_amount = models.CharField(max_length=255, blank=True, verbose_name='退税额')
    exchange_rate = models.CharField(max_length=255, blank=True, verbose_name='汇率')

    class Meta:
        # managed = False
        db_table = '外贸部台账'


class Feedback(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    timestamp = models.DateField(verbose_name='日期')
    department = models.CharField(max_length=255, blank=True, verbose_name='部门')
    product = models.CharField(max_length=255, blank=True, verbose_name='产品')
    related_formulation = models.CharField(max_length=255, blank=True, verbose_name='对应制剂')
    message = models.CharField(max_length=255, blank=True, verbose_name='信息')
    progress_status = models.CharField(max_length=255, blank=True, verbose_name='解决进度(解决状态)')
    contact_department_lead = models.CharField(max_length=255, blank=True, verbose_name='对接部门-负责人')
    details = models.CharField(max_length=255, blank=True, verbose_name='详情')

    class Meta:
        # managed = False
        db_table = '问题反馈表'


class NewProductDevelopment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    timestamp = models.DateField(verbose_name='时间戳')
    progress = models.CharField(max_length=255, blank=True, verbose_name='进度')
    status = models.CharField(max_length=255, blank=True, verbose_name='状态')
    subordinate_id = models.CharField(max_length=255, blank=True, verbose_name='隶属ID')

    class Meta:
        # managed = False
        db_table = '新品开发进度描述表'


class NewProductDevelopingProgress(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序号')
    company_name = models.CharField(max_length=255, blank=True, verbose_name='企业名称')
    province = models.CharField(max_length=255, blank=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, verbose_name='城市')
    department = models.CharField(max_length=255, blank=True, verbose_name='部门')
    specific_department = models.CharField(max_length=255, blank=True, verbose_name='具体部门')
    manager = models.CharField(max_length=255, blank=True, verbose_name='负责人')
    customer_name = models.CharField(max_length=255, blank=True, verbose_name='客户名称')
    customer_source = models.CharField(max_length=255, blank=True, verbose_name='客户来源')
    product = models.CharField(max_length=255, blank=True, verbose_name='产品')
    specification_code = models.CharField(max_length=255, blank=True, verbose_name='规格编码')
    special_requirements = models.CharField(max_length=255, blank=True, verbose_name='特殊需求')
    sample_or_sale = models.CharField(max_length=255, blank=True,
                                      verbose_name='申样/销售')  # Field renamed to remove unsuitable characters.
    is_duplicate_project = models.CharField(max_length=255, blank=True, verbose_name='是否重复项目')
    initial_quote = models.CharField(max_length=255, blank=True, verbose_name='初次报价')
    quantity = models.CharField(max_length=255, blank=True, verbose_name='数量')
    unit_price = models.CharField(max_length=255, blank=True, verbose_name='单价')
    amount = models.CharField(max_length=255, blank=True, verbose_name='金额')
    formulation_name = models.CharField(max_length=255, blank=True, verbose_name='制剂名称')
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True,
                                                         verbose_name='是否一致性评价品种')
    excipient_purpose = models.CharField(max_length=255, blank=True, verbose_name='辅料用途')
    prescription_quantity = models.CharField(max_length=255, blank=True, verbose_name='处方用量')
    start_development_date = models.DateField(verbose_name='起始开发日期')
    customer_importance = models.CharField(max_length=255, blank=True, verbose_name='客户重要程度')
    excipient_inspection = models.DateField(verbose_name='辅料检验')
    prescription_selection = models.DateField(verbose_name='处方筛选')
    preliminary_process_validation_small_scale = models.DateField(
        db_column='preliminary_process_validation_small_scale',
        verbose_name='初步验证工艺（小试）')
    pilot_scale_verification = models.DateField(verbose_name='中试验证')
    process_verification = models.DateField(verbose_name='工艺验证')
    clinical_trials = models.DateField(verbose_name='临床')
    approval_received = models.DateField(verbose_name='拿到批文')
    regular_purchase = models.DateField(verbose_name='正常采购')
    response_needed = models.DateField(verbose_name='是否回复')
    in_progress = models.DateField(verbose_name='进行中')
    notes = models.CharField(max_length=255, blank=True, verbose_name='备注')
    before_pilot_scale = models.DateField(verbose_name='中试前')
    before_submission = models.DateField(verbose_name='申报前')
    issuance_date = models.DateField(verbose_name='开具时间')
    landing_company_name = models.CharField(max_length=255, blank=True, verbose_name='落地企业名称')
    contact_person = models.CharField(max_length=255, blank=True, verbose_name='联系人')
    transfer_to_sales_manager = models.DateField(verbose_name='移交销售经理')
    transfer_date = models.DateField(verbose_name='移交时间')

    class Meta:
        # managed = False
        db_table = '新品开发中进度表'


class NewProductCompleted(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序号')
    company_name = models.CharField(max_length=255, blank=True, verbose_name='企业名称')
    province = models.CharField(max_length=255, blank=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, verbose_name='城市')
    department = models.CharField(max_length=255, blank=True, verbose_name='部门')
    specific_department = models.CharField(max_length=255, blank=True, verbose_name='具体部门')
    manager = models.CharField(max_length=255, blank=True, verbose_name='负责人')
    customer_name = models.CharField(max_length=255, blank=True, verbose_name='客户名称')
    customer_source = models.CharField(max_length=255, blank=True, verbose_name='客户来源')
    product = models.CharField(max_length=255, blank=True, verbose_name='产品')
    specification_code = models.CharField(max_length=255, blank=True, verbose_name='规格编码')
    special_requirements = models.CharField(max_length=255, blank=True, verbose_name='特殊需求')
    sample_or_sale = models.CharField(max_length=255, blank=True,
                                      verbose_name='申样/销售')  # Field renamed to remove unsuitable characters.
    is_duplicate_project = models.CharField(max_length=255, blank=True, verbose_name='是否重复项目')
    initial_quote = models.CharField(max_length=255, blank=True, verbose_name='初次报价')
    quantity = models.CharField(max_length=255, blank=True, verbose_name='数量')
    unit_price = models.CharField(max_length=255, blank=True, verbose_name='单价')
    amount = models.CharField(max_length=255, blank=True, verbose_name='金额')
    formulation_name = models.CharField(max_length=255, blank=True, verbose_name='制剂名称')
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True,
                                                         verbose_name='是否一致性评价品种')
    excipient_purpose = models.CharField(max_length=255, blank=True, verbose_name='辅料用途')
    prescription_quantity = models.CharField(max_length=255, blank=True, verbose_name='处方用量')
    start_development_date = models.DateField(verbose_name='起始开发日期')
    customer_importance = models.CharField(max_length=255, blank=True, verbose_name='客户重要程度')
    excipient_inspection = models.DateField(verbose_name='辅料检验')
    prescription_selection = models.DateField(verbose_name='处方筛选')
    preliminary_process_validation_small_scale = models.DateField(
        db_column='preliminary_process_validation_small_scale',
        verbose_name='初步验证工艺（小试）')
    pilot_scale_verification = models.DateField(verbose_name='中试验证')
    process_verification = models.DateField(verbose_name='工艺验证')
    clinical_trials = models.DateField(verbose_name='临床')
    approval_received = models.DateField(verbose_name='拿到批文')
    regular_purchase = models.DateField(verbose_name='正常采购')
    response_needed = models.DateField(verbose_name='是否回复')
    in_progress = models.DateField(verbose_name='进行中')
    notes = models.CharField(max_length=255, blank=True, verbose_name='备注')
    before_pilot_scale = models.DateField(verbose_name='中试前')
    before_submission = models.DateField(verbose_name='申报前')
    issuance_date = models.DateField(verbose_name='开具时间')
    landing_company_name = models.CharField(max_length=255, blank=True, verbose_name='落地企业名称')
    contact_person = models.CharField(max_length=255, blank=True, verbose_name='联系人')
    transfer_to_sales_manager = models.DateField(verbose_name='移交销售经理')
    transfer_date = models.DateField(verbose_name='移交时间')

    class Meta:
        # managed = False
        db_table = '新品已完成进度表'


class CustomerEngagement(models.Model):
    ENGAGEMENT_CHOICES = [
        ('主动对接', '主动对接'),
        ('被动对接', '被动对接')
    ]
    ISORNOT_CHOICES = [
        ('1', '是'),
        ('0', '否')
    ]
    engagement_number = models.AutoField(primary_key=True, verbose_name='对接编号')
    recorder = models.CharField(max_length=255, blank=True, verbose_name='记录人')
    proactive_or_passive_engagement = models.CharField(max_length=255,
                                                       blank=True,
                                                       choices=ENGAGEMENT_CHOICES,
                                                       verbose_name='主动/被动对接')  # Field renamed to remove unsuitable characters.
    company_name = models.CharField(max_length=255, blank=True, verbose_name='企业名称')
    company_category = models.CharField(max_length=255, blank=True, verbose_name='企业分类')
    customer_name = models.CharField(max_length=255, blank=True, verbose_name='客户姓名')
    customer_category = models.CharField(max_length=255, blank=True, verbose_name='客户分类')
    product_inquiry = models.CharField(max_length=255, choices=ISORNOT_CHOICES, blank=True, verbose_name='产品咨询')
    price_inquiry = models.CharField(max_length=255, choices=ISORNOT_CHOICES, blank=True, verbose_name='价格咨询')
    sample_request = models.CharField(max_length=255, blank=True, choices=ISORNOT_CHOICES, verbose_name='申样')
    purchase = models.CharField(max_length=255, blank=True, choices=ISORNOT_CHOICES, verbose_name='采购')
    electronic_material_provision = models.CharField(max_length=255, blank=True, choices=ISORNOT_CHOICES,
                                                     verbose_name='电子资料提供')
    physical_material_preparation = models.CharField(max_length=255, blank=True, choices=ISORNOT_CHOICES,
                                                     verbose_name='纸质资料准备')
    sample_tracking = models.CharField(max_length=255, choices=ISORNOT_CHOICES, blank=True, verbose_name='申样追踪')
    product_use_or_question_inquiry = models.CharField(max_length=255,
                                                       blank=True,
                                                       choices=ISORNOT_CHOICES,
                                                       verbose_name='使用咨询/问题咨询')  # Field renamed to remove unsuitable characters.
    product_name = models.CharField(max_length=255, blank=True, verbose_name='产品名称')
    specification_code = models.CharField(max_length=255, blank=True, verbose_name='规格编码')
    weight = models.CharField(max_length=255, blank=True, verbose_name='重量')
    dosage_form_or_dosage_category = models.CharField(max_length=255,
                                                      blank=True,
                                                      verbose_name='制剂/制剂大类')  # Field renamed to remove unsuitable characters.
    issue = models.CharField(max_length=255, blank=True, verbose_name='问题')
    is_resolved = models.CharField(max_length=255, blank=True, verbose_name='是否解决')
    resolution_solution = models.TextField(blank=True, verbose_name='解决方案')

    class Meta:
        # managed = False
        db_table = '研部客户对接表'


class CustomerFlow(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=255, verbose_name='客户编号')
    sales_department = models.CharField(max_length=255, verbose_name='销售部')
    province = models.CharField(max_length=255, blank=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, verbose_name='城市')
    company_name = models.CharField(max_length=255, blank=True, verbose_name='企业名')
    company_type = models.CharField(max_length=255, blank=True, verbose_name='企业性质')
    company_size = models.CharField(max_length=255, blank=True, verbose_name='企业规模')
    company_address = models.CharField(max_length=255, blank=True, verbose_name='公司地址')
    customer_name = models.CharField(max_length=255, blank=True, verbose_name='客户姓名')
    phone = models.CharField(max_length=255, blank=True, verbose_name='电话')
    tags = models.CharField(max_length=255, blank=True, verbose_name='标签(研发/采购)')
    department = models.CharField(max_length=255, blank=True, verbose_name='部门')
    position = models.CharField(max_length=255, blank=True, verbose_name='职位')
    job_level_assessment = models.CharField(max_length=255, blank=True, verbose_name='职级评估(A/B/C)')
    sample_or_purchase = models.CharField(max_length=255, blank=True,
                                          verbose_name='是否申样/采购(历史)')  # Field renamed to remove unsuitable characters.
    level_of_contact = models.CharField(max_length=255, blank=True, verbose_name='联系紧密程度(123)')
    contact_person = models.CharField(max_length=255, blank=True, verbose_name='联系人')
    overlapping_contacts = models.CharField(max_length=255, blank=True, verbose_name='是否重叠')
    contact_method = models.CharField(max_length=255, blank=True, verbose_name='联系方式')
    initial_contact_time = models.DateField(verbose_name='初始联系时间')
    first_promotional_material = models.CharField(max_length=255, blank=True, verbose_name='首次宣传资料')
    summer_gift_2021 = models.CharField(max_length=255, blank=True,
                                        verbose_name='2021夏季风扇礼')  # Field renamed because it wasn't a valid Python identifier.
    injection_books_2021 = models.CharField(max_length=255, blank=True,
                                            verbose_name='2021注射剂书籍')  # Field renamed because it wasn't a valid Python identifier.
    year_end_gift_delivery_2021 = models.CharField(max_length=255, blank=True,
                                                   verbose_name='2021年终礼寄送')  # Field renamed because it wasn't a valid Python identifier.
    summer_gift_2022 = models.CharField(max_length=255, blank=True,
                                        verbose_name='2022夏季礼')  # Field renamed because it wasn't a valid Python identifier.
    books_2022 = models.CharField(max_length=255, blank=True,
                                  verbose_name='2022书籍')  # Field renamed because it wasn't a valid Python identifier.
    major_customer_gift_2022 = models.CharField(max_length=255, blank=True,
                                                verbose_name='2022大客户礼')  # Field renamed because it wasn't a valid Python identifier.
    year_end_gift_2022 = models.CharField(max_length=255, blank=True,
                                          verbose_name='2022年终礼')  # Field renamed because it wasn't a valid Python identifier.
    former_employer = models.CharField(max_length=255, blank=True, verbose_name='曾就职单位')

    class Meta:
        # managed = False
        db_table = '研部客户流水表'


class CustomerProfile(models.Model):
    customer_id = models.AutoField(primary_key=True, verbose_name='客户编号')
    sales_department = models.CharField(max_length=255, blank=True, verbose_name='销售部')
    province = models.CharField(max_length=255, blank=True, verbose_name='省份')
    research_capacity = models.CharField(max_length=255, blank=True, verbose_name='研发实力')
    company_name = models.CharField(max_length=255, blank=True, verbose_name='企业名称')
    legal_representative = models.CharField(max_length=255, blank=True, verbose_name='法人')
    general_manager = models.CharField(max_length=255, blank=True, verbose_name='总经理')
    license_number = models.CharField(max_length=255, blank=True, verbose_name='许可证号')
    gmp_certificate = models.CharField(db_column='GMP_certificate', max_length=255, blank=True,
                                       verbose_name='GMP证书')  # Field name made lowercase.
    company_type = models.CharField(max_length=255, blank=True, verbose_name='企业性质')
    research_scope = models.CharField(max_length=255, blank=True, verbose_name='研究范围')
    business_scale = models.CharField(max_length=255, blank=True, verbose_name='经营规模')
    number_of_employees = models.CharField(max_length=255, blank=True, verbose_name='员工人数')
    other_description = models.CharField(max_length=255, blank=True, verbose_name='其他描述')
    customer_name = models.CharField(max_length=255, blank=True, verbose_name='客户姓名')
    customer_mobile = models.CharField(max_length=255, blank=True, verbose_name='客户手机号')
    customer_department = models.CharField(max_length=255, blank=True, verbose_name='客户部门')
    customer_job_level_assessment_abc = models.CharField(
        max_length=255, blank=True,
        verbose_name='客户职级评估 (ABC)')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    initial_contact_time = models.DateField(verbose_name='初次联系时间')
    customer_address = models.CharField(max_length=255, blank=True, verbose_name='客户地址')
    sample_time = models.CharField(max_length=255, blank=True, verbose_name='赠样时间')
    sample_product = models.CharField(max_length=255, blank=True, verbose_name='赠样产品')
    sample_model = models.CharField(max_length=255, blank=True, verbose_name='赠样型号')
    sample_quantity_grams = models.CharField(max_length=255, blank=True,
                                             verbose_name='样品数量 (g)')  # Field renamed to remove unsuitable characters.
    sample_purpose = models.CharField(max_length=255, blank=True, verbose_name='赠样用途')
    sample_progress = models.CharField(max_length=255, blank=True, verbose_name='进展')
    sales_time = models.CharField(max_length=255, blank=True, verbose_name='销售时间')
    sales_product = models.CharField(max_length=255, blank=True, verbose_name='销售产品')
    sales_specification = models.CharField(max_length=255, blank=True, verbose_name='销售规格')
    sales_unit_price_cny = models.CharField(max_length=255, blank=True,
                                            verbose_name='销售单价 (CNY)')  # Field renamed to remove unsuitable characters.
    sales_quantity_kg = models.CharField(max_length=255, blank=True,
                                         verbose_name='销售数量 (Kg)')  # Field renamed to remove unsuitable characters.
    sales_amount = models.CharField(max_length=255, blank=True, verbose_name='销售金额')
    sales_purpose = models.CharField(max_length=255, blank=True, verbose_name='销售用途')
    sales_progress = models.CharField(max_length=255, blank=True, verbose_name='销售进展')
    phone_sales_visit_description = models.TextField(blank=True,
                                                     verbose_name='电话销售/拜访记录')  # Field renamed to remove unsuitable characters.

    class Meta:
        # managed = False
        db_table = '研发部客户档案表'


class ExistingFormulationToDevelop(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序号')
    enterprise_name = models.CharField(max_length=255, blank=True, verbose_name='企业名称')
    province = models.CharField(max_length=255, blank=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, verbose_name='城市')
    department = models.CharField(max_length=255, blank=True, verbose_name='部门')
    specific_department = models.CharField(max_length=255, blank=True, verbose_name='具体部门')
    responsible_person = models.CharField(max_length=255, blank=True, verbose_name='负责人')
    customer_name = models.CharField(max_length=255, blank=True, verbose_name='客户姓名')
    customer_source = models.CharField(max_length=255, blank=True, verbose_name='客户来源')
    product = models.CharField(max_length=255, blank=True, verbose_name='产品')
    corresponding_specification_code = models.CharField(max_length=255, blank=True,
                                                        verbose_name='对应规格编码')
    special_requirements = models.CharField(max_length=255, blank=True, verbose_name='特殊需求')
    estimated_annual_consumption = models.CharField(max_length=255, blank=True, verbose_name='预估年用量')
    current_manufacturer = models.CharField(max_length=255, blank=True, verbose_name='现用厂家')
    product_level = models.CharField(db_column='product_level', max_length=255, blank=True,
                                     verbose_name='级别(药品级/化学级)')
    model_number = models.CharField(max_length=255, blank=True, verbose_name='型号')
    price_per_kg = models.CharField(max_length=255, blank=True, verbose_name='单价')
    formulation_name = models.CharField(max_length=255, blank=True, verbose_name='制剂名称')
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True,
                                                         verbose_name='是否一致性评价品种')
    auxiliary_material_usage = models.CharField(max_length=255, blank=True, verbose_name='辅料用途')
    prescription_dosage = models.CharField(max_length=255, blank=True, verbose_name='处方用量')
    development_date = models.DateField(verbose_name='起始开发日期')
    customer_importance = models.CharField(max_length=255, blank=True, verbose_name='客户重要程度')
    initial_negotiation = models.CharField(max_length=255, blank=True, verbose_name='前期洽谈')
    supplier_change_request = models.CharField(max_length=255, blank=True, verbose_name='提出供应商变更申请')
    supplier_audit = models.CharField(max_length=255, blank=True, verbose_name='供应商审计')
    continuous_batch_sample_testing = models.CharField(max_length=255, blank=True, verbose_name='连续3批辅料小样检测')
    first_production_of_3_batches = models.CharField(max_length=255, blank=True, verbose_name='首次生产3批')
    stability_study = models.CharField(max_length=255, blank=True, verbose_name='稳定性考察')
    additional_application_record_change = models.CharField(max_length=255, blank=True,
                                                            verbose_name='补充申请备案完成变更')
    formal_contract_signing = models.CharField(max_length=255, blank=True, verbose_name='正式合同签订')
    delivery = models.CharField(max_length=255, blank=True, verbose_name='发货')
    in_progress = models.CharField(max_length=255, blank=True, verbose_name='进行中')
    notes = models.CharField(max_length=255, blank=True, verbose_name='备注')
    before_pilot_scale_up = models.CharField(max_length=255, blank=True, verbose_name='中试前')
    before_submission = models.CharField(max_length=255, blank=True, verbose_name='申报前')
    issuing_time = models.DateField(verbose_name='开具时间')
    landing_enterprise_name = models.CharField(max_length=255, blank=True, verbose_name='落地企业名称')
    contact_person = models.CharField(max_length=255, blank=True, verbose_name='联系人')
    handover_sales_manager = models.CharField(max_length=255, blank=True, verbose_name='移交销售经理')
    handover_time = models.DateField(verbose_name='移交时间')

    class Meta:
        # managed = False
        db_table = '已有制剂待开发进度表'


class ExistingFormulationProgressDescription(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='序号')
    timestamp = models.DateField(verbose_name='时间戳')
    progress = models.CharField(max_length=255, blank=True, verbose_name='进度')
    status = models.CharField(max_length=255, blank=True, verbose_name='状态')
    subordinate_id = models.CharField(max_length=255, blank=True, verbose_name='隶属ID')

    class Meta:
        # managed = False
        db_table = '已有制剂进度描述表'


class ExistingFormulationDeveloping(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序号')
    enterprise_name = models.CharField(max_length=255, blank=True, verbose_name='企业名称')
    province = models.CharField(max_length=255, blank=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, verbose_name='城市')
    department = models.CharField(max_length=255, blank=True, verbose_name='部门')
    specific_department = models.CharField(max_length=255, blank=True, verbose_name='具体部门')
    responsible_person = models.CharField(max_length=255, blank=True, verbose_name='负责人')
    customer_name = models.CharField(max_length=255, blank=True, verbose_name='客户姓名')
    customer_source = models.CharField(max_length=255, blank=True, verbose_name='客户来源')
    product = models.CharField(max_length=255, blank=True, verbose_name='产品')
    corresponding_specification_code = models.CharField(max_length=255, blank=True,
                                                        verbose_name='对应规格编码')
    special_requirements = models.CharField(max_length=255, blank=True, verbose_name='特殊需求')
    estimated_annual_consumption = models.CharField(max_length=255, blank=True, verbose_name='预估年用量')
    current_manufacturer = models.CharField(max_length=255, blank=True, verbose_name='现用厂家')
    product_level = models.CharField(db_column='product_level', max_length=255, blank=True,
                                     verbose_name='级别(药品级/化学级)')
    model_number = models.CharField(max_length=255, blank=True, verbose_name='型号')
    price_per_kg = models.CharField(max_length=255, blank=True, verbose_name='单价')
    formulation_name = models.CharField(max_length=255, blank=True, verbose_name='制剂名称')
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True,
                                                         verbose_name='是否一致性评价品种')
    auxiliary_material_usage = models.CharField(max_length=255, blank=True, verbose_name='辅料用途')
    prescription_dosage = models.CharField(max_length=255, blank=True, verbose_name='处方用量')
    development_date = models.DateField(verbose_name='起始开发日期')
    customer_importance = models.CharField(max_length=255, blank=True, verbose_name='客户重要程度')
    initial_negotiation = models.CharField(max_length=255, blank=True, verbose_name='前期洽谈')
    supplier_change_request = models.CharField(max_length=255, blank=True, verbose_name='提出供应商变更申请')
    supplier_audit = models.CharField(max_length=255, blank=True, verbose_name='供应商审计')
    continuous_batch_sample_testing = models.CharField(max_length=255, blank=True, verbose_name='连续3批辅料小样检测')
    first_production_of_3_batches = models.CharField(max_length=255, blank=True, verbose_name='首次生产3批')
    stability_study = models.CharField(max_length=255, blank=True, verbose_name='稳定性考察')
    additional_application_record_change = models.CharField(max_length=255, blank=True,
                                                            verbose_name='补充申请备案完成变更')
    formal_contract_signing = models.CharField(max_length=255, blank=True, verbose_name='正式合同签订')
    delivery = models.CharField(max_length=255, blank=True, verbose_name='发货')
    in_progress = models.CharField(max_length=255, blank=True, verbose_name='进行中')
    notes = models.CharField(max_length=255, blank=True, verbose_name='备注')
    before_pilot_scale_up = models.CharField(max_length=255, blank=True, verbose_name='中试前')
    before_submission = models.CharField(max_length=255, blank=True, verbose_name='申报前')
    issuing_time = models.DateField(verbose_name='开具时间')
    landing_enterprise_name = models.CharField(max_length=255, blank=True, verbose_name='落地企业名称')
    contact_person = models.CharField(max_length=255, blank=True, verbose_name='联系人')
    handover_sales_manager = models.CharField(max_length=255, blank=True, verbose_name='移交销售经理')
    handover_time = models.DateField(verbose_name='移交时间')

    class Meta:
        # managed = False
        db_table = '已有制剂开发中进度表'


class ExistingProductCompleted(models.Model):
    serial_number = models.AutoField(primary_key=True, verbose_name='序号')
    enterprise_name = models.CharField(max_length=255, blank=True, verbose_name='企业名称')
    province = models.CharField(max_length=255, blank=True, verbose_name='省份')
    city = models.CharField(max_length=255, blank=True, verbose_name='城市')
    department = models.CharField(max_length=255, blank=True, verbose_name='部门')
    specific_department = models.CharField(max_length=255, blank=True, verbose_name='具体部门')
    responsible_person = models.CharField(max_length=255, blank=True, verbose_name='负责人')
    customer_name = models.CharField(max_length=255, blank=True, verbose_name='客户姓名')
    customer_source = models.CharField(max_length=255, blank=True, verbose_name='客户来源')
    product = models.CharField(max_length=255, blank=True, verbose_name='产品')
    corresponding_specification_code = models.CharField(max_length=255, blank=True,
                                                        verbose_name='对应规格编码')
    special_requirements = models.CharField(max_length=255, blank=True, verbose_name='特殊需求')
    estimated_annual_consumption = models.CharField(max_length=255, blank=True, verbose_name='预估年用量')
    current_manufacturer = models.CharField(max_length=255, blank=True, verbose_name='现用厂家')
    product_level = models.CharField(db_column='product_level', max_length=255, blank=True,
                                     verbose_name='级别(药品级/化学级)')
    model_number = models.CharField(max_length=255, blank=True, verbose_name='型号')
    price_per_kg = models.CharField(max_length=255, blank=True, verbose_name='单价')
    formulation_name = models.CharField(max_length=255, blank=True, verbose_name='制剂名称')
    is_consistency_evaluation_product = models.CharField(max_length=255, blank=True,
                                                         verbose_name='是否一致性评价品种')
    auxiliary_material_usage = models.CharField(max_length=255, blank=True, verbose_name='辅料用途')
    prescription_dosage = models.CharField(max_length=255, blank=True, verbose_name='处方用量')
    development_date = models.DateField(verbose_name='起始开发日期')
    customer_importance = models.CharField(max_length=255, blank=True, verbose_name='客户重要程度')
    initial_negotiation = models.CharField(max_length=255, blank=True, verbose_name='前期洽谈')
    supplier_change_request = models.CharField(max_length=255, blank=True, verbose_name='提出供应商变更申请')
    supplier_audit = models.CharField(max_length=255, blank=True, verbose_name='供应商审计')
    continuous_batch_sample_testing = models.CharField(max_length=255, blank=True, verbose_name='连续3批辅料小样检测')
    first_production_of_3_batches = models.CharField(max_length=255, blank=True, verbose_name='首次生产3批')
    stability_study = models.CharField(max_length=255, blank=True, verbose_name='稳定性考察')
    additional_application_record_change = models.CharField(max_length=255, blank=True,
                                                            verbose_name='补充申请备案完成变更')
    formal_contract_signing = models.CharField(max_length=255, blank=True, verbose_name='正式合同签订')
    delivery = models.CharField(max_length=255, blank=True, verbose_name='发货')
    in_progress = models.CharField(max_length=255, blank=True, verbose_name='进行中')
    notes = models.CharField(max_length=255, blank=True, verbose_name='备注')
    before_pilot_scale_up = models.CharField(max_length=255, blank=True, verbose_name='中试前')
    before_submission = models.CharField(max_length=255, blank=True, verbose_name='申报前')
    issuing_time = models.DateField(verbose_name='开具时间')
    landing_enterprise_name = models.CharField(max_length=255, blank=True, verbose_name='落地企业名称')
    contact_person = models.CharField(max_length=255, blank=True, verbose_name='联系人')
    handover_sales_manager = models.CharField(max_length=255, blank=True, verbose_name='移交销售经理')
    handover_time = models.DateField(verbose_name='移交时间')

    class Meta:
        # managed = False
        db_table = '已有制剂已完成进度表'


class Employees(models.Model):
    DEPARTMENT_CHOICES = [
        ('原辅料销售部', '原辅料销售部'),
        ('食品添加剂部', '食品添加剂部'),
        ('外贸部', '外贸部'),
        ('研发服务部', '研发服务部'),
        ('产品管理部', '产品管理部'),
        ('内务部', '内务部'),
        ('信管部', '信管部'),
    ]
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES, blank=True, verbose_name='部门')
    position = models.CharField(max_length=255, blank=True, verbose_name='职位')
    name = models.CharField(max_length=255, blank=True, verbose_name='姓名')
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, blank=True, verbose_name='性别')
    work_id = models.CharField(primary_key=True, max_length=255, verbose_name='工号')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, blank=True, verbose_name='状态')
    password = models.CharField(max_length=255, blank=True, verbose_name='密码')

    class Meta:
        db_table = '员工信息表'


# 报表及视图
class Receivable(models.Model):
    """应收账款明细（原辅料、食品、研发、产品）"""
    # 编号（从1开始自动递增）
    id = models.AutoField(primary_key=True, verbose_name='编号')
    # 存储关联的唯一标识符,内贸部台账id
    internal_trade_ledger_id = models.IntegerField()
    # 交易日期（物流发运日期）
    transaction_date = models.DateField(verbose_name='交易日期')
    # 省份（省份）
    province = models.CharField(max_length=255, verbose_name='省份')
    # 客户名称（单位名称）
    customer_name = models.CharField(max_length=255, verbose_name='客户名称')
    # 业务员（业务员）
    salesperson = models.CharField(max_length=255, verbose_name='业务员')
    # 应收账款（未收款）
    accounts_receivable = models.CharField(max_length=255, verbose_name='应收账款')
    # 应收账款期限（自己输入）
    accounts_receivable_due_date = models.DateField(verbose_name='应收账款期限')
    # 还款日（自己输入）
    repayment_date = models.DateField(verbose_name='还款日')
    # 已收货款1（自己输入）
    received_payment_1 = models.CharField(max_length=255, verbose_name='已收货款1')
    # 已收货款2（自己输入）
    received_payment_2 = models.CharField(max_length=255, verbose_name='已收货款2')
    # 应收账款余额（前面三个字段的数字的差额，应收账款-已收货款1-已收货款2）
    accounts_receivable_balance = models.CharField(max_length=255, verbose_name='应收账款余额')
    # 备注（自己输入）
    remarks = models.TextField(blank=True, verbose_name='备注')

    class Meta:
        # managed = False
        db_table = '收账款明细'


class Overdue(models.Model):
    # 编号（从1开始自动递增）
    id = models.AutoField(primary_key=True, verbose_name='编号')
    # 逾期说明与回款计划
    description = models.TextField(blank=True, verbose_name='逾期说明与回款计划')
    # Receivable id
    received_id = models.IntegerField()

    class Meta:
        # managed = False
        db_table = '逾期账款明细'


class Foreign_receivable(models.Model):
    """应收账款明细（外贸部）"""
    # 编号（从1开始自动递增）
    id = models.AutoField(primary_key=True, verbose_name='编号')
    # 外贸部id
    foreign_trade_ledger_id = models.IntegerField()
    # 交易日期（销售日期）
    transaction_date = models.DateField(verbose_name='交易日期')
    # 客户名称（单位名称）
    customer_name = models.CharField(max_length=255, verbose_name='客户名称')
    # 业务员
    salesperson = models.CharField(max_length=255, verbose_name='业务员')
    # 应收账款- USD（未收款-USD）
    accounts_receivable_usd = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='应收账款-USD')
    # 应收账款-RMB（未收款-人民币）
    accounts_receivable_rmb = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='应收账款-人民币')
    # 应收账款期限
    accounts_receivable_due = models.DateField(verbose_name='应收账款期限')
    # 还款日
    repayment_date = models.DateField(verbose_name='还款日')
    # 已收货款1- USD
    received_payment1_usd = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='已收货款1-USD')
    # 已收货款1-RMB
    received_payment1_rmb = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='已收货款1-人民币')
    # 已收货款2- USD
    received_payment2_usd = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='已收货款2-USD')
    # 已收货款2-RMB
    received_payment2_rmb = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='已收货款2-人民币')
    # 应收账款余额- USD
    accounts_receivable_balance_usd = models.DecimalField(max_digits=10, decimal_places=2,
                                                          verbose_name='应收账款余额-USD')
    # 应收账款余额-RMB
    accounts_receivable_balance_rmb = models.DecimalField(max_digits=10, decimal_places=2,
                                                          verbose_name='应收账款余额-人民币')
    # 折人民币
    rmb_discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='折人民币')
    # 备注
    remarks = models.TextField(blank=True, verbose_name='备注')

    class Meta:
        # managed = False
        db_table = '外贸部收款明细'


class Reimbursement(models.Model):
    """各部门回款目标"""
    DEPARTMENT_CHOICES = [
        ('sales1', '销售一部'),
        ('sales2', '销售二部'),
        ('sales3', '销售三部'),
        ('sales4', '销售四部'),
        ('sales5', '销售五部'),
        ('sales6', '销售六部'),
        ('additives', '食品添加剂部'),
        ('rnd_service', '研发服务部'),
        ('foreign_trade', '外贸部'),
    ]

    name = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES, unique=True)
    year = models.IntegerField(verbose_name="年份")
    target_jan = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="1月回款目标")
    target_feb = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="2月回款目标")
    target_mar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="3月回款目标")
    target_apr = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="4月回款目标")
    target_may = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="5月回款目标")
    target_jun = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="6月回款目标")
    target_jul = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="7月回款目标")
    target_aug = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="8月回款目标")
    target_sep = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="9月回款目标")
    target_oct = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="10月回款目标")
    target_nov = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="11月回款目标")
    target_dec = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="12月回款目标")

    class Meta:
        unique_together = ('name', 'year')
        # managed = False
        db_table = '各部门回款目标'


class ActualSales(models.Model):
    """实际销售数据"""
    department = models.ForeignKey(Reimbursement, on_delete=models.CASCADE)
    year = models.IntegerField()
    actual_jan = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="1月实际回款")
    actual_feb = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="2月实际回款")
    actual_mar = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="3月实际回款")
    actual_apr = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="4月实际回款")
    actual_may = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="5月实际回款")
    actual_jun = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="6月实际回款")
    actual_jul = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="7月实际回款")
    actual_aug = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="8月实际回款")
    actual_sep = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="9月实际回款")
    actual_oct = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="10月实际回款")
    actual_nov = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="11月实际回款")
    actual_dec = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="12月实际回款")

    class Meta:
        # managed = False
        db_table = '实际销售数据'


class ComplaintSummary(models.Model):
    """全国客诉汇总"""
    id = models.AutoField(primary_key=True)
    month = models.CharField(max_length=20, verbose_name='月份')
    shipment_date = models.DateField(verbose_name='发货日期')
    department = models.CharField(max_length=100, verbose_name='部门')

    # 使用choices参数限制complaint_type字段的选项
    complaint_type = models.CharField(max_length=100, verbose_name='客诉问题类型')
    form_type = models.CharField(max_length=100, verbose_name='表单类型')
    contract_number = models.CharField(max_length=100, verbose_name='合同编号')
    customer_name = models.CharField(max_length=100, verbose_name='客户名称')
    product_name = models.CharField(max_length=100, verbose_name='产品名称')
    specification = models.CharField(max_length=100, verbose_name='规格')
    replacement_quantity = models.FloatField(verbose_name='补/换货数量（KG）')
    reason = models.TextField(verbose_name='原因')
    # 定义选择项
    CATEGORY_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]
    category = models.CharField(max_length=1,
                                choices=CATEGORY_CHOICES, verbose_name='分类')
    remarks = models.TextField(verbose_name='备注（补/换货运单号）')
    return_history = models.TextField(verbose_name='退货记录')

    class Meta:
        # managed = False
        db_table = '全国客诉汇总'


class SalesVisitReport(models.Model):
    """销售客户拜访报告"""
    # 假设序号是自动生成的，不需要手动输入
    serial_number = models.AutoField(primary_key=True, verbose_name='序号')
    # 企业名称
    company_name = models.CharField(max_length=255, verbose_name='企业名称')
    # 拜访日期
    visit_date = models.DateField(verbose_name='拜访日期')
    # 本年度拜访次数
    visits_this_year = models.PositiveIntegerField(verbose_name='本年度拜访次数')
    # 客户性质 - 新客户或老客户
    CUSTOMER_TYPE_CHOICES = [
        ('new', '新客户'),
        ('existing', '老客户'),
    ]
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPE_CHOICES, verbose_name='客户性质')
    # 拜访性质
    visit_nature = models.CharField(max_length=255, verbose_name='拜访性质')
    # 拜访目的
    visit_purpose = models.TextField(verbose_name='拜访目的')
    # 拜访结果及反馈
    visit_feedback = models.TextField(verbose_name='拜访结果及反馈')
    # 备注
    remarks = models.TextField(blank=True, verbose_name='备注')

    class Meta:
        # managed = False
        db_table = '销售客户拜访报告'
