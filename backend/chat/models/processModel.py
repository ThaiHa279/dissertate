from peewee import *
from models.connector import BaseModel, pg_db
    
class Process(BaseModel):
    name = CharField(max_length=255)
    api = CharField(max_length=255)

pg_db.connect()
pg_db.create_tables([Process], safe=True)