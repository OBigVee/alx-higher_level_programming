#!/usr/bin/python3

"""
    script lists all states from databases hbtn_0e_0_usa
    - Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - Results must be displayed as they are in the example below
    - Your code should not be executed when imported
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]
    PORT = 3306
    db = MySQLdb.connect(
        host="localhost", port=3306, user=USERNAME, passwd=PASSWORD, db=DATABASE_NAME
    )
    cur = db.cursor()

    cur.execute(f"SELECT * FROM {DATABASE_NAME}.states ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)
