# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0022_auto_20160331_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download',
            name='code',
            field=models.CharField(blank=True, max_length=40, unique=True, verbose_name='Код'),
        ),
    ]
