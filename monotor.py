from pymongo import MongoClient 
import json
uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
client=MongoClient(uri)

db=client['UniMarketDB']
collection=db['data']
data=[]
f=open('./item_id_list.txt','r')
while True:
    line=f.readline().rstrip()
    if not line:break
    data.append(line)
for i in collection.find():#갱신된 부분이 있는지 확인
      if i['item_id'] not in data:
            print('알림')
            # 알림 보내기