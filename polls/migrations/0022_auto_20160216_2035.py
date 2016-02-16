# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='language_subtopic',
        ),
        migrations.RemoveField(
            model_name='exercisequestion',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='languagesubtopic',
            name='language_topic',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='ExerciseQuestion',
        ),
        migrations.DeleteModel(
            name='LanguageSubtopic',
        ),
    ]
