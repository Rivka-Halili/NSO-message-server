import requests
import json


def test_get_message_messageid_return_message():
     response = requests.get("http://127.0.0.1:5000/message/1 ")
     assert response.status_code == 200

def test_get_all_messages():
     response = requests.get("http://127.0.0.1:5000/messages")
     assert response.status_code == 200

def test_get_messages_by_appid_return_message_list():
     response = requests.get("http://127.0.0.1:5000/messages?application_id=100")
     assert response.status_code == 200

def test_get_messages_by_sessionid_return_message_list():
     response = requests.get("http://127.0.0.1:5000/messages?session_id=200")
     assert response.status_code == 200

def test_post_new_message_is_created():
     response = requests.post("http://127.0.0.1:5000/message/add", data=json.dumps({"message_id": "20",
 "application_id": "150","session_id": "250","participants": "150","content": "150"}))
     assert response.status_code == 200

def test_delete_message_by_messageid_is_deleted():
     response = requests.delete("http://127.0.0.1:5000/message/1")
     assert response.status_code == 200 
     
def test_delete_messages_by_appid_is_deleted():
     response = requests.delete("http://127.0.0.1:5000/messages?application_id=100")
     assert response.status_code == 200

def test_delete_message_by_sessionid_is_deleted():
     response = requests.delete("http://127.0.0.1:5000/messages?session_id=100")
     assert response.status_code == 200

