# Generated by Django 2.0.4 on 2018-04-24 01:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='post_date',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='Date Published'),
        ),
    ]
