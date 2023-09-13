from __future__ import annotations

from django.http import HttpResponseBadRequest
from django.template.response import TemplateResponse

import client.flight_endpoints as flight_endpoints
import iata.models as iata_models
from client.iata_endpoints import IataNotFoundError
from connection.models import Connection


def flights(request):
    context_data = {'errors': []}
    request_keys = [
        'departure_iata',
        'destination_iata',
        'outgoing_date',
        'passenger_count',
        'currency',
    ]

    request_dict = {}
    for request_key in request_keys:
        request_dict[request_key] = request.GET.get(request_key)
        if not request_dict[request_key]:
            context_data['errors'].append(
                {'message': f'Bad request, missing {request_key}'},
            )

    request_dict['return_date'] = request.GET.get('return_date', default=None)

    if request_dict.get('departure_iata', False) and request_dict.get('destination_iata', False):
        try:
            request_dict['departure_iata_pks'] = iata_models.get_iata_pks_by_code(
                request_dict['departure_iata'],
            )
            request_dict['destination_iata_pks'] = iata_models.get_iata_pks_by_code(
                request_dict['destination_iata'],
            )
        except IataNotFoundError:
            context_data['errors'].append({'message': 'IATA not found error'})

    if len(context_data['errors']) > 0:
        return HttpResponseBadRequest(', <br>'.join(one['message'] for one in context_data['errors']))

    context_data['data_source'] = 'basement'
    flight_data = Connection.objects.select_related('fk_flight').filter(
        fk_flight__fk_departure__in=request_dict['departure_iata_pks'],
        fk_flight__fk_destination__in=request_dict['destination_iata_pks'],
        fk_flight__outgoing_date=request_dict['outgoing_date'],
        fk_flight__return_date=request_dict['return_date'],
        fk_flight__passenger_count=request_dict['passenger_count'],
        fk_flight__currency=request_dict['currency'],
    ).values()

    if not flight_data.count():
        context_data['data_source'] = 'other peoples basement'
        flight_data = flight_endpoints.amadeus_search_flights(request_dict)

    context_data['flight_data'] = flight_data
    context_data['request_dict'] = request_dict

    return TemplateResponse(request, 'flight/index.html', context=context_data)
