# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-10 17:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20170710_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='buy_place',
        ),
        migrations.DeleteModel(
            name='BuyPlace',
        ),
    ]