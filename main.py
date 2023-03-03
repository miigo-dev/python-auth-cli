import re
import sqlite3
import bcrypt

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users (
        username VARCHAR,
        password BLOB
    )""")

conn.commit()


def user_check(username):
    c.execute("""SELECT * FROM users WHERE username=?
            """, (username,))
    row = c.fetchone()

    if not re.match("^[a-zA-Z0-9_.-]+$", username):
        print("Only alphanumeric characters are allowed.")
        return False

    elif row and row:
        print("Username already exists.")
        return False
    return True


def pass_check(password):
    if len(password) < 8:
        print("Password must be 8 characters long.")
        return False
    elif re.search('[0-9]', password) is None:
        print("Password must contain a number.")
        return False
    elif re.search('[A-Z]', password) is None:
        print("Password must contain a capital letter.")
        return False
    return True


def register():
    while True:
        username = input("Enter a Username: ")
        if user_check(username):
            break

    while True:
        password = input("Enter a password: ")
        if pass_check(password):
            pwd = password.encode('utf-8')
            pwd_salt = bcrypt.gensalt()
            pwd_hashed = bcrypt.hashpw(pwd, pwd_salt)
            break

    try:
        c.execute("""
                INSERT INTO users (username, password) VALUES (?,?)
            """, (username, pwd_hashed))
        conn.commit()
        print("User registered successfully.")
    except Exception as e:
        print("An error occurred while registering the user.")
        print(str(e))


def login():
    while True:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        c.execute("""
                SELECT * FROM users WHERE username=?
            """, (username,))
        row = c.fetchone()

        if row and bcrypt.checkpw(password.encode('utf-8'), row[1]):
            print("Login Successful!")
            break
        else:
            print("Invalid Username or Password.")


while True:
    option = input("[1] Register\n[2] Login\n[3] Exit\n> ")
    if option == '1':
        register()

    elif option == '2':
        login()

    elif option == '3':
        conn.close()
        break
