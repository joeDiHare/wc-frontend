# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 03:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displaydata', '0003_auto_20170315_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displaydata',
            name='shortcode',
            field=models.CharField(default='cfdefaultvalue', max_length=15, unique=True),
        ),
    ]