# Generated by Django 5.0.3 on 2024-03-10 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventsapp', '0003_alter_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
    ]