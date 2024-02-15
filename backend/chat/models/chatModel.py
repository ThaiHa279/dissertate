from peewee import *
from models.connector import BaseModel, pg_db
from models.roomModel import Room
    
class Chat(BaseModel):
    room_id = ForeignKeyField(Room, backref='room')
    text = TextField()

pg_db.connect()
pg_db.create_tables([Chat], safe=True)