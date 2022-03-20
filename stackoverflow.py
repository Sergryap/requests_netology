import requests
import json
import datetime as dtm


def get_dates():
    """Находит даты в секундах с начала вчерашнего дня по текущее время"""
    dt = dtm.datetime.today()
    second_now = int(dt.timestamp())
    second_yesterday = second_now - 86400
    second_yesterday -= second_yesterday % 86400
    return second_yesterday, second_now


def out_questions(url: str, par: dict):
    """Вывод вопросов"""
    res = requests.get(url, params=par)
    for item in res.json()['items']:
        print(item['title'])


if __name__ == '__main__':
    URL = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': get_dates()[0], 'todate': get_dates()[1], 'order': 'desc', 'sort': 'votes',
              'tagged': 'Python',
              'site': 'stackoverflow'}
    out_questions(URL, params)
