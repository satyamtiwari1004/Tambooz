# Generated by Django 3.1.7 on 2023-03-15 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='content',
        ),
    ]
