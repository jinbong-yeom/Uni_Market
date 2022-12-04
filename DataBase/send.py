import firebase_admin
import os
from firebase_admin import credentials
from firebase_admin import messaging

def send(token):
    current_path = os.getcwd()
    cred_path = current_path+"/DataBase/unimarket_firebase.json"
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

    registration_token = token
    message = messaging.Message(
        notification = messaging.Notification(
            title='title',
            body='되나'
        ),
        token=registration_token,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)

    