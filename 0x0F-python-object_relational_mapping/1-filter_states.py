#!/usr/bin/python3
"""filter and list states name starting with N"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    un = sys.argv[1]
    pas = sys.argv[2]
    dbN = sys.argv[3]

    conn = MySQLdb.connect(host='localhost', port=3306, user=un,
                           passwd=pas, db=dbN)
    c = conn.cursor()
    c.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id')
    for res in c:
        print(res)
