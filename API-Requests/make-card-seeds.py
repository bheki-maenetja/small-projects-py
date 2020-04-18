import json 
from urllib import request, error
from random import choice
import requests

my_list = []

banned_publishers = [
  'NBC - Heroes',
  'SyFy',
  'South Park',
  'ABC Studios',
  'Universal Studios'
]

def make_model(json_dict):

  base_prices = {1: 100, 2: 200, 3: 400, 4: 800, 5: 1600}

  intelligence = json_dict['powerstats']['intelligence']
  strength = json_dict['powerstats']['strength']
  durability = json_dict['powerstats']['durability']
  speed = json_dict['powerstats']['speed']
  combat = json_dict['powerstats']['combat']
  power = json_dict['powerstats']['power']

  overall = int((intelligence + strength + durability + speed + combat + power) / 6)

  if overall >= 90: power_level = 5
  elif 90 > overall >= 70: power_level = 4
  elif 70 > overall >= 50: power_level = 3
  elif 50 > overall >= 30: power_level = 2
  else: power_level = 1

  price = base_prices[power_level] + (5 * choice([intelligence, strength, durability, speed, combat, power]))

  if price >= 2000: price_bracket = 5
  elif 2000 > price >= 1500: price_bracket = 4
  elif 1500 > price >= 1000: price_bracket = 3
  elif 1000 > price >= 500: price_bracket = 2
  else: price_bracket = 1

  new_model = {
    'name': json_dict['name'],
    'image': json_dict['images']['lg'],
    'owner': '',
    'hero': json_dict['id'],
    'intelligence': intelligence,
    'strength': strength,
    'durability': durability,
    'speed': speed,
    'power': power,
    'combat': combat,
    'overall': overall,
    'level': power_level,
    'price': price,
    'price_bracket': price_bracket 
  }

  return new_model


res = request.urlopen('https://cdn.rawgit.com/akabab/superhero-api/0.2.0/api/all.json')
data = json.loads(res.read())
my_list = [make_model(item) for item in data if item['biography']['publisher'] not in banned_publishers]


my_list = sorted(my_list, key=lambda x: x['price'], reverse=True)

loop_counts = {1: 25, 2: 20, 3: 15, 4: 10, 5: 5}

# *** THINK VERY LONG AND HARD BEFORE YOU RUN THIS ***
for model in my_list:
  loop_count = loop_counts[model['level']]
  for i in range(loop_count):
    post_res = requests.post(url = 'http://localhost:8000/api/cards/', data=model)

# with open('card-seeds.json', 'w') as outfile:
#   json.dump(my_list, outfile, indent=2)