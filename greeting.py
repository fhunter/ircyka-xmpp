import sqlite3,random

def get_greeting(conn):
    cursor=conn.cursor()
    cursor.execute('select greeting from greetings')
    greet_list=cursor.fetchall()
    number=len(greet_list)
    conn.commit()
    cursor.close()
    return greet_list[random.randrange(0,number-1)][0]

def act_on_message(conn,nick,text):
    