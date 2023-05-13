from datetime import datetime
from peewee import *

DB_STR_CONNECTION = "file::memory:?cache=shared"

db = SqliteDatabase(DB_STR_CONNECTION)


class Addresses(Model):
    id = AutoField()
    address = CharField(unique=True)
    label = CharField(null=True)
    balance = FloatField(null=True)
    currency = CharField(null=False)
    creation_date = DateTimeField(default=datetime.now(), null=True)
    last_used = DateTimeField(null=True)
    description = TextField(null=True)
    status = CharField(null=True)

    class Meta:
        database = db
        table_name = "addresses"


def get_db_connection() -> SqliteDatabase:
    return SqliteDatabase(DB_STR_CONNECTION)


def init_db():
    db.connect()
    db.create_tables([Addresses])
    db.close()
