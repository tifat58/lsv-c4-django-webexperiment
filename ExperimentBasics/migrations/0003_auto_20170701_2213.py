# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-07-01 20:13
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExperimentBasics', '0002_auto_20170520_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='medal_height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='experiment',
            name='medal_width',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='experiment',
            name='user_medal',
            field=models.ImageField(blank=True, height_field='medal_height', null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/static//medals/medal.png', location='/static//medals/'), upload_to='/static//medals/', width_field='medal_width'),
        ),
        migrations.AddField(
            model_name='news',
            name='news_description_mk',
            field=models.CharField(max_length=1024, null=True, verbose_name='news description'),
        ),
        migrations.AddField(
            model_name='news',
            name='news_description_sl',
            field=models.CharField(max_length=1024, null=True, verbose_name='news description'),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='is_exactly_correct',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='normalized_form_is_correct',
            field=models.NullBooleanField(),
        ),
    ]
