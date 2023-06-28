#!/usr/bin/python3
"""
script list all State objects from the
database hbtn_0e_6_usa
"""

import MySQLdb
import sys

from model_state import State, Base

if __name__ == "__main__":

    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]
    PORT = 3306

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=USERNAME,
        passwd=PASSWORD,
        db=DATABASE_NAME
    )
    cur = db.cursor()
    cur.execute(
        f"SELECT * FROM {DATABASE_NAME}.states\
              ORDER BY states.id ASC"
    )
    for row in cur.fetchall():
        print(row)
