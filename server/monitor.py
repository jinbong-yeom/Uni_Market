from pymongo import MongoClient 
import json 
from threading import Thread
import time
import send as send
import os
uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
client=MongoClient(uri)
def monitor(user,title,Max,Min,Filter,region):
    db=client['UniMarketDB']
    collection=db['data']
    monitor_collection=db["{}".format(user)]
    data=[]
    for i in monitor_collection.find():
        data.append(i)
    for i in collection.find({'$and':[{'$and':[{"price":{"$lte":Max}},{"price":{"$gte":Min}},
    {"title":{"$regex":".*{}.*".format(title)}}]},{'$nor':[{"title":{"$regex":".*{}.*".format(Filter)}},
    {"region":{"$regex":".*{}.*".format(region)}}]}]}):#갱신된 부분이 있는지 확인
        if i['item_id'] not in data:
                send(user,i['title'])
                # 알림 보내기
                monitor_collection.insert_one(i['item_id'])