# Generated by Django 5.0.1 on 2024-02-03 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0004_measurement_sensor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='sensor',
        ),
    ]
