import pymongo
from pymongo import MongoClient
client=MongoClient(host='localhost',port=27017)
print(client.list_database_names())
db=client['UniMarketDB']
collection=db['data']
post={"item_id":"0125475",
      "title":"노트북",
      "picture":" ",
      "region":" ",
      "price":" ",
      "link":" "}
post
posts=db.data
post_id=posts.insert_one(post).inserted_id
print(post_id)
db.list_collection_names()
import pprint
pprint.pprint(posts.find_one())
