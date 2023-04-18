from pymongo import MongoClient 
import json
import os
        uri = " " % (
                ' ', ' ', ' ')
client=MongoClient(uri)
def deletedata(user):
      db=client['UniMarketDB']
      collection=db['UserDB']
      collection2=db["{}".format(user)]
      collection2.drop()
      collection.delete_one({"user_id":user})


