from __future__ import annotations

from django.forms import model_to_dict

from connection.models import Connection
from flight.models import Flight
from iata.models import get_iata_pks_by_code


def parse_amadeus(request_dict, amadeus_json):
    response_json = {'flights': {}}

    for flight_offer in amadeus_json.get('data', []):
        if flight_offer['type'] == 'flight-offer':
            iata_departure = get_iata_pks_by_code(
                request_dict['departure_iata'],
            )
            iata_destination = get_iata_pks_by_code(
                request_dict['destination_iata'],
            )

            for fk_departure in iata_departure:
                for fk_destination in iata_destination:
                    response_json = create_flight_per_iata(
                        fk_departure,
                        fk_destination,
                        flight_offer,
                        request_dict,
                        response_json,
                    )

    return response_json


def create_flight_per_iata(fk_departure, fk_destination, flight_offer, request_dict, response_json):
    total_price = flight_offer.get('price', {}).get('total')
    currency = flight_offer.get('price', {}).get('currency')
    flight = Flight(
        fk_destination_id=fk_destination,
        fk_departure_id=fk_departure,
        price=total_price,
        currency=currency,
        outgoing_date=request_dict['outgoing_date'],
        return_date=request_dict['return_date'],
        passenger_count=request_dict['passenger_count'],
    )
    flight.save()
    response_json['flights'][flight.id] = model_to_dict(flight)
    response_json['flights'][flight.id]['connections'] = []
    for itinerary in flight_offer['itineraries']:
        for segment in itinerary['segments']:
            response_json = create_connection_per_segment(
                flight, segment, response_json,
            )

    return response_json


def create_connection_per_segment(flight, segment, response_json):
    connection_departure = segment.get('departure', {}).get('iataCode')
    connection_arrival = segment.get('arrival', {}).get('iataCode')
    departure_fks_iata = get_iata_pks_by_code(connection_departure)
    arrival_fks_iata = get_iata_pks_by_code(connection_arrival)
    for departure_fk_iata in departure_fks_iata:
        for arrival_fk_iata in arrival_fks_iata:
            connection = Connection(
                fk_flight_id=flight.id,
                fk_connection_departure_id=departure_fk_iata,
                fk_connection_destination_id=arrival_fk_iata,
                duration=segment.get('duration'),
                departure_at=segment.get('departure', {}).get('at'),
                departure_terminal=segment.get(
                    'departure', {},
                ).get('terminal'),
                arrival_at=segment.get('arrival', {}).get('at'),
                arrival_terminal=segment.get('arrival', {}).get('terminal'),
                number_of_stops=segment.get(
                    'arrival', {},
                ).get('numberOfStops'),
            )
            connection.save()
            response_json['flights'][flight.id]['connections'].append(
                model_to_dict(connection),
            )

    return response_json
