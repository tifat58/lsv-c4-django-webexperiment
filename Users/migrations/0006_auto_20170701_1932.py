# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-07-01 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20170514_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='country_name_mk',
            field=models.CharField(max_length=70, null=True, verbose_name='country name'),
        ),
        migrations.AddField(
            model_name='country',
            name='country_name_sl',
            field=models.CharField(max_length=70, null=True, verbose_name='country name'),
        ),
        migrations.AddField(
            model_name='educationdegree',
            name='name_mk',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='educationdegree',
            name='name_sl',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='gender',
            name='name_mk',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='gender',
            name='name_sl',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='language',
            name='language_name_mk',
            field=models.CharField(max_length=30, null=True, verbose_name='language'),
        ),
        migrations.AddField(
            model_name='language',
            name='language_name_sl',
            field=models.CharField(max_length=30, null=True, verbose_name='language'),
        ),
    ]
