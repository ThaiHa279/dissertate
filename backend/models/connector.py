import os
from peewee import *
import datetime
from dotenv import load_dotenv

load_dotenv()

database_name = os.environ.get('DATABASE_NAME')
database_host = os.environ.get('DATABASE_HOST')
database_port  = os.environ.get('DATABASE_PORT')
database_user = os.environ.get('DATABASE_USER')
database_password = os.environ.get('DATABASE_PASSWORD')

pg_db = PostgresqlDatabase(database_name, user=database_user, password=database_password,
                           host=database_host, port=database_port)

class BaseModel(Model):
    id = PrimaryKeyField(null=False)
    createdAt = DateTimeField(default=datetime.datetime.now)
    updatedAt = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = pg_db