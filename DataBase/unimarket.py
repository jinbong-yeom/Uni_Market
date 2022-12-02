from pymongo import MongoClient

uri = "" % (
                '', '', '')
client=MongoClient(uri)

db=client['UniMarketDB']
collection=db['data']
sanghan=300000
hahan=0
title="갤럭시"
one="S21"
two="S7"
three="무고"
for i in collection.find({'$and':[{'$and':[{"price":{"$lte":sanghan}},{"price":{"$gte":hahan}},
{"title":{"$regex":".*{}.*".format(title)}}]},{'$nor':[{"title":{"$regex":".*{}.*".format(one)}},
{"title":{"$regex":".*{}.*".format(two)}},{"title":{"$regex":".*{}.*".format(three)}}]}]}).sort("price"):
      print(i)