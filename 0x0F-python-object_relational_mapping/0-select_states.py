#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    import MySQLdb

    userName = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=userName, passwd=password, db=dbName)
    c = conn.cursor()
    c.execute("""SELECT * FROM states ORDERBY states.id ASC""")
    for res in cu:
        print(row)
