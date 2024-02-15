import sys  
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from controllers.chatController import Chat
from controllers.roomController import Room
from controllers.processController import Process

app = Flask(__name__)
sys.path.append('/home/thaiha/workspace/dissertate/backend') 
CORS(app)
api = Api(app)

api.add_resource(Chat, '/api/v1/chat')
api.add_resource(Room, '/api/v1/room')
api.add_resource(Process, '/api/v1/process')

if __name__ == '__main__':
    app.run(debug=True)