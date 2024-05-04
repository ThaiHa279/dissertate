import os
from dotenv import load_dotenv
load_dotenv() 
import google.generativeai as genai
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

class GeminiService:
    def __init__(self) -> None:
        pass
    
    # embed = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    embed = HuggingFaceEmbeddings(model_name="keepitreal/vietnamese-sbert")
    model = genai.GenerativeModel('gemini-pro')

    def createSentences(self, process_id, data):
        response = self.model.generate_content("bạn vào vai nguời dùng, hãy tạo ra 10 câu yêu cầu chatbot ngắn gọn \"" + data + "\" có nội dung đa dạng, không cần đánh số thứ tự câu.")
        sentence = response.text.split('\n')

        docs = [Document(page_content=st, metadata={'process_id': process_id}) for st in sentence]
        db = Chroma.from_documents(docs, self.embed,  persist_directory="./chroma_db")

        return sentence
    
    chat = model.start_chat(history=[])
    def conversations(self, message):
        response = self.chat.send_message(message)
        return response.text
    
    def classifyMessage(self, query):
        response = self.model.generate_content("câu \""+query+"\" có yêu cầu chatbot hay không? Chỉ trả lời Đúng hoặc Sai.")
        if "Đúng" in response.text:
            db = Chroma(persist_directory="./chroma_db", embedding_function=self.embed)
            db.get() 
            docs = db.similarity_search(query)
            res = [docs[0].metadata.get('process_id'), docs[1].metadata.get('process_id'), docs[2].metadata.get('process_id')]
            print(res)
            return max(set(res), key = res.count)
        else:
            return 0
    
    def extractInfor(self, message, arguments):
        response = self.chat.send_message("Hãy trích xuất thông tin về "+ arguments + " trong câu sau:" + message + "các thông tin cần format theo chuẩn: {\"argument1\":\"infor1\",\"argument2\":\"infor2\"} ")
        response.text.replace("\'", "")
        response.text.replace("\n", "")
        return response.text

# gemi = GeminiService()
# print(gemi.extractInfor("tôi cần đăng ký học phần CT123 vào lớp CT12301", "ma_hoc_phan, ma_lop_hoc"))
# print(gemi.createSentences(1, "yêu cầu chatbot thêm quy trình vào hệ thống"))
# print(gemi.createSentences(2, "yêu cầu chatbot giúp đăng ký học phần"))
# print(gemi.createSentences(3, "yêu cầu chatbot giúp thay đổi thông tin cá nhân"))
# print(gemi.createSentences(4, "yêu cầu chatbot giúp in giấy hoãn nghĩa vụ quân sự"))
# print(gemi.retrieval("tôi cần đăng ký học phần mới"))