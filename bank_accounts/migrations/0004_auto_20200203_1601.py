# Generated by Django 3.0.2 on 2020-02-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_accounts', '0003_auto_20200203_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_code',
            field=models.CharField(default='1', max_length=7),
        ),
    ]
