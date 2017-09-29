# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavesystem', '0002_datepost_is_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datepost',
            name='leaveDate',
            field=models.DateField(null=True, blank=True),
        ),
    ]
