# Generated by Django 4.2 on 2023-04-19 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('iata', '0001_initial'),
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_terminal', models.CharField(max_length=256)),
                ('departure_terminal', models.CharField(max_length=256)),
                ('duration', models.CharField(max_length=256)),
                ('number_of_stops', models.IntegerField()),
                ('arrival_at', models.DateTimeField()),
                ('departure_at', models.DateTimeField()),
                ('fk_connection_departure', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='connection_departure', to='iata.iata')),
                ('fk_connection_destination', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='connection_destination', to='iata.iata')),
                ('fk_flight', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='flight.flight')),
            ],
        ),
    ]
