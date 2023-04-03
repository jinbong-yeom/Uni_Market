from flask import Flask, make_response, jsonify, request, make_response
from send import *
from search import *
from monitor import *
from deletedata import *
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/post",methods=['POST'])
def post():
    params = request.get_json()
    print(params)
    user=params['userId']
    title = params['title']
    Max=params['filteringData']['maxPrice']
    Min=params['filteringData']['minPrice']
    Filter=params['filteringData']['excludeKeyword']
    region=params['filteringData']['region']
    result = search(user,title,Max,Min,Filter[0],region[0])
    return {"result":result}

@app.route("/notice",methods=['POST'])
def notice():
    params = request.get_json()
    print(params)
    user=params['userId']
    firebaseid=params['firebaseId']
    title = params['title']
    Max=params['filteringData']['maxPrice']
    Min=params['filteringData']['minPrice']
    Filter=params['filteringData']['excludeKeyword']
    region=params['filteringData']['region']
    
    db=client['UniMarketDB']
    collection=db['data']
    collection2=db['{}'.format(user)]
    print('새 콜렉션 만들기')
    collection3=db['UserDB']
    post={"user_id":str(user),
    "firebase_id":str(firebaseid),
                "title":str(title),
                "max_price":int(Max),
                "min_price":int(Min),
                "filter_keyword":str(Filter[0]),
                "region":str(region[0])}
    name=[]
    for i in collection3.find():
        name.append(i['user_id'])
    if post['user_id'] not in name:
        print('새 콜렉션 데이터 넣기')
        collection3.insert_one(post)
    
    print(Filter[0], "dsd ")
    print(region[0], "dsdfdsf")
    for i in collection.find({'$and':[{'$and':[{"price":{"$lte":Max}},
    {"price":{"$gte":Min}},{"title":{"$regex":".*{}.*".format(title)}},
    {"region":{"$regex":".*{}.*".format(region[0])}}]},
    {'$nor':[{"title":{"$regex":".*{}.*".format(Filter[0])}}]}]}):
        user_post= {"item_id":i["item_id"]}
        print(user_post['item_id'])
        collection2.insert_one(user_post)
    
    print('모니터링 시작')
    thread = Thread(target=monitor, daemon=True)
    thread.start()
    return {"Success": True}

@app.route("/delete",methods=['POST'])
def delete():
    params = request.get_json()
    User = params['userId']
    event.set()
    deletedata(User)
    return {"Success": True}

if __name__ == '__main__':
    uri = " " % (
                ' ', ' ', ' ')
    client=MongoClient(uri)
    app.run(host='0.0.0.0', port=60000)
