from pymongo import MongoClient 
import json
uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
client=MongoClient(uri)

def search(title,Max,Min,Filter,region):
      
      db=client['UniMarketDB']
      collection=db['data']
      item_id=[]# 기존 item_id
      result=[]
      for i in collection.find():
            item_id.append(i['item_id'])
      with open('/server/item_id_list.txt','w',encoding='UTF-8')as f:
            for name in item_id:
                  f.write(name+'\n')
      
      for i in collection.find({'$and':[{'$and':[{"price":{"$lte":Max}},{"price":{"$gte":Min}},
      {"title":{"$regex":".*{}.*".format(title)}}]},{'$nor':[{"title":{"$regex":".*{}.*".format(Filter)}},
      {"region":{"$regex":".*{}.*".format(region)}}]}]}).sort("price"):
            temp_dict = {'title': i['title'], 
                  'picture': i['picture'], 
                  'region': i['region'],
                  'price': i['price'], 
                  'link':i['link'], 
                  'app_name': i['app_name'], 
                  'description': i['description'],
                  'date': i['date'],
                  'seller_info': i['seller_info']
                  }
            result.append(temp_dict)
      print(result)
      return result