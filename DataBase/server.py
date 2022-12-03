from flask import Flask, make_response, jsonify, request, make_response
from unimarket import *
import json

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
    filteringData = params['filteringData']['excludeKeyword']
    for i in filteringData:
        if filteringData == []:
            print("없음")
            break
        else:
            print(i)


    word = params['title']
    result = DB_find(word)
    print(result)
    return {"result": result}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60000)