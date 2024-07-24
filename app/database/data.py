import sqlite3

DATABASE_NAME = 'db.sqlite3'

def get_connection():
    return sqlite3.connect(DATABASE_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        name TEXT,
        amount INTEGER DEFAULT 0,
        invited_friends INTEGER DEFAULT 0,
        invited_friends_usernames TEXT
    )
    ''')
    conn.commit()
    conn.close()

def insert_user(user_id, username, name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (user_id, username, name, amount, invited_friends, invited_friends_usernames)
    VALUES (?, ?, ?, 0, 0, ?)
    ''', (user_id, username, name, '[]'))
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user(user_id, amount_increase=0, invited_friends_increase=0, invited_friends_username=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE users SET amount = amount + ?
    WHERE user_id = ?
    ''', (amount_increase, user_id))

    cursor.execute('''
    UPDATE users SET invited_friends = invited_friends + ?
    WHERE user_id = ?
    ''', (invited_friends_increase, user_id))

    if invited_friends_username:
        cursor.execute('SELECT invited_friends_usernames FROM users WHERE user_id = ?', (user_id,))
        current_usernames = cursor.fetchone()[0]
        if current_usernames:
            current_usernames = eval(current_usernames)
        else:
            current_usernames = []
        current_usernames.append(invited_friends_username)
        cursor.execute('''
        UPDATE users SET invited_friends_usernames = ?
        WHERE user_id = ?
        ''', (str(current_usernames), user_id))

    conn.commit()
    conn.close()

create_table()
