# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20160223_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisevocabularyquestion',
            name='correct_answer',
            field=models.CharField(default=(b'1', b'1'), max_length=1, choices=[(b'1', b'1'), (b'2', b'2'), (b'3', b'3'), (b'4', b'4'), (b'5', b'5'), (b'6', b'6')]),
        ),
    ]
