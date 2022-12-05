from flask import Flask, make_response, jsonify, request, make_response
from unimarket import *
from send import send
import json
import time

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/posts/207092540')
def hello():
    test = {'userId': '207092540'}
    data = json.dumps(test, ensure_ascii=False).encode('utf8')
    
    return data


@app.route("/post",methods=['POST'])
def post():
    params = request.get_json()
    print(params['region'][0])
    word = params['title']
    result = DB_find(word)
    print(result)
    return {"result": result}

@app.route("/notice",methods=['POST'])
def notice():
    params = request.get_json()
    print(params['userId'],end='\n')
    word = params['title']
    result = DB_find(word)
    time.sleep(10)
    send(params['userId'])
    print(result)
    return {"result": result}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60000)