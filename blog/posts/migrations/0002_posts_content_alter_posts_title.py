# Generated by Django 4.1.7 on 2023-03-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='content',
            field=models.CharField(default='hello wordl', max_length=10000),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
