#!/usr/bin/python3
"""script takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches
the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":

    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]
    NAME_SEARCHED = str(sys.argv[4])
    PORT = 3306

    db = MySQLdb.connect(
        host="localhost", port=3306, user=USERNAME, passwd=PASSWORD,
        db=DATABASE_NAME
    )
    cur = db.cursor()

    cur.execute(
        f"SELECT * FROM {DATABASE_NAME}.states WHERE BINARY name = %s\
                 ORDER BY states.id ASC",
        (NAME_SEARCHED,),
    )
    for row in cur.fetchall():
        print(row)
