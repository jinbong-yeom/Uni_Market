from pymongo import MongoClient

uri = "" % (
                '', '', '')
client=MongoClient(uri)
db=client['UniMarketDB']
collection=db['data']
sanghan=300000
hahan=100000
title="아이폰"
for i in collection.find({'$and':[{"price":{"$lte":sanghan}},{"price":{"$gte":hahan}},
{"title":{"$regex":".*{}.*".format(title)}}]}).sort("price"):
      print(i)