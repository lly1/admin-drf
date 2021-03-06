# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-17 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='remark',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('developer_supremo', '总监'), ('developer_manager', '经理'), ('developer', '研发')], default='developer', max_length=32),
        ),
    ]
