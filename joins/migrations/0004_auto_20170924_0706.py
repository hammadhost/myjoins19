# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-24 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_auto_20170924_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default='ABC', max_length=120, unique=True),
        ),
    ]
