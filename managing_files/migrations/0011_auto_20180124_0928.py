# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-24 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing_files', '0010_auto_20180116_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date attached'),
        ),
        migrations.AddField(
            model_name='project',
            name='is_deleted_in_file_system',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sample',
            name='date_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date attached'),
        ),
        migrations.AddField(
            model_name='sample',
            name='is_deleted_in_file_system',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='uploadfiles',
            name='date_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Date attached'),
        ),
        migrations.AddField(
            model_name='uploadfiles',
            name='is_deleted_in_file_system',
            field=models.BooleanField(default=False),
        ),
    ]
