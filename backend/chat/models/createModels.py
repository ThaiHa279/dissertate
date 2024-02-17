from peewee import *
from models.connector import BaseModel, pg_db

class Process(BaseModel):
    name = CharField(max_length=255)
    api = CharField(max_length=255, null=True)

class Room(BaseModel):
    user_id_1 = IntegerField()
    user_id_2 = IntegerField()

class Chat(BaseModel):
    room_id = ForeignKeyField(Room, backref='room')
    role = IntegerField()
    content = TextField()

pg_db.connect()
pg_db.create_tables([Process, Room, Chat], safe=True)