# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_exercise_exercise_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='situationalvideo',
            name='choice_1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='situationalvideo',
            name='choice_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='situationalvideo',
            name='choice_3',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='situationalvideo',
            name='choice_4',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='situationalvideo',
            name='choice_5',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='situationalvideo',
            name='choice_6',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='situationalvideo',
            name='correct_answers',
            field=models.CharField(default='1', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='situationalvideo',
            name='question_text',
            field=models.CharField(default='question text', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='name',
            field=models.CharField(choices=[('Alphabet', 'Alphabet'), ('Numbers', 'Numbers'), ('Days', 'Days of the Week'), ('Holidays', 'Holidays'), ('Months', 'Seasons and Months'), ('Time', 'Time')], default=0, max_length=200),
        ),
    ]
