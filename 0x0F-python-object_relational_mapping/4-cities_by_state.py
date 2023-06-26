#!/usr/bin/python3
"""
script lists all cities from db hbtn_0e-04_usa
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
    cur.execute(
        f"SELECT {DATABASE_NAME}.cities.id, {DATABASE_NAME}.cities.name,\
              {DATABASE_NAME}.states.name FROM cities INNER JOIN\
                {DATABASE_NAME}.states on cities.state_id=states.id\
                    ORDER BY cities.id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
