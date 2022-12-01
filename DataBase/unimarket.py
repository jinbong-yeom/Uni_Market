from pymongo import MongoClient

uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')

client=MongoClient(uri)
db=client['UniMarketDB']
collection=db['data']
posts=db.data.find()
for i in posts:
      print(i)
