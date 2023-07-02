from __future__ import annotations

import os

import requests

from client.auth_endpoints import amadeus_auth
from client.flight_parser import parse_amadeus


class FlightNotFoundError(Exception):
    ...


def amadeus_search_flights(request_dict):
    url = os.environ.get('AMADEUS_API_BASE_URL') + \
        os.environ.get('AMADEUS_API_SHOPPING_FLIGHT_OFFERS')
    headers = {'Authorization': amadeus_auth()}
    amadeus_request_dict = map_amadeus_request(request_dict)
    # response = requests.get(url, params=amadeus_request_dict, headers=headers)
    # response_json = response.json()
    response_json = mock_response_json()
    for error in response_json.get('errors', []):
        if error['status'] > 400:
            raise FlightNotFoundError

    return parse_amadeus({**request_dict, **amadeus_request_dict}, response_json)


def mock_response_json():
    return {
        'data': [{
            'type': 'flight-offer',
            'price': {
                'total': 120,
                'currency': 'EUR',
            },
            'itineraries': [
                {
                    'segments': [
                        {
                            'departure': {
                                'iataCode': 'HSV',
                                'at': '2022-12-30 14:00',
                                'terminal': 1,
                                'numberOfStops': 2,
                            },
                            'duration': '',
                            'arrival': {
                                'iataCode': 'BHM',
                                'at': '2023-01-01 14:00',
                                'terminal': 2,
                                'numberOfStops': 2,
                            },
                        },
                    ],
                },
            ],
        }],
        'errors': [],
    }


def map_amadeus_request(request_dict):
    return {
        'originLocationCode': request_dict['departure_iata'],
        'destinationLocationCode': request_dict['destination_iata'],
        'departureDate': request_dict['outgoing_date'],
        'adults': request_dict['passenger_count'],
        'nonStop': 'false',
        'max': 5,
    }
