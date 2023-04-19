from django.db import models
from iata.models import Iata
from flight.models import Flight


class Connection(models.Model):
    fk_flight = models.ForeignKey(Flight, on_delete=models.DO_NOTHING)
    fk_connection_departure = models.ForeignKey(Iata, on_delete=models.DO_NOTHING, related_name='connection_departure')
    fk_connection_destination = models.ForeignKey(Iata, on_delete=models.DO_NOTHING, related_name='connection_destination')
    arrival_terminal = models.CharField(max_length=256, null=True)
    departure_terminal = models.CharField(max_length=256, null=True)
    duration = models.CharField(max_length=256, null=True)
    number_of_stops = models.IntegerField(null=True)
    arrival_at = models.DateTimeField(null=True)
    departure_at = models.DateTimeField(null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
