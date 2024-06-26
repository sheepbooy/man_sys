# Generated by Django 4.2.1 on 2024-03-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_rename_authorization_number_authorization_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='preparation_new',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('status', models.CharField(blank=True, choices=[('开发中', '开发中'), ('进行中', '进行中'), ('已完成', '已完成'), ('暂停', '暂停')], max_length=20, verbose_name='开发状态')),
                ('serial_number', models.IntegerField(blank=True, verbose_name='序号')),
                ('enterprise_name', models.CharField(blank=True, max_length=100, verbose_name='企业名称')),
                ('province', models.CharField(blank=True, max_length=50, verbose_name='省份')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='城市')),
                ('department', models.CharField(blank=True, max_length=100, verbose_name='部门')),
                ('specific_department', models.CharField(blank=True, max_length=100, verbose_name='具体部门')),
                ('responsible_person', models.CharField(blank=True, max_length=100, verbose_name='负责人')),
                ('customer_name', models.CharField(blank=True, max_length=100, verbose_name='客户名称')),
                ('customer_source', models.CharField(blank=True, max_length=100, verbose_name='客户来源')),
                ('product', models.CharField(blank=True, max_length=100, verbose_name='产品')),
                ('corresponding_specification_code', models.CharField(blank=True, max_length=100, verbose_name='对应规格编码')),
                ('special_requirements', models.CharField(blank=True, max_length=200, verbose_name='特殊需求')),
                ('estimated_annual_consumption', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='预估年用量')),
                ('current_manufacturer', models.CharField(blank=True, max_length=100, verbose_name='现用厂家')),
                ('grade', models.CharField(blank=True, max_length=50, verbose_name='级别（药用级/化工级）')),
                ('model_number', models.CharField(blank=True, max_length=100, verbose_name='型号')),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='单价（kg）')),
                ('preparation_name', models.CharField(blank=True, max_length=100, verbose_name='制剂名称')),
                ('consistency_evaluation_variety', models.BooleanField(default=False, verbose_name='是否一致性评价品种')),
                ('auxiliary_material_usage', models.CharField(blank=True, max_length=100, verbose_name='辅料用途')),
                ('prescription_dosage', models.CharField(blank=True, max_length=100, verbose_name='处方用量')),
                ('date', models.DateField(blank=True, null=True, verbose_name='时间')),
                ('customer_importance_level', models.CharField(blank=True, max_length=10, verbose_name='客户重要程度')),
                ('initial_negotiation', models.DateField(blank=True, null=True, verbose_name='前期洽谈')),
                ('supplier_change_request', models.DateField(blank=True, null=True, verbose_name='提出供应商变更申请')),
                ('supplier_audit', models.DateField(blank=True, null=True, verbose_name='供应商审计')),
                ('continuous_3_batch_auxiliary_material_sampling_testing', models.DateField(blank=True, null=True, verbose_name='连续3批辅料小样检测')),
                ('first_production_3_batches', models.DateField(blank=True, null=True, verbose_name='首次生产3批')),
                ('stability_inspection', models.DateField(blank=True, null=True, verbose_name='稳定性考察')),
                ('supplementary_application_completion_change', models.DateField(blank=True, null=True, verbose_name='补充申请备案完成变更')),
                ('formal_contract_signing', models.DateField(blank=True, null=True, verbose_name='正式合同签订')),
                ('delivery', models.DateField(blank=True, null=True, verbose_name='发货')),
                ('in_progress', models.DateField(blank=True, null=True, verbose_name='进行中')),
                ('remarks', models.TextField(blank=True, verbose_name='备注（现状简报）')),
                ('before_pilot', models.DateField(blank=True, null=True, verbose_name='中试前')),
                ('before_declaration', models.DateField(blank=True, null=True, verbose_name='申报前')),
                ('issuance_date', models.DateField(blank=True, null=True, verbose_name='开具时间')),
                ('landing_enterprise_name', models.CharField(blank=True, max_length=100, verbose_name='落地企业名称')),
                ('contact_person', models.CharField(blank=True, max_length=100, verbose_name='联系人')),
                ('transfer_sales_manager', models.CharField(blank=True, max_length=100, verbose_name='移交销售经理')),
                ('transfer_date', models.DateField(blank=True, null=True, verbose_name='移交时间')),
            ],
            options={
                'db_table': '新已有制剂表',
            },
        ),
    ]
