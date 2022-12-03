import firebase_admin
import os
from firebase_admin import credentials
from firebase_admin import messaging

current_path = os.getcwd()
cred_path = current_path+"/DataBase/unimarket_firebase.json"
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

registration_token = 'ezSibjEnST-q8tmlTFN8-m:APA91bFCqcW3lqnShBJjyzYS_ozAMTUC99IPGaix26pBsGSdAGG2qCldwCE7EoAVZdvzilJfGvm72JzlFipcQlvnNwGstQ005LZ3UM4p26N5Xn2t4b-9hSP-js0DgqGp0rH4JPqvbQxK'
message = messaging.Message(
    notification = messaging.Notification(
        title='title',
        body='되나'
    ),
    token=registration_token,
)

response = messaging.send(message)
print('Successfully sent message:', response)