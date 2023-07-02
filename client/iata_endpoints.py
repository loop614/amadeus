from __future__ import annotations

import os

import requests

from client.auth_endpoints import amadeus_auth


class IataNotFoundError(Exception):
    ...


def get_location_by_iata(iata_code):
    url = os.environ.get('AMADEUS_API_BASE_URL') + \
        os.environ.get('AMADEUS_API_REFERENCE_DATA_LOCATIONS')
    headers = {'Authorization': amadeus_auth()}

    # TODO: check .env.dev
    # response = requests.get(url, {'subType': 'CITY', 'keyword': iata_code}, headers=headers)
    # response_json = response.json()

    if iata_code == 'HSV':
        return mock_hsv_iata().get('data', {})

    if iata_code == 'BHM':
        return mock_bhm_iata().get('data', {})

    return mock_bhm_iata()
    # for error in response_json.get('errors', []):
    #     if error.get('code') in [1797, 38196]:
    #         raise IataNotFoundError()
    #
    # return response_json.get('data', {})


def mock_hsv_iata():
    return {
        'data': [{
            'iataCode': 'HSV',
            'name': 'something with HSV',
            'detailedName': 'details of HSV',
        }],
    }


def mock_bhm_iata():
    return {
        'data': [{
            'iataCode': 'BHM',
            'name': 'something with BHM',
            'detailedName': 'details of BHM',
        }],
    }
