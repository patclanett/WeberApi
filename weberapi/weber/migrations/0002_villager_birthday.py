# Generated by Django 3.0.6 on 2020-05-13 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weber', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='villager',
            name='birthday',
            field=models.CharField(default='01/01', max_length=40),
        ),
    ]
