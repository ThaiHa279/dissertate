from peewee import *
from models.connector import BaseModel, pg_db

class Process(BaseModel):
    name = CharField(max_length=255)
    key = CharField(max_length=255, null=True)
    arguments = CharField(max_length=255, null=True)
    
class User(BaseModel):
    name = CharField(max_length=255, null=True)

class Chat(BaseModel):
    user = ForeignKeyField(User, backref='user')
    content = TextField()

pg_db.connect()
pg_db.create_tables([User, Process, Chat], safe=True)
