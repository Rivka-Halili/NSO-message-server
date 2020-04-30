# NSO-message-server
api with flask using pytest and sqlite

for active endpoints are:

GET /message/1

DELETE /message/1 

GET /messages 

GET /messages?application_id=100

DELETE /messages?application_id=100

GET /messages?session_id=200

DELETE /messages?session_id=200

POST /message/add


pre requirements

to run this application install:

*python3

*virtul environment

*sqlite

and for the run test you need also 

*pytest

to run the tests run the server by  app.py in the background

and than from the command prompt on the tests directory

 run python -q messagetests.py





