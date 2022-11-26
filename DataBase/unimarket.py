from pymongo import MongoClient

uri = "" % (
                '', '', '')
client=MongoClient(uri)
db=client['onlineJudgeDB']
collection=db['data']
posts=db.data
for i in posts.find():
      print(i)