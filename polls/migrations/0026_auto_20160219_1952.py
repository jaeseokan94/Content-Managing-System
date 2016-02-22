# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0025_auto_20160217_1737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='situationalvideo',
            options={'ordering': ('language_topic',)},
        ),
    ]
