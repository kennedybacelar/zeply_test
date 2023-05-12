from typing import List
import sqlite3

DB_STR_CONNECTION = "file::memory:?cache=shared"


def get_table_column_names(table_name: str) -> List[str]:
    with get_db_connection() as conn:
        col_data = conn.execute(f"PRAGMA table_info({table_name});").fetchall()
        columns = [entry[1] for entry in col_data]
    return columns


def init_db():

    conn = sqlite3.connect(DB_STR_CONNECTION)
    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS addresses
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  address TEXT UNIQUE,
                  label TEXT,
                  balance REAL,
                  currency TEXT,
                  creation_date TIMESTAMP,
                  last_used TIMESTAMP,
                  description TEXT,
                  status TEXT)"""
    )

    conn.commit()
    conn.close()


def get_db_connection() -> sqlite3.Connection:
    return sqlite3.connect("file::memory:?cache=shared")
