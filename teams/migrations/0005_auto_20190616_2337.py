# Generated by Django 2.1.5 on 2019-06-16 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20190616_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='incumbent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incumbent', to='accounts.Profile'),
        ),
    ]
