# Generated by Django 3.0.4 on 2020-03-13 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseSistema', '0002_auto_20200312_2331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipoia',
            name='meta',
        ),
        migrations.RemoveField(
            model_name='tipoia',
            name='src',
        ),
    ]