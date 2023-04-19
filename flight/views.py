from django.template.response import TemplateResponse

from client.iata_endpoints import IataNotFoundError
from client.flight_endpoints import amadeus_search_flights
from connection.models import Connection
from iata.models import get_iata_pks_by_code


def flights(request):
    data = {'errors': []}
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
            data['errors'].append({'message': f'Bad request, missing {request_key}'})

    request_dict['return_date'] = request.GET.get('return_date', default=None)
    try:
        request_dict['departure_iata_pks'] = get_iata_pks_by_code(request_dict['departure_iata'])
        request_dict['destination_iata_pks'] = get_iata_pks_by_code(request_dict['destination_iata'])
    except IataNotFoundError:
        data['errors'].append({'message': 'IATA not found error'})

    if len(data['errors']) > 0:
        return TemplateResponse(request, 'flight/index.html', context=data)

    flights = Connection.objects.select_related('fk_flight').filter(
        fk_flight__fk_departure__in=request_dict['departure_iata_pks'],
        fk_flight__fk_destination__in=request_dict['destination_iata_pks'],
        fk_flight__outgoing_date=request_dict['outgoing_date'],
        fk_flight__return_date=request_dict['return_date'],
        fk_flight__passenger_count=request_dict['passenger_count'],
        fk_flight__currency=request_dict['currency'],
    ).values()

    if not flights.count():
        flights = amadeus_search_flights(request_dict)

    data['flights'] = flights
    print(data)
    return TemplateResponse(request, 'flight/index.html', context=data)
