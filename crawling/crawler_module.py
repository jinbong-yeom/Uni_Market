from abc import ABC, abstractmethod
from pymongo import MongoClient


class Crawler(ABC):
    crawler_data = []

    #생성자
    def __init__(self):
        super().__init__()


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
            "link: " + str(one[5]) + "\n")
 

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



    #크롤링한 데이터 보내기 
    def serve_data(self):
        client = MongoClient(host='localhost',port=27017)
        db = client['UniMarketDB']
        collection=db['data']
        for tmp in self.crawler_data:
            post={"item_id":str(tmp[0]),
                "title":str(tmp[1]),
                "picture":str(tmp[2]),
                "region":str(tmp[3]),
                "price":str(tmp[4]),
                "link":str(tmp[5])}
            posts=db.data
            post_id=posts.insert_one(post).inserted_id
        
        
        db.list_collection_names()


"""   #최저가 찾기
    def find_smallest_price(self):
        pass
"""

