# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-04 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0015_auto_20161031_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='physician',
            name='first_name',
            field=models.CharField(default='firstname', max_length=100),
        ),
        migrations.AlterField(
            model_name='physician',
            name='last_name',
            field=models.CharField(default='lastname', max_length=100),
        ),
    ]
