import requests
import json

def get_json(FILE_PATCH):
    with open(FILE_PATCH, encoding='utf-8') as f:
        return json.load(f)



if __name__ == '__main__':
    API_PATCH = "https://superheroapi.com/api/2619421814940190/search/name"
    # API_PATCH = "https://superheroapi.com/api/2619421814940190/search/name"

    response = requests.get(API_PATCH)

    print(response.json())




