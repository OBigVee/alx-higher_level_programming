#!/usr/bin/python3
""" script lists all stated with a name starting with N
    from database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":

    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]
    PORT = 3306

    db = MySQLdb.connect(
        host="localhost", port=3306, user=USERNAME, passwd=PASSWORD,
        db=DATABASE_NAME
    )
    cur = db.cursor()

    cur.execute(f"SELECT * FROM {DATABASE_NAME}.states WHERE BINARY name\
                LIKE 'N%'")
    for row in cur.fetchall():
        print(row)
