# Generated by Django 3.0.2 on 2020-02-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_accounts', '0002_auto_20200203_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_code',
            field=models.CharField(default='', max_length=7),
        ),
    ]