from flask import Flask, jsonify
from flask_restful import Api

from resources.message import Message, MessageList, MessageRegister

from db.database import create_database



app = Flask(__name__)
api = Api(app)



api.add_resource(Message, '/message/<string:id>')
api.add_resource(MessageList, '/messages')
api.add_resource(MessageRegister, '/message/add')



if __name__ == '__main__':
    create_database('./db/datamessage.db')
    app.run()
