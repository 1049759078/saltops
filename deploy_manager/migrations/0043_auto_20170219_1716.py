# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0042_projectconfigfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectconfigfile',
            name='config_path',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='配置文件路径'),
        ),
    ]
