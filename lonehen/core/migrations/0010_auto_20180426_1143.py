# Generated by Django 2.0.4 on 2018-04-26 11:43

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_shopitem_raw_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitem',
            name='raw_description',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
