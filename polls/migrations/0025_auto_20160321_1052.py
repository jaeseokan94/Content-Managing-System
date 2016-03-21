# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-21 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_auto_20160320_1634'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='question_type',
        ),
        migrations.AddField(
            model_name='exercisequestion',
            name='question_type',
            field=models.CharField(choices=[('ty', 'Typing'), ('tf', 'True or False'), ('dd', 'Drag and Drop'), ('mc', 'Multiple Choice')], default=('ty', 'Typing'), max_length=3),
        ),
    ]
