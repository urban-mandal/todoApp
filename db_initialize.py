import sqlite3 as sq
import os


def db_initilize():
    cwd = os.getcwd()
    name = '/app.db'
    path = cwd + name
    conn = sq.connect(path)
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY  KEY , username TEXT NOT NULL, email TEXT NOT NULL, password TEXT NOT NULL)")
    conn.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (task_id INTEGER PRIMARY KEY, description TEXT NOT NULL, deadline TEXT NOT NULL, user_id, FOREIGN KEY (user_id) REFERENCES users (user_id))")
    conn.commit()
    conn.close()
