import sqlite3
import sqlite3

def get_connection():
    return sqlite3.connect("livestock.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS animals (
            tag_no TEXT PRIMARY KEY,
            institution_no TEXT,
            name TEXT,
            breed TEXT,
            gender TEXT,
            birth_date TEXT,
            pregnancy_count TEXT,
            status TEXT,
            vaccination_date TEXT,
            last_birth_date TEXT,
            image TEXT
        )
    """)
    conn.commit()
    conn.close()

def init_db():
    conn = sqlite3.connect("livestock.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS animals (
            tag_no TEXT PRIMARY KEY,
            institution_no TEXT,
            name TEXT,
            breed TEXT,
            gender TEXT,
            birth_date TEXT,
            pregnancy_count TEXT,
            status TEXT,
            vaccination_date TEXT,
            last_birth_date TEXT,
            image TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_animal(data):
    conn = sqlite3.connect("livestock.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO animals VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, tuple(data.values()))
    conn.commit()
    conn.close()

def fetch_all_animals():
    conn = sqlite3.connect("livestock.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM animals")
    results = cursor.fetchall()
    conn.close()
    return results
