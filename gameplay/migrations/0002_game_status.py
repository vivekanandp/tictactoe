# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-24 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('gameplay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(default='F', max_length=1),
        ),
    ]
