from pymongo import MongoClient

uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')

client=MongoClient(uri)
db=client['UniMarketDB']

myquery = { "title": { "$regex": ".*노트북.*" }}
posts=db.data.find(myquery)

for i in posts:
      print(i)
