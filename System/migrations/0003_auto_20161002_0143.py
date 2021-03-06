# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-02 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0002_auto_20161001_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='cell_number',
            field=models.IntegerField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='patient',
            name='health_insurance_number',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AddField(
            model_name='patient',
            name='hospital',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='next_appointment',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='patient',
            name='physician',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='zipcode',
            field=models.IntegerField(default=0, max_length=5),
        ),
    ]
