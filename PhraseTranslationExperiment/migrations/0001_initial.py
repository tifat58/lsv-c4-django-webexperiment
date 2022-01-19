# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-03-10 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0004_userinfo_highest_education_degree'),
        ('ExperimentBasics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhraseTranslationAnswer',
            fields=[
                ('phrase_translation_answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('native_word', models.CharField(max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhraseTranslationExperiment',
            fields=[
                ('experiment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='ExperimentBasics.Experiment')),
                ('phrase_translation_experiment_id', models.AutoField(primary_key=True, serialize=False)),
                ('foreign_language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PhraseTranslation_foreign_language', to='Users.Language')),
                ('native_language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PhraseTranslation_native_language', to='Users.Language')),
            ],
            bases=('ExperimentBasics.experiment',),
        ),
        migrations.CreateModel(
            name='PhraseTranslationQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='ExperimentBasics.Question')),
                ('phrase_translation_question_id', models.AutoField(primary_key=True, serialize=False)),
                ('foreign_word', models.CharField(max_length=512)),
            ],
            bases=('ExperimentBasics.question',),
        ),
        migrations.CreateModel(
            name='PhraseTranslationCorrectAnswer',
            fields=[
                ('phrasetranslationanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='PhraseTranslationExperiment.PhraseTranslationAnswer')),
                ('phrase_translation_correct_answer_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('PhraseTranslationExperiment.phrasetranslationanswer',),
        ),
        migrations.CreateModel(
            name='PhraseTranslationUserAnswer',
            fields=[
                ('phrasetranslationanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='PhraseTranslationExperiment.PhraseTranslationAnswer')),
                ('useranswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='ExperimentBasics.UserAnswer')),
                ('phrase_translation_user_answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('result_changes', models.TextField(null=True)),
            ],
            bases=('ExperimentBasics.useranswer', 'PhraseTranslationExperiment.phrasetranslationanswer'),
        ),
        migrations.AddField(
            model_name='phrasetranslationquestion',
            name='correct_answers',
            field=models.ManyToManyField(related_name='associated_question', to='PhraseTranslationExperiment.PhraseTranslationCorrectAnswer'),
        ),
    ]
