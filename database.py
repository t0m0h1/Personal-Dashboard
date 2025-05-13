import sqlite3

DB_PATH = "data/dashboard.db"

def get_db():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS health (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        water INTEGER,
        sleep REAL,
        steps INTEGER,
        exercise TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS mood (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        mood TEXT,
        note TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS gratitude (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        entry1 TEXT,
        entry2 TEXT,
        entry3 TEXT
    )''')
    conn.commit()
    conn.close()
