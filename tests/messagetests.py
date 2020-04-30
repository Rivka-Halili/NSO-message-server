import requests
import json


def test_get_signle_message():
     response = requests.get("http://127.0.0.1:5000/message/1 ")
     assert response.status_code == 200

def test_get_all_messages():
     response = requests.get("http://127.0.0.1:5000/messages")
     assert response.status_code == 200

def test_get_messages_by_app():
     response = requests.get("http://127.0.0.1:5000/messages?application_id=100")
     assert response.status_code == 200

def test_get_messages_by_session():
     response = requests.get("http://127.0.0.1:5000/messages?session_id=200")
     assert response.status_code == 200

def test_post_message():
     response = requests.post("http://127.0.0.1:5000/message/add", data=json.dumps({
"message_id": "200",
 "application_id": "150",
 "session_id": "250",
 "participants": "150",
 "content": "150"}))
     assert response.status_code == 200

def test_delete_signle_message():
     response = requests.delete("http://127.0.0.1:5000/message/1")
     assert response.status_code == 200 
     
def test_delete_messages_by_app():
     response = requests.delete("http://127.0.0.1:5000/messages?application_id=100")
     assert response.status_code == 200

def test_delete_messages_by_session():
     response = requests.delete("http://127.0.0.1:5000/messages?session_id=100")
     assert response.status_code == 200
