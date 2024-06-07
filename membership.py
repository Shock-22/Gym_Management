import sqlite3

# Define membership plans
MEMBERSHIP_PLANS = {
    "Basic": 30,
    "Standard": 50,
    "Premium": 70,
    "VIP": 100
}

def create_membership(name, age, membership_type):
    connection = sqlite3.connect('gym_management.db')
    cursor = connection.cursor()
    
    cursor.execute('INSERT INTO members (name, age, membership_type) VALUES (?, ?, ?)', (name, age, membership_type))
    connection.commit()
    connection.close()

def view_memberships():
    connection = sqlite3.connect('gym_management.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM members')
    members = cursor.fetchall()
    
    connection.close()
    return members

def get_membership_plans():
    return MEMBERSHIP_PLANS
