# Generated by Django 4.1.7 on 2023-03-24 21:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_alter_message_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
