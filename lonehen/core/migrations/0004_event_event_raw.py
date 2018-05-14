# Generated by Django 2.0.4 on 2018-04-25 18:10

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180425_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_raw',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default='default'),
            preserve_default=False,
        ),
    ]
