from pymongo import MongoClient 
import json 
from threading import Thread
uri = "" % (
                    '', '', '')
client=MongoClient(uri)
def monitor(instance):
    db=client['UniMarketDB']
    collection=db['data']
    data=[]
    sanghan=300000
    hahan=0
    title="갤럭시"
    one="S21"
    two="사고"
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
                with open('item_id_list.txt','a',encoding='UTF-8')as f:#알림 보내고 리스트 파일 갱신
                    f.write(i['item_id']+'\n')
#if 모니터링 요청이 오면: 
thread = Thread(target=monitor, args=(), daemon=True)
thread.start()
