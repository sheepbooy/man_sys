# Generated by Django 4.2.1 on 2024-03-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0021_delete_salesvisitreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesVisitReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('company_name', models.CharField(blank=True, max_length=255, verbose_name='企业名称')),
                ('visit_date', models.DateField(blank=True, verbose_name='拜访日期')),
                ('visits_this_year', models.IntegerField(blank=True, verbose_name='本年度拜访次数')),
                ('customer_type', models.CharField(blank=True, max_length=255, verbose_name='客户性质')),
                ('visit_nature', models.CharField(blank=True, max_length=255, verbose_name='拜访性质')),
                ('visit_purpose', models.TextField(blank=True, verbose_name='拜访目的')),
                ('visit_feedback', models.TextField(blank=True, verbose_name='拜访结果及反馈')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
            ],
            options={
                'db_table': '销售客户拜访报告',
            },
        ),
    ]
