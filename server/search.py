from pymongo import MongoClient 
import json
import os
uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
client=MongoClient(uri)
def search(title,Max,Min,Filter,region):
      db=client['UniMarketDB']
      collection=db['data']
      item_id=[]# 기존 item_id
      send_list=[]
      current_path = os.getcwd()
      cred_path = current_path+"/server/item_id_list.txt"
      
      for i in collection.find():
            item_id.append(i['item_id'])
      with open(cred_path,'w',encoding='UTF-8')as f:
            for name in item_id:
                  f.write(name+'\n')
      for post in collection.find({'$and':[{'$and':[{"price":{"$lte":Max}},{"price":{"$gte":Min}},
      {"title":{"$regex":".*{}.*".format(title)}}]},{'$nor':[{"title":{"$regex":".*{}.*".format(Filter[0])}},
      {"region":{"$regex":".*{}.*".format(region[0])}}]}]}).sort("price"):
            temp_dict = {'title': post['title'], 
            'picture': post['picture'], 
            'region': post['region'],
            'price': post['price'], 
            'link':post['link'], 
            'app_name': post['app_name'], 
            'description': post['description'],
            'date': post['date'],
            'seller_info': post['seller_info']
            }
            send_list.append(temp_dict)
      print(send_list)
      return send_list