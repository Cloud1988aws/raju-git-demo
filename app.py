print("this is new app")

import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # VULNERABLE: User input is directly injected into the query
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    cursor.execute(query)
    user_data = cursor.fetchall()
    conn.close()
    return user_data

# Attacker input could be " OR '1'='1"
username_input = input("Enter your username: ")
print(get_user_data(username_input))

