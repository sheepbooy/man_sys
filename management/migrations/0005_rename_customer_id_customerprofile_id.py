# Generated by Django 4.2.1 on 2024-03-11 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_rename_engagement_number_customerengagement_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerprofile',
            old_name='customer_id',
            new_name='id',
        ),
    ]