# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-25 13:26
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.CharField(blank=True,
                                   help_text="It's always nice to add a friendly message!",
                                   max_length=300,
                                   verbose_name='Optional message'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='to_user',
            field=models.ForeignKey(
                help_text='Please select a user you want to play a game with.',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='invitations_received',
                to=settings.AUTH_USER_MODEL, verbose_name='User to invite'),
        ),
    ]
