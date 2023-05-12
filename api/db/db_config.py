import sqlite3

DB_STR_CONNECTION = "file::memory:?cache=shared"


def init_db():

    conn = sqlite3.connect(DB_STR_CONNECTION)
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS addresses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  address TEXT UNIQUE,
                  currency TEXT)"""
    )

    conn.commit()
    conn.close()


def get_db_connection():
    return sqlite3.connect("file::memory:?cache=shared")
