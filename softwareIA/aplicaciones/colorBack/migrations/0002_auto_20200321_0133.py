# Generated by Django 3.0.4 on 2020-03-21 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colorBack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorinfo',
            name='red',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='colorBack.RedColor'),
        ),
    ]
