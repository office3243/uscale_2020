# Generated by Django 3.0.2 on 2020-02-03 07:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('attribute', models.CharField(blank=True, max_length=6)),
                ('material_code', models.CharField(max_length=12)),
                ('extra_info', models.TextField(blank=True)),
                ('has_report', models.BooleanField(default=False)),
                ('up_rate', models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(limit_value=0.1)])),
                ('default_rate', models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(limit_value=0.1)])),
                ('down_rate', models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(limit_value=0.1)])),
                ('is_active', models.BooleanField(default=True)),
                ('merge_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='merge_materials', to='materials.Material')),
            ],
        ),
    ]
