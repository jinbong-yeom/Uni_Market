from pymongo import MongoClient 
import json

uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
client=MongoClient(uri)

db=client['UniMarketDB']
collection=db['data']
sanghan=300000
hahan=0
title="갤럭시"
one="S21"
two="S7"
three="무고"
item_id=[]# 기존 item_id
for i in collection.find():
      item_id.append(i['item_id'])
      
for i in collection.find():#갱신된 부분이 있는지 확인
      if i['item_id'] not in item_id:
            print('알림')
            # 알림 보내기
for i in collection.find({'$and':[{'$and':[{"price":{"$lte":sanghan}},{"price":{"$gte":hahan}},
{"title":{"$regex":".*{}.*".format(title)}}]},{'$nor':[{"title":{"$regex":".*{}.*".format(one)}},
{"title":{"$regex":".*{}.*".format(two)}},{"title":{"$regex":".*{}.*".format(three)}}]}]}).sort("price"):
      print(i)