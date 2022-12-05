from flask import Flask, make_response, jsonify, request, make_response
from send import *
from search import *
from monitor import *
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/post",methods=['POST'])
def post():
    params = request.get_json()
    print(params)
    title = params['title']
    Max=params['filteringData']['maxPrice']
    Min=params['filteringData']['minPrice']
    Filter=params['filteringData']['excludeKeyword']
    region=params['filteringData']['region']
    result = search(title,Max,Min,Filter,region)
    return {"result":result}

@app.route("/notice",methods=['POST'])
def notice():
    params = request.get_json()
    print(params)
    user=params['userId']
    title = params['title']
    Max=params['filteringData']['maxPrice']
    Min=params['filteringData']['minPrice']
    Filter=params['filteringData']['excludeKeyword']
    region=params['filteringData']['region']

    db=client['UniMarketDB']
    collection=db['monitor']
    post={"user_id":str(user),
                "title":str(title),
                "max_price":int(Max),
                "min_price":int(Min),
                "filter_keyword":str(Filter),
                "region":str(region)}
    post_id=collection.insert_one(post).inserted_id


    return {"Success": True}

if __name__ == '__main__':
    uri = "mongodb://%s:%s@%s/?authMechanism=DEFAULT&authSource=UniMarketDB" % (
                    'uni', 'uni1234', 'db.yoonleeverse.com')
    client=MongoClient(uri)

    app.run(host='0.0.0.0', port=60000)