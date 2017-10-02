# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leavesystem', '0005_remove_datepost_testdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='datepost',
            name='comment',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
