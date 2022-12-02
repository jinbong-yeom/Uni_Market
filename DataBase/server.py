from flask import Flask, make_response, jsonify, request, make_response
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
	value = request.form['input']
	msg = "%s 님 환영합니다." %value
	return msg


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60000)