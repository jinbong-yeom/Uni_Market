from pymongo import MongoClient 
import json
import os
uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
client=MongoClient(uri)
def deletedata(user,title,Max,Min,Filter,region):
      db=client['UniMarketDB']
      collection=db['data']