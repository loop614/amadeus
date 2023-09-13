from __future__ import annotations

import json
import os

import client.auth_endpoints as auth
import client.flight_parser as parser


class FlightNotFoundError(Exception):
    ...


def amadeus_search_flights(request_dict):
    url = os.environ.get('AMADEUS_API_BASE_URL') + \
        os.environ.get('AMADEUS_API_SHOPPING_FLIGHT_OFFERS')
    headers = {'Authorization': auth.amadeus_auth()}
    amadeus_request_dict = map_amadeus_request(request_dict)
    # usual way would be to send a request to amadeus
    # response = requests.get(url, params=amadeus_request_dict, headers=headers)
    # response_json = response.json()

    response_json = mock_response_json()
    for error in response_json.get('errors', []):
        if error['status'] < 500 or error['status'] > 400:
            raise FlightNotFoundError

    return parser.parse_amadeus({**request_dict, **amadeus_request_dict}, response_json)


def mock_response_json():
    with open('client/amadeus_mock/shopping/flight-offers/bhm-hsv.json') as f_in:
        return json.load(f_in)


def map_amadeus_request(request_dict):
    return {
        'originLocationCode': request_dict['departure_iata'],
        'destinationLocationCode': request_dict['destination_iata'],
        'departureDate': request_dict['outgoing_date'],
        'adults': request_dict['passenger_count'],
        'nonStop': 'false',
        'max': 5,
    }
