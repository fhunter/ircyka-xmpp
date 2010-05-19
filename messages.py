import sqlite3,random
import re

def get_greeting(conn):
    cursor=conn.cursor()
    cursor.execute('select greeting from greetings')
    greet_list=cursor.fetchall()
    number=len(greet_list)
    conn.commit()
    cursor.close()
    return greet_list[random.randrange(0,number-1)][0]

def act_on_message(conn,nick,text):
    responces=[]
    if nick=='ircyka':
        return responces
    cursor=conn.cursor()
    cursor.execute('select regexp,reaction from regexp')
    data_list=cursor.fetchall()
    for tt in data_list:
        try:
            regexp=tt[0]
	    pattern=re.compile(regexp)
            if pattern.search(nick+':'+text) != None:
                print tt[1]
    	        responces.append(tt[1])
        except:
            print "Regexp %s failed on %s"%(tt[0],nick+':'+text)
    conn.commit()
    cursor.close()
    return responces
