import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json' , 'trainer_token' : '15acfc259967a2c38432bbf1e20b5b4a'}
TOKEN = '15acfc259967a2c38432bbf1e20b5b4a'

def test_status_cod():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : 2160})
    assert response.status_code == 200


def test_trainer_id():
    response = requests.get(url = f'{URL}/trainers', params = {"trainer_id" : 2160})
    assert response.json ()['data'][0]['id'] == '2160'