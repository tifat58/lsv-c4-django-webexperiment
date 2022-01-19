# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-26 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ExperimentBasics', '0001_initial'),
        ('Users', '0004_userinfo_highest_education_degree'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeTranslationWithContextAnswer',
            fields=[
                ('free_translation_with_context_answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('gap_answer', models.CharField(max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FreeTranslationWithContextExperiment',
            fields=[
                ('experiment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='ExperimentBasics.Experiment')),
                ('free_translation_with_context_experiment_id', models.AutoField(primary_key=True, serialize=False)),
                ('foreign_language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FreeTranslationWithContext_foreign_language', to='Users.Language')),
                ('native_language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='FreeTranslationWithContext_native_language', to='Users.Language')),
            ],
            bases=('ExperimentBasics.experiment',),
        ),
        migrations.CreateModel(
            name='FreeTranslationWithContextQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='ExperimentBasics.Question')),
                ('free_translation_with_context_question_id', models.AutoField(primary_key=True, serialize=False)),
                ('sentence', models.CharField(max_length=1024)),
                ('question_answer_time', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
            bases=('ExperimentBasics.question',),
        ),
        migrations.CreateModel(
            name='FreeTranslationWithContextCorrectAnswer',
            fields=[
                ('freetranslationwithcontextanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='FreeTranslationWithContextExperiment.FreeTranslationWithContextAnswer')),
                ('free_translation_with_context_correct_answer_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('FreeTranslationWithContextExperiment.freetranslationwithcontextanswer',),
        ),
        migrations.CreateModel(
            name='FreeTranslationWithContextUserAnswer',
            fields=[
                ('freetranslationwithcontextanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='FreeTranslationWithContextExperiment.FreeTranslationWithContextAnswer')),
                ('useranswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='ExperimentBasics.UserAnswer')),
                ('free_translation_with_context_user_answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('result_changes', models.TextField(null=True)),
                ('words_click_time', models.TextField(null=True)),
            ],
            bases=('ExperimentBasics.useranswer', 'FreeTranslationWithContextExperiment.freetranslationwithcontextanswer'),
        ),
        migrations.AddField(
            model_name='freetranslationwithcontextquestion',
            name='correct_answers',
            field=models.ManyToManyField(related_name='associated_question', to='FreeTranslationWithContextExperiment.FreeTranslationWithContextCorrectAnswer'),
        ),
    ]
