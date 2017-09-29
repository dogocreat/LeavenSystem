# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavesystem', '0004_datepost_testdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datepost',
            name='testDate',
        ),
    ]
