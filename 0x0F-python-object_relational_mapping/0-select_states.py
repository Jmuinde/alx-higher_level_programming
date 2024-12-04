#!/usr/bin/env python3
"""Script to list all states in the database"""

import MySQLdb
from sys import argv

if len(argv) != 4:
    print("Usage: script_name <username> <password> <database>")
    exit(1)

# connect to mysql and query database
if __name__ == '__main__':
    try:
        conn = MySQLdb.connect(
            host ='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            unix_socket='/var/run/mysqld/mysqld.sock',
            charset='utf8'
            )
    except MySQLdb.Error as e:
        print(f"Error connecting to MySql: {e}")
        exit(1)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for obj in rows:
        print(obj)
    cur.close()
    conn.close()

