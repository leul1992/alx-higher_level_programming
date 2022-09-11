#!/usr/bin/python3
"""filter states by user input"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    c = conn.cursor()
    c.execute(f'SELECT * FROM states WHERE name LIKE BINARY
              "%{argv[4]}%" ORDER BY id')
    for res in c:
        print(res)
