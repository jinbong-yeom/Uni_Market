from abc import *

class Crawler(metaClass=ABCMeta):
    crawler_data = {}

    def __init__(self):
        self.crawler_data = {'picture': [],
            'title': [],
            'Region': [],
            'Price': [],
            'Link': []}

    @abstractmethod
    def crawler_search():
        pass
