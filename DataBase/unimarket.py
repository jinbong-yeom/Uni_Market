from pymongo import MongoClient
import json

def DB_find(word):
      uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
            'uni', 'uni1234', 'db.yoonleeverse.com')

      client=MongoClient(uri)
      db=client['UniMarketDB']

      send_list = []

      myquery = { "title": { "$regex": ".*{}.*".format(word) }}
      posts = db.data.find(myquery)
      
      for post in posts:
            temp_dict = {'title': post['title'], 'picture': post['picture'], 'region': post['region'], 'price': post['price'], 'link':post['link'], 'app_name': post['app_name']}
            send_list.append(temp_dict)
      
      dataNotFound = "dataNotFound"
      if send_list == []:
            return dataNotFound
      return send_list
