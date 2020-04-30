from models.message import MessageModel
from flask_restful import Resource, reqparse

class Message(Resource):
    def get(self, id):
        messages = MessageModel.find_by_message_id(id)
        if messages:
           return {'messages': messages.json()}, 200
        return {'message': 'Message not found!'}, 404

    def delete(self, id):
        if MessageModel.find_by_message_id(id):
           message = MessageModel.delete_by_message_id(id)
           return {'message': 'Message was successfully deleted from database!'},200
        return {'message': 'There is no message with this id'},404


class MessageList(Resource):
    def get(self):
        messages=[]
        args=reqparse.request.args
        if args:
            if  'application_id' in args:
                messages= MessageModel.find_by_app_id(args['application_id'])
            elif 'session_id' in args:
                 messages = MessageModel.find_by_session_id(args['session_id'])
            else:
                  return {'method not allowed': 'this url is not exists'}, 404
        else:
              messages = MessageModel.find_all()
        if messages:
            return {'message': [message.json() for message in messages]}, 200
        return {'message': 'No messages found!'}, 404


    def delete(self):
        args=reqparse.request.args
        if args:
            if  'application_id' in args:
               messages = MessageModel.delete_by_app_id(args['application_id'])
            elif 'session_id' in args:
                 messages = MessageModel.delete_by_session_id(args['session_id'])
            else:
                 return {'Not Found': 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again'}, 404
            return {'message': 'Messages was successfully deleted from database!'} ,200
        return {'Not Found': 'The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again'}, 404

class MessageRegister(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message_id',
                            type=int,
                            required=True,
                            help='This field is required!')
        parser.add_argument('application_id',
                            type=int,
                            required=True,
                            help='This field is required!')
        parser.add_argument('session_id',
                            type=int,
                            required=True,
                            help='This field is required!')
        parser.add_argument('participants',
                            type=str,
                            required=True,
                            help='This field is required!')
        parser.add_argument('content',
                            type=str,
                            required=True,
                            help='This field is required!')

        data_payload = parser.parse_args()

        if MessageModel.find_by_message_id(data_payload['message_id']):
            return {'message': 'Message with the same id already exists in database!'}, 400
        else:
            MessageModel.insert_into_table(data_payload['message_id'],
                                        data_payload['application_id'],
                                        data_payload['session_id'],
                                        data_payload['participants'],
                                        data_payload['content'])
            return {'message': 'Message successfully added to the database!'}, 200