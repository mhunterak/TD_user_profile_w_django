# Generated by Django 2.1.5 on 2019-06-16 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='last_name',
        ),
    ]
