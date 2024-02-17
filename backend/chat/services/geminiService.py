import os
from dotenv import load_dotenv
load_dotenv() 
import google.generativeai as genai
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

class GeminiService:
    def __init__(self) -> None:
        pass
    
    embed = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    model = genai.GenerativeModel('gemini-pro')

    def createSentences(self, process_id, data):
        response = self.model.generate_content("bạn vào vai nguời dùng, hãy tạo ra 10 câu để huấn luyện chatbot có chủ đề về  " + data + " có nội dung đa dạng")
        sentence = response.text.split('\n')

        docs = [Document(page_content=st, metadata={'process_id': process_id}) for st in sentence]
        db = Chroma.from_documents(docs, self.embed,  persist_directory="./chroma_db")

        return sentence
    
    chat = model.start_chat(history=[])
    def chatConversations(self, message):
        response = self.chat.send_message(message)
        return response.text
    
    def retrieval(self, query):
        db = Chroma(persist_directory="./chroma_db", embedding_function=self.embed)
        db.get() 
        docs = db.similarity_search(query)
        return docs[0].metadata

# gemi = GeminiService()
# print(gemi.createSentences(1, "chào hỏi"))
# print(gemi.createSentences(2, "yêu cầu đăng ký học phần"))
# print(gemi.createSentences(3, "yêu cầu nhập kế hoạch học tập"))
# print(gemi.retrieval("toi muon dang ky hoc phan"))