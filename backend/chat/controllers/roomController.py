from flask import request
from flask_restful import Resource, Api
from services.roomService import *

class Room(Resource):
    def get(self):
        return {'message': 'GET method called'}

    def post(self):
        json_data = request.get_json(force=True)
        return {'message': 'POST method called', 'data': json_data}, 201

    def put(self):
        json_data = request.get_json(force=True)
        return {'message': 'PUT method called', 'data': json_data}, 200

    def delete(self):
        return {'message': 'DELETE method called'}, 204