# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 08:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0038_auto_20170219_1615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_config_path',
        ),
    ]
