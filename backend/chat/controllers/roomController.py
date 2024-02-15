from flask import request
from flask_restful import Resource, Api
from services.chatService import post_message

class Room(Resource):
    def get(self):
        return {'message': 'GET method called'}

    def post(self):
        json_data = request.get_json(force=True)
        post_message(json_data['user'], json_data['message'])
        return {'message': 'POST method called', 'data': json_data}, 201

    def put(self):
        json_data = request.get_json(force=True)
        return {'message': 'PUT method called', 'data': json_data}, 200

    def delete(self):
        return {'message': 'DELETE method called'}, 204