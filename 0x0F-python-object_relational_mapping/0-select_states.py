#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import sys
    import MySQLdb

    userName = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=userName, passwd=password, db=dbName)
    c = conn.cursor()
    c.execute('SELECT * FROM states ORDER BY id ASC')
    for res in c:
        print(res)
