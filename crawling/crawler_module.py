from abc import *

class Crawler(metaClass=ABCMeta):
    crawler_data = []

    #생성자
    @abstractmethod
    def __init__(self):
        self.crawler_data = []

    #크롤링
    @abstractmethod
    def crawler_search(self):
        pass

    #모든 크롤링데이터 찾기
    @abstractmethod
    def find_all(self):
        pass

    #item_id가져와 찾기
    @abstractmethod
    def find_one(self, item_id):
        pass

    #최저가 찾기
    @abstractmethod
    def find_smallest_price(self):
        pass
    
    #크롤링한 데이터 초기화
    @abstractmethod
    def data_clean(self):
        pass

    #크롤링한 데이터 보내기
    @abstractmethod
    def serve_data(self):
        pass