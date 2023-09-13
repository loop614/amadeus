from __future__ import annotations

import json
import os

import client.auth_endpoints as auth


class IataNotFoundError(Exception):
    ...


def get_location_by_iata(iata_code):
    url = os.environ.get('AMADEUS_API_BASE_URL') + \
        os.environ.get('AMADEUS_API_REFERENCE_DATA_LOCATIONS')
    headers = {'Authorization': auth.amadeus_auth()}

    # usual way would be to send a request to amadeus
    # response = requests.get(url, {'subType': 'CITY', 'keyword': iata_code}, headers=headers)
    # response_json = response.json()

    response_json = {}
    if iata_code == 'HSV':
        response_json = mock_hsv_iata()
    if iata_code == 'BHM':
        response_json = mock_bhm_iata()

    for error in response_json.get('errors', []):
        if error.get('code') in [1797, 38196]:
            raise IataNotFoundError()

    return response_json.get('data', {})


def mock_hsv_iata():
    with open('client/amadeus_mock/reference-data/locations/hsv.json') as f_in:
        return json.load(f_in)


def mock_bhm_iata():
    with open('client/amadeus_mock/reference-data/locations/bhm.json') as f_in:
        return json.load(f_in)
