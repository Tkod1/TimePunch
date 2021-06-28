import time
import sqlite3

print("Hello welcome to Time punch!")
time.sleep(1.5)
print("Are you a (n)New or (e)Existing user?")
member_choice = input()


def new_user():
    try:
        n_user_name = input("New Username: ")
        n_user_password = input("New Password: ")
        conn = sqlite3.connect('temp.db')
        nsql = """ INSERT INTO USERSINFO
     (username, password) VALUES ('{}', '{}');""".format(n_user_name, n_user_password)
        cursor = conn.cursor()
        cursor.execute(nsql)
        conn.commit()
        print("Insertion complete!")
        cursor.close()
    except sqlite3.Error as error:
        print("Error while Inserting Data", error)
    finally:
        if conn:
            conn.close()
            print("Connection Closed Now")


def existing_user():
    try:
        cur = conn.cursor()
        cursor.execute(""" SELECT * FROM USERSINFO; """)
        for row in cursor.fetchall():
            print(row)
    except sqlite3.Error as error:
        print("Error trying to search userinfo: ", error)
    finally:
        if conn:
            conn.close()
            print("Connection Closed Now")


conn = sqlite3.connect('temp.db')
cursor = conn.cursor()

if member_choice == 'e':
    existing_user()
elif member_choice == 'n':
    new_user()
