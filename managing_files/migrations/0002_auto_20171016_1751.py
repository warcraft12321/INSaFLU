# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 17:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import managing_files.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('managing_files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MetaKeySample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='uploaded date')),
                ('value', models.CharField(default='value not needed', max_length=200)),
                ('description', models.TextField(default='')),
                ('meta_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meta_key_sample', to='managing_files.MetaKey')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meta_key_sample', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['sample__id', 'meta_tag__id', 'creation_date'],
            },
        ),
        migrations.CreateModel(
            name='SampleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sample_tag', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RemoveField(
            model_name='project',
            name='create_user',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='user_uploaded',
        ),
        migrations.AddField(
            model_name='files',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reference',
            name='number_of_sequences',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reference',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reference', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sample',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sample', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='files',
            name='file_name_1',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='file_name_2',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='path_name_1',
            field=models.FileField(max_length=400, upload_to=managing_files.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='files',
            name='path_name_2',
            field=models.FileField(max_length=400, upload_to=managing_files.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='reference',
            name='reference',
            field=models.FileField(max_length=400, upload_to=managing_files.models.reference_directory_path),
        ),
        migrations.AlterField(
            model_name='sample',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='software',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='metakeysample',
            name='sample',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meta_key_sample', to='managing_files.Sample'),
        ),
        migrations.AddField(
            model_name='sample',
            name='tag_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sample', to='managing_files.SampleTag'),
        ),
    ]
