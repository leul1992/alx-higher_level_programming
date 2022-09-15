#!/usr/bin/python3
"""takes name of state as arg and lists all cities of the state"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect('localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    c = conn.cursor()
    c.execute('SELECT c.name FROM cities c JOIN states s ON s.name\
              = %s AND c.state_id=s.id ORDER BY c.id', (argv[4],))
    i = 0
    for res in c:
        print(res[0], end=', ' if len(list(c))-1 != i else '\n')
        i += 1
