# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 19:19
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0007_auto_20170317_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='email',
            field=models.CharField(default='ste@gmail.com', max_length=220, validators=[shortener.validators.validate_dot_com]),
        ),
    ]
