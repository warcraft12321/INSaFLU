# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing_files', '0017_projectsample_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='is_ready_for_projects',
            field=models.BooleanField(default=False),
        ),
    ]
