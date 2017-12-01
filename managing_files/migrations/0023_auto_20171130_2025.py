# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managing_files', '0022_auto_20171129_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountVariations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.PositiveIntegerField(default=0)),
                ('var_less_50', models.PositiveIntegerField(default=0)),
                ('var_bigger_50', models.PositiveIntegerField(default=0)),
                ('project_sample', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='count_variations', to='managing_files.ProjectSample')),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(default='value not needed', max_length=50)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='managing_files.TagName')),
            ],
        ),
        migrations.AlterField(
            model_name='metakey',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='metakeyproject',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='uploaded date'),
        ),
        migrations.AlterField(
            model_name='metakeyprojectsample',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='uploaded date'),
        ),
        migrations.AlterField(
            model_name='metakeysample',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='uploaded date'),
        ),
    ]
