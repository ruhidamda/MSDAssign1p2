# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-07 18:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_customer_updated_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutualFund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('share_class', models.CharField(max_length=50)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mutualfunds', to='portfolio.Customer')),
            ],
        ),
    ]
