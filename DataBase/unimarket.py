from pymongo import MongoClient
client=MongoClient(host='localhost',port=27017)
print(client.list_database_names())
db=client['test']
collection=db['data']
posts=db.data
db.list_collection_names()
import pprint
for i in posts:
      pprint.pprint(i.find_one())
