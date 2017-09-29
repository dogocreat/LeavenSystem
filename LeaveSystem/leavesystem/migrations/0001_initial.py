# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatePost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, editable=False)),
                ('dep', models.CharField(default=True, max_length=100, choices=[(b'RD', b'RD'), (b'RDI', b'RDI'), (b'RDII', b'RDII')])),
                ('leaveDate', models.DateTimeField(null=True, blank=True)),
                ('timeRange', models.CharField(max_length=100, choices=[(b'True', b'\xe4\xb8\x8a\xe5\x8d\x88'), (b'False', b'\xe4\xb8\x8b\xe5\x8d\x88')])),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
