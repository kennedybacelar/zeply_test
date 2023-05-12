import sqlite3


def init_db():

    conn = sqlite3.connect("mydatabase.db")
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS addresses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  address TEXT UNIQUE,
                  currency TEXT)"""
    )

    conn.commit()
    conn.close()
