import sqlite3
import bcrypt

def initialize_db():
    connection = sqlite3.connect('gym_management.db')
    cursor = connection.cursor()
    
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        membership_type TEXT
    )
    ''')
    
    connection.commit()
    connection.close()

if __name__ == '__main__':
    initialize_db()
