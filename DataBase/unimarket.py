from pymongo import MongoClient

uri = "" % (
                '', '', '')
client=MongoClient(uri)
db=client['UniMarketDB']
collection=db['data']
sanghan=400000
hahan=100000
for i in collection.find({"price":{"$lt":sanghan},"price":{"$gt":hahan}}).sort("price"):
      print(i)