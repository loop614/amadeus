# Generated by Django 4.2 on 2023-04-19 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0004_alter_connection_arrival_terminal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='number_of_stops',
            field=models.IntegerField(null=True),
        ),
    ]
