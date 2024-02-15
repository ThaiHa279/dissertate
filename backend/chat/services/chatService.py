from flask import request
from models.chatModels import Message 

def post_message(user, message_text):
    if message_text:
        new_message = Message(user=user, content=message_text)
        new_message.save()
        return {'message': 'Message saved successfully'}, 201
    else:
        return {'error': 'No message provided'}, 400