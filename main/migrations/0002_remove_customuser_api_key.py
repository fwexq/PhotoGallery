# Generated by Django 4.0.7 on 2022-08-28 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='api_key',
        ),
    ]
