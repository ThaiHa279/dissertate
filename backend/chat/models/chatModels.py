from peewee import *
import datetime
from connector import BaseModel, pg_db



class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField(unique=True)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)
    is_active = BooleanField(default=True)
    
class Message(BaseModel):
    user = ForeignKeyField(User, backref='messages')
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

pg_db.connect()
pg_db.create_tables([Message, User], safe=True)