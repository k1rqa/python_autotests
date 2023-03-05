import requests


token = 'dbf8f9d039fbf43fcaaea5aea619e198'
add_pokemon_repsonse = requests.post ('https://pokemonbattle.me:9104/pokemons', headers= {'Content-Type': 'application/json', 'trainer_token': token},
               json={"name": "Бульбазавр", "photo": "https://dolnikov.ru/pokemons/albums/010.png"})

print(add_pokemon_repsonse.text)

change_pokemons_name_repsonse = requests.put ('https://pokemonbattle.me:9104/pokemons', headers= {'Content-Type': 'application/json', 'trainer_token': token},
            json={"pokemon_id": 5981, "name": "Кирилл", "photo": "https://dolnikov.ru/pokemons/albums/010.png"})

print(change_pokemons_name_repsonse.text)

add_pokeball_repsonse = requests.post ('https://pokemonbattle.me:9104/trainers/add_pokeball', headers= {'Content-Type': 'application/json', 'trainer_token': token},
            json={"pokemon_id": 5981})

print(add_pokeball_repsonse.text)