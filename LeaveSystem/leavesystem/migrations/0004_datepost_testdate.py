# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavesystem', '0003_auto_20170928_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='datepost',
            name='testDate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
