import os
import requests

from client.auth_endpoints import amadeus_auth


class IataNotFoundError(Exception):
    ...


def get_location_by_iata(iata_code):
    url = os.environ.get('AMADEUS_API_BASE_URL') + os.environ.get('AMADEUS_API_REFERENCE_DATA_LOCATIONS')
    headers = {'Authorization': amadeus_auth()}
    response = requests.get(url, {'subType': 'CITY', 'keyword': iata_code}, headers=headers)
    response_json = response.json()
    for error in response_json.get('errors', []):
        if error.get('code') in [1797, 38196]:
            raise IataNotFoundError()

    return response_json.get('data', {})

