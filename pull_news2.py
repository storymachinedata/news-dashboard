
import requests

api_key = 'ebaa63cf9dfa430d8f20bb9f7726ed03'

from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key=api_key)


def pull_news(country):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'  
    r = requests.get(url).json()['articles']
    if len(r) > 0:
        return r
    return 'Unfortunately no news found'

def get_news(country):
    news = pull_news(country)
    news = [(n['title'],n['description'],n['publishedAt'],n['url']) for n in news]
    return news

