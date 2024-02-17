from models.createModels import Process 
from services.geminiService import GeminiService

def addProcess(name, api):
    if name:
        new_process = Process(name=name, api=api)
        new_process.save()
        gemi = GeminiService()
        res = gemi.createSentences(new_process.id, name)
        print(res)
        return {'message': 'New process is save sucessfully'}, 201
    else:
        return {'error': 'No name or api provided'}, 400