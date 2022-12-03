from pymongo import MongoClient 
import json
uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
client=MongoClient(uri)
def search(title,Max,Min,Filter):
      db=client['UniMarketDB']
      collection=db['data']
      item_id=[]# 기존 item_id
      result=[]
      for i in collection.find():
            item_id.append(i['item_id'])
      with open('item_id_list.txt','w',encoding='UTF-8')as f:
            for name in item_id:
                  f.write(name+'\n')
      for i in collection.find({'$and':[{'$and':[{"price":{"$lte":Max}},{"price":{"$gte":Min}},
      {"title":{"$regex":".*{}.*".format(title)}}]},{'$nor':[{"title":{"$regex":".*{}.*".format(Filter)}}]}]}).sort("price"):
            result.append(i)
      print(result)
      return result