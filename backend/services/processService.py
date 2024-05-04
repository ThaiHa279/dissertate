import json

from models.createModels import Process 
from services.geminiService import GeminiService
from services.rpaService import RPAService

gemi = GeminiService()

class ProcessService:
    def __init__(self) -> None:
        pass
    
    def addProcess(self, name, key, arguments):
        try:
            new_process = Process(name=name, key=key, arguments=arguments)
            new_process.save()
            gemi = GeminiService()
            res = gemi.createSentences(new_process.id, name)
            print(res)
            return f'Đã thêm quy trình {name} vào cơ sở dữ liệu với id là {new_process.id}'
        except Exception as e:
            return e
        
    def getArguments(self, process_id):
        process = Process.get_by_id(process_id)
        return "Tôi cần các thông tin về " + process.arguments + " để thực thi quy trình " + process.name
    
    def runProcess(self, process_id, message):
        try: 
            process = Process.get_by_id(process_id)
            arguments = gemi.extractInfor(message, process.arguments)
            if arguments == "" or "null" in arguments or "Không" in arguments or "không" in arguments:
                return f'Không thể trích xuất thông tin từ "{message}"'
            if process_id == 1:
                json_obj = list(json.loads(arguments).items())
                (name, key, varible) = (json_obj[0][1], json_obj[1][1], json_obj[2][1])
                return self.addProcess(name, key, varible)
            rpa = RPAService()
            rpa.runProcess(process.key, arguments)
            return f'Đang chạy quy trình {process.name} với thông tin {arguments}'
        except Exception as e:
            return e