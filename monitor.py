from pymongo import MongoClient 
import json 
from threading import Thread
import time
uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
client=MongoClient(uri)
def monitor(user,title,Max,Min,Filter,region):
    db=client['UniMarketDB']
    collection=db['data']
    data=[]
    f=open('./item_id_list.txt','r')
    while True:
        line=f.readline().rstrip()
        if not line:break
        data.append(line)
    for i in collection.find({'$and':[{'$and':[{"price":{"$lte":Max}},{"price":{"$gte":Min}},
    {"title":{"$regex":".*{}.*".format(title)}}]},{'$nor':[{"title":{"$regex":".*{}.*".format(Filter)}},
    {"region":{"$regex":".*{}.*".format(region)}}]}]}):#갱신된 부분이 있는지 확인
        if i['item_id'] not in data:
                print('알림')
                # 알림 보내기
                with open('item_id_list.txt','a',encoding='UTF-8')as f:#알림 보내고 리스트 파일 갱신
                    f.write(i['item_id']+'\n')
#if 모니터링 요청이 오면: 
thread = Thread(target=monitor, args=(), daemon=True)
thread.start()
time.sleep(3)