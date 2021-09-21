import requests
from pprint import pprint
API_BASE_URL = 'https://www.superheroapi.com/api.php/2619421814940190/'

headers = {
    'accept':'application/json',
}

names_hero = ['Hulk', 'Captain America', 'Thanos']

#Вариант 1 
max_intelligence = -100000000000000
smart_hero = ''
for hero in range(len(names_hero)):
  response = requests.get(API_BASE_URL + 'search/'+ names_hero[hero], headers = headers)
  current_intelligence = response.json()['results'][0]['powerstats']['intelligence']
  if int(current_intelligence) > max_intelligence:
    max_intelligence = int(current_intelligence)
    smart_hero = names_hero[hero]

print(f"Самый умный супергерой - {smart_hero}. Его интелект - {max_intelligence}")

#Вариант 2

heros_id = []
heros_dict = {}
for hero in range(len(names_hero)):
  response = requests.get(API_BASE_URL + 'search/'+ names_hero[hero], headers = headers)
  heros_id.append (response.json()['results'][0]['id'])

  response = requests.get(API_BASE_URL + heros_id[hero] + '/powerstats', headers = headers)
  heros_dict[names_hero[hero]] = response.json()['intelligence']


for hero, intel in heros_dict.items():
  if int(intel) > max_intelligence:
    max_intelligence = int(intel)
    smart_hero = hero
print(smart_hero)
  

