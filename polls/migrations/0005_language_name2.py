# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20160208_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='name2',
            field=models.CharField(default=datetime.datetime(2016, 2, 13, 23, 1, 16, 894002, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
