import json, requests
from news_api.models import News
# sort - top|latest|popular
# https://newsapi.org/v1/articles?sources=%s&apiKey=%s % (source, newsKey)

srcs = ['abc-news-au','ars-technica','associated-press','bbc-news',
        'bbc-sport','bild','bloomberg','business-insider',
        'business-insider-uk','buzzfeed','cnbc','cnn',
        'daily-mail','engadget','entertainment-weekly','espn',
        'espn-cric-info','financial-times','focus','football-italia',
        'fortune','four-four-two','fox-sports','google-news',
        'gruenderszene','hacker-news','ign','independent',
        'mashable','metro','mirror','mtv-news',
        'mtv-news-uk','national-geographic','new-scientist','newskweek',
        'new-york-magazine','nfl-news','polygon','recode',
        'reddit-r-all','reuters','sky-news','sky-sports-news',
        'spiegel-online','t3n','talksport','techcrunch',
        'techradar','the-economist','the-guardian-au','the-guardian-uk',
        'the-hindu','the-huffington-post','the-lad-bible','the-new-york-times',
        'the-next-web','the-sport-bible','the-telegraph','the-times-of-india',
        'the-verge','the-wall-street-journal','the-washington-post','time',
        'usa-today','wired-de']

def load_news(key, source, sort, n):

    if sort is None:
        if source not in srcs:
            url = 'https://newsapi.org/v1/articles?source=%s&apiKey=%s' % ('bbc-news', key)
        else:
            url = 'https://newsapi.org/v1/articles?source=%s&apiKey=%s' % (source, key)
    else:
        if source not in srcs:
            url = 'https://newsapi.org/v1/articles?source=%s&apiKey=%s&sortBy=%s' % ('bbc-news', key, sort)
        else:
            url = 'https://newsapi.org/v1/articles?source=%s&apiKey=%s&sortBy=%s' % (source, key, sort)

    news_json = requests.get(url).json()
    return News(news_json, n)
