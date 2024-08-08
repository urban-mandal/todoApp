import sqlite3 as sq
import os


def db_path():
    cwd = os.getcwd()
    name = '/app.db'
    path = cwd + name
    return path


def add_user(username, email, password):
    conn = sq.connect(db_path())
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                    (username, email, password))
        conn.commit()
        res = cur.execute("SELECT * FROM users")
        print(res.fetchall())
        conn.close()
        return True
    except:
        return False


def get_hashed_password(email):
    conn = sq.connect(db_path())
    cur = conn.cursor()
    res = cur.execute(
        "SELECT password FROM users WHERE email = (?) ", (email,))
    if res.fetchall():
        res = cur.execute(
            "SELECT password FROM users WHERE email = (?) ", (email,))
        password = res.fetchall()[0][0]
        conn.close()
        return password
    else:
        conn.close()
        return None


def get_username(email):
    conn = sq.connect(db_path())
    cur = conn.cursor()
    res = cur.execute("SELECT username FROM users WHERE email = (?)", (email,))
    username = res.fetchall()[0][0]
    return username


# too much work so I wont make this work yet!
def delete_user(username):
    pass
