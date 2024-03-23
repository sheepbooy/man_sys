from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from management import models
from django.contrib.auth.models import User

"""
    model: 指定你想要导入导出的 Django 模型类。
    fields: 指定一个字段名称的列表或元组，这些字段将被包含在导入和导出中。如果设置为 '__all__'，则表示导入导出模型中的所有字段。
    exclude: 指定一个字段名称的列表或元组，这些字段将在导入和导出时被排除。
    export_order: 定义导出时字段的顺序。它是一个包含字段名称的列表或元组。
    import_id_fields: 定义哪些字段应被用作查找已存在记录的标识。默认是模型的主键。
    widgets: 一个字典，允许为模型字段定义自定义小部件（widgets）。小部件用于在导入和导出时转换字段值。
    skip_unchanged: 如果设置为 True，在导入时将跳过未发生变化的记录。默认为 False。
    report_skipped: 控制是否在导入报告中包含被跳过的记录。默认为 True。
    use_transactions: 指定是否在导入过程中使用数据库事务。默认为 True，以保证数据的一致性。
    batch_size: 定义每批处理的记录数。这对于优化导入过程的性能特别有用。
    clean_model_instances: 在保存模型实例之前，确定是否调用模型的 full_clean 方法来验证数据的完整性。默认为 True。
"""


class BaseResource(resources.ModelResource):
    """基础资源类，用于导出数据的共通处理, 无外键"""
    export_fields = None  # 初始化时，指定一个属性来存储用户选择的导出字段

    def set_export_fields(self, field_names):
        """
        根据用户选择设置需要导出的字段。
        :param field_names: 字段名称列表
        """
        self.export_fields = field_names

    def get_export_fields(self):
        fields = super().get_export_fields()
        if self.export_fields is not None:
            fields = [field for field in fields if
                      field.attribute in self.export_fields or field.column_name in self.export_fields]
        else:
            fields = [field for field in fields if field.column_name != 'id']
        return fields

    def get_export_headers(self):
        headers = []
        for field in self.get_export_fields():
            if hasattr(self.Meta.model, field.attribute):
                model_field = self.Meta.model._meta.get_field(field.attribute)
                headers.append(model_field.verbose_name)
            else:
                headers.append(field.attribute)
        return headers

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        model = self.Meta.model
        field_mapping = {f.verbose_name: f.name for f in model._meta.fields}
        dataset.headers = [field_mapping.get(header, header) for header in dataset.headers]


class ProductsResource(BaseResource):
    """药用辅料产品规格编码设置表-2022.08.18"""

    class Meta:
        model = models.Products
        import_id_fields = ('spec_code',)


class ForeignCustomerResource(BaseResource):
    """外贸部客户档案表模板202303"""

    class Meta:
        model = models.ForeignCustomerProfile


class turnover_resource(BaseResource):
    """研发部客户流水表导入"""

    class Meta:
        model = models.CustomerFlow


class butting_resource(BaseResource):
    """研发部客户对接表"""

    class Meta:
        model = models.CustomerEngagement


class dev_custom_resource(BaseResource):
    """研发部客户档案表"""

    class Meta:
        model = models.CustomerProfile


class sales_visit_report_resource(BaseResource):
    """销售客户拜访报告"""

    class Meta:
        model = models.SalesVisitReport


class customer_audit_resource(BaseResource):
    """客户审计表"""

    class Meta:
        model = models.CustomerAudit


class preparation_new_resource(BaseResource):
    """已有制剂"""

    class Meta:
        model = models.preparation_new


class product_new_resource(BaseResource):
    """新品"""

    class Meta:
        model = models.product_new


class authorization_resource(BaseResource):
    """授权书总表"""

    class Meta:
        model = models.Authorization


class question_resource(BaseResource):
    """问题调查表"""

    class Meta:
        model = models.Feedback


class medicine_resource(BaseResource):
    """仿制药参比制剂目录"""

    class Meta:
        model = models.Medicine


class sales_forecast_resource(BaseResource):
    """预算详情表"""

    class Meta:
        model = models.SalesForecast


class complaint_summary_resource(BaseResource):
    """结合部门和产品分类的客诉汇总"""

    class Meta:
        model = models.ComplaintSummary


class inner_trade_ledger_resource(BaseResource):
    """内贸部台账表"""

    class Meta:
        model = models.InternalTradeLedger


class foreign_trade_ledger_resource(BaseResource):
    """外贸部台账表"""

    class Meta:
        model = models.ForeignTradeLedger


class EmployeeResource(BaseResource):
    # 假设User模型有一个字段与Employee的工号对应，这里使用username作为例子
    user = fields.Field(
        column_name='user',
        attribute='user',
        widget=ForeignKeyWidget(User, 'username'))

    class Meta:
        model = models.Employees
        import_id_fields = ('work_id',)

    def before_import_row(self, row, **kwargs):
        """
        重写此方法以在导入每行之前处理数据。
        """
        # 工号(work_id)是User的username
        work_id = row.get('work_id')
        if work_id:
            user, created = User.objects.get_or_create(username=work_id)
            row['user'] = user.username  # 确保user字段指向正确的User对象
