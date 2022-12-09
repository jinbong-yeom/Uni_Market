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
    result = search(user,title,Max,Min,Filter,region)
    return {"result":result}

@app.route("/notice",methods=['POST'])
def notice():
    params = request.get_json()
    print(params)
    user=params['userId']
    firebaseid=params['firebase_id']
    title = params['title']
    Max=params['filteringData']['maxPrice']
    Min=params['filteringData']['minPrice']
    Filter=params['filteringData']['excludeKeyword']
    region=params['filteringData']['region']

    db=client['UniMarketDB']
    collection=db['data']
    collection2=db["{}".format(user)]
    collection3=db['UserDB']
    post={"user_id":str(user),
    "firebase_id":str(firebaseid),
                "title":str(title),
                "max_price":int(Max),
                "min_price":int(Min),
                "filter_keyword":str(Filter),
                "region":str(region)}
    name=[]
    for i in collection3.find():
        name.append(i['userId'])
    if post['user_id'] not in name:
        collection3.insert_one(post)

    for i in collection.find({'$and':[{'$and':[{"price":{"$lte":Max}},
    {"price":{"$gte":Min}},{"title":{"$regex":".*{}.*".format(title)}},
    {"region":{"$regex":".*{}.*".format(region)}}]},
    {'$nor':[{"title":{"$regex":".*{}.*".format(Filter)}}]}]}):
        collection2.insert_one(i['item_id'])



    return {"Success": True}

@app.route("/delete",methods=['POST'])
def delete():
    params = request.get_json()
    User = params['userId']
    deletedata(User)

if __name__ == '__main__':
    uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                'uni', 'uni1234', 'db.yoonleeverse.com')
    client=MongoClient(uri)
    app.run(host='0.0.0.0', port=60000)

    thread = Thread(target=monitor, daemon=True)
    thread.start()
