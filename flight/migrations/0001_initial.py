# Generated by Django 4.2 on 2023-04-19 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('iata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outgoing_date', models.DateField()),
                ('return_date', models.DateField(default=None)),
                ('passenger_count', models.IntegerField()),
                ('price', models.FloatField()),
                ('currency', models.CharField(max_length=8)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('fk_departure', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='flight_departure', to='iata.iata')),
                ('fk_destination', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='flight_destination', to='iata.iata')),
            ],
        ),
    ]
