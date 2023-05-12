import sqlite3


def init_db():

    # conn = sqlite3.connect(":memory:", isolation_level=None)
    conn = sqlite3.connect("file::memory:?cache=shared")
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
