# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-25 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ExperimentBasics', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentenceTranslationAnswer',
            fields=[
                ('sentence_translation_answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('translated_sentence', models.CharField(max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SentenceTranslationExperiment',
            fields=[
                ('experiment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='ExperimentBasics.Experiment')),
                ('sentence_translation_experiment_id', models.AutoField(primary_key=True, serialize=False)),
                ('foreign_language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SentenceTranslation_foreign_language', to='Users.Language')),
                ('native_language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SentenceTranslation_native_language', to='Users.Language')),
            ],
            bases=('ExperimentBasics.experiment',),
        ),
        migrations.CreateModel(
            name='SentenceTranslationQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='ExperimentBasics.Question')),
                ('sentence_translation_question_id', models.AutoField(primary_key=True, serialize=False)),
                ('stimulus_sentence', models.CharField(max_length=512)),
            ],
            bases=('ExperimentBasics.question',),
        ),
        migrations.CreateModel(
            name='SentenceTranslationCorrectAnswer',
            fields=[
                ('sentencetranslationanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='SentenceTranslationExperiment.SentenceTranslationAnswer')),
                ('sentence_translation_correct_answer_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('SentenceTranslationExperiment.sentencetranslationanswer',),
        ),
        migrations.CreateModel(
            name='SentenceTranslationUserAnswer',
            fields=[
                ('sentencetranslationanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='SentenceTranslationExperiment.SentenceTranslationAnswer')),
                ('useranswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='ExperimentBasics.UserAnswer')),
                ('sentence_translation_user_answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('result_changes', models.TextField(null=True)),
            ],
            bases=('ExperimentBasics.useranswer', 'SentenceTranslationExperiment.sentencetranslationanswer'),
        ),
    ]