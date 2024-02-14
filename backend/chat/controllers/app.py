from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class HelloWorld(Resource):
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

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)