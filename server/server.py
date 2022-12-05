from flask import Flask, make_response, jsonify, request, make_response
from server.search import *
from server.monitor import *
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
    print(result)
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
    result = monitor(user,title,Max,Min,Filter,region)
    print(result)
    return {"Success": True}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60000)