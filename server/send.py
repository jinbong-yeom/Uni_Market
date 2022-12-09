import firebase_admin
import os
from firebase_admin import credentials
from firebase_admin import messaging
def send(token):
    
    current_path = os.getcwd()
    cred_path = current_path+"/unimarket_firebase.json"
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

    registration_token = token
    message = messaging.Message(
        notification = messaging.Notification(
            name="새로운 매물이 등록되었습니다.",
            body='앱에서 다시 검색하여 확인하세요!'
        ),
        token=registration_token,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)