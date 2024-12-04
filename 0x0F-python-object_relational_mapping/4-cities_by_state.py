#!/usr/bin/env python3
""" Script to list states where name starts with N"""

import MySQLdb
from sys import argv

# connect to mysql and query the database

if __name__ == '__main__':
    conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3],
    unix_socket = '/var/run/mysqld/mysqld.sock',
    charset='utf8')
    
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities INNER JOIN states\
    ON cities.state_id = states.id\
    ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for obj in rows:
        print(obj)
    cur.close()
    conn.close()
