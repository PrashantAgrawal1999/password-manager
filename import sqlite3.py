import sqlite3

def init_db():
    conn = sqlite3.connect('passwords.db')
    c = conn.cursor()
    c.execute('''
                CREATE TABLE IF NOT EXISTS passwords (
              id INTEGER PRIMARY KEY,
              service TEXT NOT NULL,
              username TEXT NOT NULL,
              password BLOB NOT NULL
            )
        ''')
    conn.commit()
    conn.close()
init_db()