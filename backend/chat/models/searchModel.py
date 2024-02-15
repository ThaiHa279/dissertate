from peewee import *
from models.processModel import Process
from models.connector import BaseModel, pg_db
    
class Search(BaseModel):
    text = TextField()
    process_id = ForeignKeyField(Process, backref='process')

pg_db.connect()
pg_db.create_tables([Search], safe=True)