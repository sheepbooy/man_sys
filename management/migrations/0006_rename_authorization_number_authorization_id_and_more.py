# Generated by Django 4.2.1 on 2024-03-11 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_rename_customer_id_customerprofile_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authorization',
            old_name='authorization_number',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='existingformulationdeveloping',
            old_name='serial_number',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='existingformulationtodevelop',
            old_name='serial_number',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='existingproductcompleted',
            old_name='serial_number',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='foreigntradeledger',
            old_name='serial_number',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='newproductcompleted',
            old_name='serial_number',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='newproductdevelopingprogress',
            old_name='serial_number',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='salesvisitreport',
            old_name='serial_number',
            new_name='id',
        ),
    ]