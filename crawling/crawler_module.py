from abc import ABC, abstractmethod
from pymongo import MongoClient
import re

class Crawler(ABC):
    crawler_data = []
    #생성자
    def __init__(self):
        uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
        self.client=MongoClient(uri)


    #크롤링
    @abstractmethod
    def crawler_search(self):
        pass

    #모든 크롤링데이터 찾기
    def find_all(self):
        for one in self.crawler_data:
            print("item_id: " + str(one[0]) + "\n" + 
            "title: " + str(one[1]) + "\n" +
            "picture: " + str(one[2]) + "\n" +
            "region: " + str(one[3]) + "\n" +
            "price: " + str(one[4]) + "\n" +
            "link: " + str(one[5]) + "\n" +
            "date" + str(one[6]) + "\n" + 
            "app_name" + str(one[7]) + "\n")
 

    #item_id가져와 찾기
    def find_one(self, item_id):
        for one in len(self.crawler_data):
            if one[0] == item_id:
                return one
            else:
                return 


    #크롤링한 데이터 초기화
    def data_clean(self):
        self.crawler_data = []

    #제외할 데이터 찾기
    def sub_filter(self, title, sub_filter):
        for filter in sub_filter:
            if filter not in title:
                break
        else:
            return True


    #크롤링한 데이터 보내기 
    def serve_data(self):
        db = self.client['UniMarketDB']
        posts=db['data']
        for tmp in self.crawler_data:
            post={"item_id":str(tmp[0]),
                "title":str(tmp[1]),
                "picture":str(tmp[2]),
                "region":str(tmp[3]),
                "price":int(tmp[4]),
                "link":str(tmp[5]),
                "description":str(tmp[6]),
                "date":str(tmp[7]),
                "seller_info":str(tmp[8]),
                "app_name":str(tmp[9])}

            post_id=posts.insert_one(post).inserted_id
        
        
        db.list_collection_names()

    #가격 통합 함수
    def price_filtering(self, price):
        try:
            if '백' in price:
                price = price.replace('백', "00")

            if '만' in price:
                price = price.replace('만', "0000")

            if '천' in price:
                price = price.replace('천', "000")
            
            if ',' in price:
                price = price.replace(',','')

            if '원' in price:
                price = price.replace('원','')
            
            if ' ' in price:
                price = price.replace(' ', '')

            price = re.sub(r"[^0-9]", "", price)
            
        except:
            price = -1
        return int(price)