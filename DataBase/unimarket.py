from pymongo import MongoClient
client=MongoClient(host='localhost',port=27017)
db=client['UniMarketDB']
collection=db['data']
posts=db.data.find()
posts.sort()
for i in posts:
      print(i)
