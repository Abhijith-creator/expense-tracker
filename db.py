import sqlite3

def get_connection():
    return sqlite3.connect('database.db')

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        amount REAL NOT NULL,
                        category TEXT NOT NULL,
                        description TEXT,
                        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    conn.commit()
    conn.close()
