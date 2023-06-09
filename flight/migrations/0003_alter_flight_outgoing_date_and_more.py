# Generated by Django 4.2 on 2023-04-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_alter_flight_outgoing_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='outgoing_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='passenger_count',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='return_date',
            field=models.DateField(null=True),
        ),
    ]
