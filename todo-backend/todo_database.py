# This module is all about database

import sqlite3, json

#connect database (if not exists)
def database():
    try:
        conn = sqlite3.connect('database.sqlite')
    except Exception as e:
        print('The Database cannot be connected due to: ' + e)
    return (conn)

#create a todo table
def todo_table():
    db = database()
    query = """CREATE TABLE IF NOT EXISTS todo(
                id integer PRIMARY KEY,
                start_date text NOT NULL,
                finish_date text NOT NULL,
                priority text NOT NULL,
                category text NOT NULL,
                notes text NOT NULL,
                )
            """
    db.execute(query)
try:
    todo_table()
except Exception as e:
    print('The table cannot be created due to: ' + e)

#write into the todo table
def create_todo(start_date, finish_date, priority, category, notes):
    db = database()
    query = """INSERT INTO todo(start_date, finish_date, priority, category, notes) VALUES(?, ?, ?, ?, ?)"""
    db.execute(query, (start_date, finish_date, priority, category, notes))
    db.commit()

def read_todo():
    db = database()
    query = """SELECT * FROM todo"""
    query_exe = db.execute(query)
    all_todos = query_exe.fetchall()

    todo_array = []

    for todo in all_todos:
        todo_dic = {
            'id': todo[0],
            'start_date': todo[1],
            'finish_date': todo[2],
            'priority': todo[3],
            'category': todo[4],
            'notes': todo[5]
        }
        todo_array.append(todo_dic)
    
    return (todo_array)



