# Generated by Django 4.1.7 on 2023-03-15 00:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_alter_employee_date_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2023, 3, 14, 21, 18, 56, 417953), verbose_name='Fecha de registro'),
        ),
    ]