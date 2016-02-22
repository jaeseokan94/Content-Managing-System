# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_auto_20160216_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instructions', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('choice_answers', models.CharField(max_length=200)),
                ('correct_answer', models.CharField(max_length=200)),
                ('exercise', models.ForeignKey(to='polls.Exercise', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageSubtopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subtopic_name', models.CharField(max_length=200, null=True)),
                ('video_url', models.CharField(max_length=200, null=True)),
                ('language_topic', models.ForeignKey(to='polls.LanguageTopic', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='language_subtopic',
            field=models.ForeignKey(to='polls.LanguageSubtopic', null=True),
        ),
    ]
