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
    class Meta:
        model = models.Products

    def get_export_fields(self):
        fields = super(Products_resource, self).get_export_fields()
        fields = [field for field in fields if field.column_name != 'id']  # 排除 'id' 字段
        return fields

    def get_export_headers(self):
        headers = []
        for field in self.get_fields():
            # 排除'id'字段
            if field.attribute == 'id':
                continue
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

# class Products_resource(resources.ModelResource):
#     """
#     药用辅料产品规格编码设置表-2022.08.18。
#     在初始化时排除'id'字段，确保在导入和导出时不处理'id'字段，
#     同时在导入前将中文列名转换为英文列名。
#     """
#
#     def __init__(self, *args, **kwargs):
#         super(Products_resource, self).__init__(*args, **kwargs)
#         if 'id' in self.fields:
#             del self.fields['id']  # 在字段映射中排除'id'
#
#     def get_export_headers(self):
#         headers = []
#         for field in self.get_fields():
#             # 排除'id'字段
#             if field.attribute == 'id':
#                 continue
#             # 使用字段的verbose_name作为列头，如果字段在模型定义中
#             if hasattr(self.Meta.model, field.attribute):
#                 model_field = self.Meta.model._meta.get_field(field.attribute)
#                 headers.append(model_field.verbose_name)
#             else:
#                 # 对于自定义Field或不存在于模型中的字段，使用其属性名
#                 headers.append(field.attribute)
#         return headers
#
#     def before_import(self, dataset, using_transactions, dry_run, **kwargs):
#         model = self.Meta.model
#         # 创建映射，排除'id'字段
#         field_mapping = {f.verbose_name: f.name for f in model._meta.fields if f.name != 'id'}
#         # 将列名从中文转换为英文
#         dataset.headers = [field_mapping.get(header, header) for header in dataset.headers]
#
#     class Meta:
#         model = models.Products

# class EmployeeResource(resources.ModelResource):
#     user = fields.Field(
#         column_name='user',
#         attribute='user',
#         widget=ForeignKeyWidget(User, 'username'))
#
#     class Meta:
#         model = Employees
#         fields = ('work_id', 'name', 'gender', 'department', 'position', 'status')
#         exclude = ('user',)
#         import_id_fields = ('work_id',)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         field_to_verbose_name = {field.name: field.verbose_name for field in Employees._meta.fields}
#         english_to_chinese = {k: v for k, v in field_to_verbose_name.items() if k in self.fields}
#         chinese_to_english = {v: k for k, v in english_to_chinese.items()}
#
#         # 设置字段的column_name属性为中文verbose_name
#         for field_name, field in self.fields.items():
#             field.column_name = english_to_chinese.get(field_name, field_name)
#
#         # 保存中文到英文的映射供导入时使用
#         self.chinese_to_english_mapping = chinese_to_english

# def before_import(self, dataset, using_transactions, dry_run, **kwargs):
#     logger.info("原始列名: %s", dataset.headers)
#     dataset.headers = [self.chinese_to_english_mapping.get(col, col) for col in dataset.headers]
#     logger.info("映射后的列名: %s", dataset.headers)
#
#     # 移除空行
#     non_empty_rows = []
#     for row in dataset:
#         if any(cell for cell in row):
#             non_empty_rows.append(row)
#     dataset.dict = non_empty_rows
#
#     return super().before_import(dataset, using_transactions, dry_run, **kwargs)
#
# def before_import_row(self, row, **kwargs):
#     work_id = row.get('work_id')
#     if work_id:
#         try:
#             user, created = User.objects.get_or_create(username=work_id)
#             row['user'] = user.username
#         except IntegrityError as e:
#             logger.error("创建用户时出错，工号: %s, 错误: %s", work_id, e)
#             # 根据你的需要，你可以选择跳过这行数据，或者添加到某个错误日志中
#             # 例如: raise e
#
# def get_export_fields(self):
#     """
#     重写此方法以定制导出的字段，确保user字段在导出时不被包含。
#     """
#     fields = super().get_export_fields()
#     # 从导出的字段中排除user字段
#     export_fields = [field for field in fields if field.attribute != 'user']
#     return export_fields


# class ForeignCustomerProfileResource(resources.ModelResource):
#     class Meta:
#         model = ForeignCustomerProfile
#         fields = '__all__'
#         import_id_fields = ('id',)
#
#     def export_field(self, field, obj):
#         field_value = getattr(obj, field.attribute)
#         if isinstance(field, Field) and field_value is not None:
#             # 检查模型中的字段类型是否为日期或日期时间
#             model_field = self.Meta.model._meta.get_field(field.attribute)
#             if isinstance(model_field, (DateField, DateTimeField)):
#                 # 直接将日期或时间字段的值转换为字符串
#                 return str(field_value)
#         return super().export_field(field, obj)
