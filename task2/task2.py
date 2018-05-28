#Monument labs Internship assignment
#Task 2

#Author: Alexander Moreno
#5/27/2018

import sqlite3

#using python-intercom
from intercom.client import Client


def addAllUsersToIntercom(conn, interc):

    c = conn.cursor();


    #get the total number of rows in user
    c.execute('SELECT COUNT(*) FROM user')
    maxCount = c.fetchone()[0]
    #if M
    if maxCount == 0:
        conn.close()
        return 0

    
    #iterate through users, then add them to Intercom
    for idNum in range(1,maxCount+1):
        c.execute('SELECT * FROM user WHERE id=%d' % (idNum))
        row = c.fetchone()
        interc.users.create(user_id=row[0],name=row[1],email=row[2])

    #work is done, close database session
    c.close()
    return 1




if __name__ == '__main__':
    conn = sqlite3.connect('PATH/userdb.db');
    intercom = Client(personal_access_token='access_token')
    addAllUsersToIntercom(conn,intercom)
    conn.close()
    
    
