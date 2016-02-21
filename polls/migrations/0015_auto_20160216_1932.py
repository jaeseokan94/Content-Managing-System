# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20160216_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='languagetopic',
            name='topic_name',
            field=models.CharField(default='Greeting', max_length=200),
        ),
        migrations.AlterField(
            model_name='languagetopic',
            name='topic_name_in_english',
            field=models.CharField(default='Greeting', max_length=200),
        ),
        migrations.AlterField(
            model_name='languagetopic',
            name='topic_name_in_language',
            field=models.CharField(default='Saludo', max_length=200),
        ),
    ]
