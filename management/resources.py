from management.models import ForeignCustomerProfile
from import_export.fields import Field
from django.db.models.fields import DateField, DateTimeField
import logging
from django.db import IntegrityError
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from django.contrib.auth.models import User
from management import models

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


class Products_resource(resources.ModelResource):
    # 初始化时，指定一个属性来存储用户选择的导出字段
    export_fields = None

    class Meta:
        model = models.Products

    def set_export_fields(self, field_names):
        """
        根据用户选择设置需要导出的字段。
        :param field_names: 字段名称列表
        """
        self.export_fields = field_names

    def get_export_fields(self):
        fields = super(Products_resource, self).get_export_fields()
        # 如果设置了export_fields，则过滤字段
        if self.export_fields is not None:
            fields = [field for field in fields if
                      field.attribute in self.export_fields or field.column_name in self.export_fields]
        else:
            # 默认行为，排除 'id' 字段
            fields = [field for field in fields if field.column_name != 'id']
        return fields

    def get_export_headers(self):
        headers = []
        for field in self.get_export_fields():  # 注意这里调用的是get_export_fields来确保字段一致性
            # 使用字段的verbose_name作为列头，如果字段在模型定义中
            if hasattr(self.Meta.model, field.attribute):
                model_field = self.Meta.model._meta.get_field(field.attribute)
                headers.append(model_field.verbose_name)
            else:
                # 对于自定义Field或不存在于模型中的字段，使用其属性名
                headers.append(field.attribute)
        return headers

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        model = self.Meta.model
        # 创建映射，排除'id'字段
        field_mapping = {f.verbose_name: f.name for f in model._meta.fields}
        # 将列名从中文转换为英文
        dataset.headers = [field_mapping.get(header, header) for header in dataset.headers]
