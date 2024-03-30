import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json' , 'trainer_token' : '15acfc259967a2c38432bbf1e20b5b4a'}
TOKEN = '15acfc259967a2c38432bbf1e20b5b4a'
body = {
    "name": "Корнишон",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

#response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body )

#print(response.text)

body_new_pokenon_name = {
    "pokemon_id": "15175",
    "name": "skyandbunny",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

#response_pokemon_name = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_new_pokenon_name )

#print(response_pokemon_name.text)

body_pokeball = {
    "pokemon_id": "15175"
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_pokeball )

print(response_pokeball.text)