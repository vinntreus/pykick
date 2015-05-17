# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(default=b'', max_length=255)),
                ('version', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('data', models.TextField(default=b'')),
                ('agg_id', models.UUIDField()),
                ('agg_type', models.CharField(max_length=255)),
                ('version', models.PositiveIntegerField()),
                ('ts', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
