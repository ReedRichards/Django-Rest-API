# Generated by Django 2.0.4 on 2018-04-25 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_press_event_raw'),
    ]

    operations = [
        migrations.RenameField(
            model_name='press',
            old_name='event_raw',
            new_name='press_raw',
        ),
    ]