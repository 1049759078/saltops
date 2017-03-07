# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 09:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools_manager', '0033_auto_20170212_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toolsexecjob',
            options={'verbose_name': '工具执行', 'verbose_name_plural': '工具执行'},
        ),
        migrations.AlterField(
            model_name='toolsexecjob',
            name='tools',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools_manager.ToolsScript', verbose_name='工具'),
        ),
        migrations.AlterField(
            model_name='toolsscript',
            name='tools_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools_manager.ToolsTypes', verbose_name='工具类型'),
        ),
    ]