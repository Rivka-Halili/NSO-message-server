# REST API with Flask, Flask-RESTful and SQLite.

## Description:
Simple RESTFul Flask application (still in development) with bunch of automated API tests. Main reason for developing this app is writing automated tests against exposed endpoints (with usage of Python requests library, Postman (form manual testing) and REST Assured (Java) in the near future).

So far active endpoints are:

GET /message/1 

DELETE /message/1 no such table: message

GET /messages 

GET /messages?application_id=100

DELETE /messages?application_id=100

GET /messages?session_id=200

DELETE /messages?session_id=200

POST /message/add
