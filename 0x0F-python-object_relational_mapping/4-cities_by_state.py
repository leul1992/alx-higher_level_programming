#!/usr/bin/python3
"""Lists all cities from database hbtn_0e_4_usa"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect('localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    c = conn.cursor()
    c.execute('SELECT c.id, c.name, s.name FROM cities c\
              JOIN states s ON c.state_id=s.id ORDER BY c.id')
    for res in c:
        print(res)
