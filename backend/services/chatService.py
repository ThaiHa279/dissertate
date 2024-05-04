from services.geminiService import GeminiService
from models.createModels import Chat 
from services.userService import UserService
from services.processService import ProcessService
from peewee import *


class ChatService:
    def __init__(self) -> None:
        pass
    
    in_process = 0

    def storageMessage(self, name, message):
        user = UserService()
        user_id = user.findUser(name)
        new_message = Chat(user=user_id, content=message)
        new_message.save()
        print('Message saved successfully')

    def createRespone(self, message):
        process = ProcessService()
        if self.in_process:
            respone = process.runProcess(self.in_process, message)
            self.in_process = 0
            return respone

        if message:
            gemi = GeminiService()
            process_id = gemi.classifyMessage(message)
            print(f"Classify process to id {process_id}")
            if process_id == 0:
                respone = gemi.conversations(message)
            else:
                respone = process.getArguments(process_id)
                self.in_process = process_id
            return respone
        else:
            return 'No message provided'