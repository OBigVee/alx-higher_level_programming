#!/usr/bin/python3
"""
script lists all cities from db hbtn_0e-04_usa
"""

import sys
import MySQLdb
import pprint

if __name__ == "__main__":

    USERNAME = sys.argv[1]
    PASSWORD = sys.argv[2]
    DATABASE_NAME = sys.argv[3]
    STATE_NAME = sys.argv[4]
    PORT = 3306

    db = MySQLdb.connect(
        host="localhost", port=3306, user=USERNAME, passwd=PASSWORD,
        db=DATABASE_NAME
    )

    cur = db.cursor()
    cur.execute(
        "SELECT cities.name\
        FROM cities INNER JOIN states on cities.state_id=states.id\
        WHERE states.name=%s ORDER BY cities.id ASC",
        (STATE_NAME,),
    )

    list_cities = []
    for row in cur.fetchall():
        list_cities.append(row)
    cities = [city[0] for city in list_cities]
    output = ", ".join(cities)
    print(output)

    cur.close()
    db.close()
