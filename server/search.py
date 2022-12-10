from pymongo import MongoClient 
import json
import os
uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
client=MongoClient(uri)
def search(user,title,Max,Min,Filter,region):
      db=client['UniMarketDB']
      collection=db['data']
      send_list=[]  
      if Filter=='':
            for post in collection.find({'$and':[{"price":{"$lte":Max}},{"price":{"$gte":Min}},
            {"title":{"$regex":".*{}.*".format(title)}},{"region":{"$regex":".*{}.*".format(region[0])}}]}).sort("price"):
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
      else:
            for post in collection.find({'$and':[{'$and':[{"price":{"$lte":Max}},{"price":{"$gte":Min}},
            {"title":{"$regex":".*{}.*".format(title)}},{"region":{"$regex":".*{}.*".format(region[0])}}]},
            {'$nor':[{"title":{"$regex":".*{}.*".format(Filter[0])}}]}]}).sort("price"):
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
