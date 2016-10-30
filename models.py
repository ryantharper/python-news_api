import requests, json
#from api import load_news


class News(object):

    def __init__(self, json, articleNum):
        self.json = json
        self.articleNum = articleNum

    def titles(self):
        if self.json['status'] == "ok":
            return [self.json['articles'][i]['title'] for i in range(self.articleNum)]
        else:
            return self.json['message']

    def desc(self):
        if self.json['status'] == "ok":
            return [self.json['articles'][i]['description'] for i in range(self.articleNum)]
        else:
            return self.json['message']
    def link(self):
        if self.json['status'] == "ok":
            return [self.json['articles'][i]['url'] for i in range(self.articleNum)]
        else:
            return self.json['message']

    def titles_desc(self):
        if self.json['status'] == "ok":
            return {self.json['articles'][i]['title']: self.json['articles'][i]['description'] for i in range(self.articleNum)}
        else:
            return self.json['message']

    def titles_url(self):
        if self.json['status'] == "ok":
            return {self.json['articles'][i]['title']: self.json['articles'][i]['url'] for i in range(self.articleNum)}
        else:
            return self.json['message']
