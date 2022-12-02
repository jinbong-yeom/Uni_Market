from flask import Flask, make_response, jsonify, request, make_response
import json
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/posts/207092540')
def hello():
    test = {'userId': '207092540'}
    data = json.dumps(test, ensure_ascii=False).encode('utf8')
    
    return data
"""
@app.route('/posts/<param>') 
def get_echo_call(param):
    test = {'user_id': '207092540', 'title': 'rc420 i5 2410M/4g/ssd120 노트북 팝니다', 'picture': 'https://media.bunjang.co.kr/product/207092540_1_1669880604_w{res}.jpg', 'region': '', 'price': 105000, 'link': 'https://m.bunjang.co.kr/products/207092540', 'description': 'rc420  14인치\n\ni5 2410m \n\nssd120g(새상품)/cd롬 \n\n인텔HD그래픽 3000\n\n\n구성품: 본체 + 어댑터 \n\n윈도우10 오피스 한글 설치 및 인증되어있고 액정,외관 파손없이 양호하고 상태좋습니다.\n배터리는 완충시 2시간정도이고 사용환경에따라 다를수있네요.\n\n사무용 인강용 인터넷용 매장용 등 사용하시기에 가성비 좋을거라 생각됩니다. 직거래는 마산 월영동이고 그외지역은 안전하게 포장해서 택배발송가능합니다 \n서로에게 소중시간이니만큼 신중히 고민하시고 꼭 구매하실분만 연락바랍니다', 'date': '2022-12-01', 'seller_info': '9', 'app_name': '번개'}
    if test['user_id'] == param:
        return jsonify(test)
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=60000)