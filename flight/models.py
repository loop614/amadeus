from django.db import models
from iata.models import Iata


class Flight(models.Model):
    fk_departure = models.ForeignKey(Iata, on_delete=models.DO_NOTHING, related_name='flight_departure')
    fk_destination = models.ForeignKey(Iata, on_delete=models.DO_NOTHING, related_name='flight_destination')
    outgoing_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    passenger_count = models.IntegerField(null=True)
    price = models.FloatField()
    currency = models.CharField(max_length=8)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
