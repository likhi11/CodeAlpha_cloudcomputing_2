import sqlite3

def init_db():
    conn = sqlite3.connect('secure.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn

def safe_query(conn, query, params=(), fetch=False):
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    return cursor.fetchall() if fetch else None