from peewee import *
import datetime

pg_db = PostgresqlDatabase('chat_app', user='admin', password='admin',
                           host='localhost', port=5432)


class BaseModel(Model):
    id = PrimaryKeyField(null=False)
    createdAt = DateTimeField(default=datetime.datetime.now)
    updatedAt = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = pg_db