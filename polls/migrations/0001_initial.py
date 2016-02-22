# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Dialect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name_in_language', models.CharField(max_length=200)),
            ],
        ),
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
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name2', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='LanguageSubtopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subtopic_name', models.CharField(max_length=200, null=True)),
                ('video_url', models.FileField(null=True, upload_to=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic_name_in_language', models.CharField(default=b'Saludo', max_length=200)),
                ('language', models.ForeignKey(to='polls.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=0, max_length=200, choices=[(b'Alphabet', b'Alphabet'), (b'Numbers', b'Numbers'), (b'Days of the Week', b'Days of the Week'), (b'Holidays', b'Holidays'), (b'Seasons and Months', b'Seasons and Months'), (b'Time', b'Time')])),
                ('name_in_language', models.CharField(max_length=200)),
                ('instructions', models.CharField(max_length=200)),
                ('instructions_in_language', models.CharField(max_length=200)),
                ('dialect_id', models.ForeignKey(to='polls.Dialect')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=200)),
                ('word_in_language', models.CharField(max_length=200)),
                ('pronounciation_guide_or_date', models.CharField(max_length=200)),
                ('audio_url', models.FileField(null=True, upload_to=b'', blank=True)),
                ('resource_id', models.ForeignKey(to='polls.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceItemPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phrase', models.CharField(max_length=200)),
                ('phrase_in_language', models.CharField(max_length=200)),
                ('picture_url', models.FileField(null=True, upload_to=b'', blank=True)),
                ('audio_url', models.FileField(null=True, upload_to=b'', blank=True)),
                ('resource_id', models.ForeignKey(to='polls.Resource')),
            ],
        ),
        migrations.CreateModel(
            name='SituationalVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('situation_description', models.CharField(max_length=200)),
                ('video_with_transcript', models.FileField(null=True, upload_to=b'', blank=True)),
                ('video_wihtout_transcript', models.FileField(null=True, upload_to=b'', blank=True)),
                ('language_topic', models.ForeignKey(to='polls.LanguageTopic', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(default=b'b', max_length=1, choices=[(b'b', b'Beginner'), (b'i', b'Intermediate')])),
                ('topic_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='languagetopic',
            name='topic',
            field=models.ForeignKey(to='polls.Topic'),
        ),
        migrations.AddField(
            model_name='languagesubtopic',
            name='language_topic',
            field=models.ForeignKey(to='polls.LanguageTopic', null=True),
        ),
        migrations.AddField(
            model_name='exercise',
            name='language_subtopic',
            field=models.ForeignKey(to='polls.LanguageSubtopic', null=True),
        ),
        migrations.AddField(
            model_name='dialect',
            name='language_id',
            field=models.ForeignKey(to='polls.Language'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='polls.Question'),
        ),
    ]
