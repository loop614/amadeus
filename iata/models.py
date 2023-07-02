from __future__ import annotations

from django.db import models

from client.iata_endpoints import get_location_by_iata


class Iata(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=256)
    detailed_name = models.CharField(max_length=256, default='')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)


def get_iata_pks_by_code(iata_code) -> list[int]:
    iatas = Iata.objects.filter(code=iata_code)
    if iatas.exists():
        return [iata.id for iata in iatas]

    amadeus_location = get_location_by_iata(iata_code)

    iata_ids = []
    for amadeus in amadeus_location:
        iata = Iata(
            code=amadeus['iataCode'],
            name=amadeus['name'],
            detailed_name=amadeus['detailedName'],
        )
        iata.save()
        iata_ids.append(iata.id)

    return iata_ids
