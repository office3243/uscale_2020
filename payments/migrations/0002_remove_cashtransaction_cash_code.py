# Generated by Django 3.0.2 on 2020-02-03 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cashtransaction',
            name='cash_code',
        ),
    ]