import os
import requests
from functools import lru_cache


@lru_cache
def amadeus_auth():
    auth_url = os.environ.get('AMADEUS_API_BASE_URL') + os.environ.get('AMADEUS_API_TOKEN_URL')
    data = {
        'grant_type': 'client_credentials',
        'client_id': os.environ.get('AMADEUS_API_KEY'),
        'client_secret': os.environ.get('AMADEUS_API_SECRET')
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(url=auth_url, data=data, headers=headers)
    response_json = response.json()

    return response_json['token_type'] + ' ' + response_json['access_token']
