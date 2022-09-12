#!/usr/bin/python3
"""filter states by user input safely from sql injection"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    c = conn.cursor()
    c.execute('SELECT * FROM states WHERE name \
              LIKE BINARY "{:s}" ORDER BY id'.format(argv[4]))
    for res in c:
        print(res)
