# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-19 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GapFillingExperiment', '0002_gapfillingquestion_question_answer_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='gapfillinguseranswer',
            name='words_click_time',
            field=models.TextField(null=True),
        ),
    ]
