import requests
import json


def get_id(her: list):
    """Нахождение id героев"""
    ids = []
    for hero in her:
        url = f"https://superheroapi.com/api/2619421814940190/search/{hero}"
        response = requests.get(url)
        ids.append(response.json()['results'][0]['id'])
    return ids


def find_smart(hero: tuple):
    """Определение самого умного героя"""
    heroes_id = get_id(hero)
    iq = 0
    for i in heroes_id:
        url = f"https://superheroapi.com/api/2619421814940190/{i}/powerstats"
        response = requests.get(url)
        data_res = response.json()
        intell = int(data_res['intelligence'])
        if intell > iq:
            iq = intell
            hero = data_res['name']
    return f"Самый умный герой '{hero}'"


if __name__ == '__main__':
    heroes = ('Hulk', 'Captain America', 'Thanos')
    print(find_smart(heroes))
