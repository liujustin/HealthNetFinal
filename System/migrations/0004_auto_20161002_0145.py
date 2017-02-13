# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-02 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('System', '0003_auto_20161002_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='cell_number',
            field=models.IntegerField(default=1, max_length=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='health_insurance_number',
            field=models.IntegerField(default=1, max_length=4),
        ),
        migrations.AlterField(
            model_name='patient',
            name='next_appointment',
            field=models.DateField(default=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='zipcode',
            field=models.IntegerField(default=1, max_length=5),
        ),
    ]
