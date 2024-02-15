from peewee import *
from models.connector import BaseModel, pg_db
    
class Room(BaseModel):
    user_id_1 = IntegerField()
    user_id_2 = IntegerField()

pg_db.connect()
pg_db.create_tables([Room], safe=True)