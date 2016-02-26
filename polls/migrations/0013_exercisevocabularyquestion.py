# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 16:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20160223_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExerciseVocabularyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('choice_1', models.FileField(blank=True, null=True, upload_to='')),
                ('choice_2', models.FileField(blank=True, null=True, upload_to='')),
                ('choice_3', models.FileField(blank=True, null=True, upload_to='')),
                ('choice_4', models.FileField(blank=True, null=True, upload_to='')),
                ('choice_5', models.FileField(blank=True, null=True, upload_to='')),
                ('choice_6', models.FileField(blank=True, null=True, upload_to='')),
                ('correct_answer', models.CharField(max_length=200)),
                ('exercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Exercise')),
            ],
        ),
    ]