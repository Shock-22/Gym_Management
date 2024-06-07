import sqlite3
import bcrypt

def register_user(username, password):
    if not username or not password:
        print("Username and password cannot be empty.")
        return False

    connection = sqlite3.connect('gym_management.db')
    cursor = connection.cursor()
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        connection.commit()
    except sqlite3.IntegrityError:
        print("Username already exists.")
        return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        connection.close()
    print("User registered successfully.")
    return True

def login_user(username, password):
    if not username or not password:
        print("Username and password cannot be empty.")
        return False

    connection = sqlite3.connect('gym_management.db')
    cursor = connection.cursor()
    
    try:
        cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
    
        if result and bcrypt.checkpw(password.encode('utf-8'), result[0]):
            print("Login successful!")
            return True
        else:
            print("Invalid username or password.")
            return False
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        connection.close()
