# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_auto_20160219_2053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='situationalvideo',
            options={},
        ),
        migrations.AlterField(
            model_name='languagesubtopic',
            name='video_url',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
