from models.createModels import Chat 

def post_message(user, message_text, room_id):
    if message_text:
        new_message = Chat(role=user, content=message_text, room_id=room_id)
        new_message.save()
        return {'message': 'Message saved successfully'}, 201
    else:
        return {'error': 'No message provided'}, 400