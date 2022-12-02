from pymongo import MongoClient 
import json 
import time
while(1):
    uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                    'uni', 'uni1234', 'db.yoonleeverse.com')
    client=MongoClient(uri)

    db=client['UniMarketDB']
    collection=db['data']
    data=[]
    sanghan=300000
    hahan=0
    title="갤럭시"
    one="S21"
    two="S7"
    three="무고"
    f=open('./item_id_list.txt','r')
    while True:
        line=f.readline().rstrip()
        if not line:break
        data.append(line)
    for i in collection.find({'$and':[{'$and':[{"price":{"$lte":sanghan}},{"price":{"$gte":hahan}},
    {"title":{"$regex":".*{}.*".format(title)}}]},{'$nor':[{"title":{"$regex":".*{}.*".format(one)}},
    {"title":{"$regex":".*{}.*".format(two)}},{"title":{"$regex":".*{}.*".format(three)}}]}]}):#갱신된 부분이 있는지 확인
        if i['item_id'] not in data:
                print('알림')
                # 알림 보내기
    time.sleep(5)