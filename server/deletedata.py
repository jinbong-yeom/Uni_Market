from pymongo import MongoClient 
import json
import os
uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
client=MongoClient(uri)
def deletedata(user):
      db=client['UniMarketDB']
      collection=db['UserDB']
      collection2=db["{}".format(str(user))]
      collection2.drop()
      collection.delete_one({"userId":{"$regex":".*{}.*".format(str(user))}})


