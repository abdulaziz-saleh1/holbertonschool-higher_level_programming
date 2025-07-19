#!/usr/bin/python3
"""
Lists all cities with their state names from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )

    query = db.cursor()
    query.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    rows = query.fetchall()

    for row in rows:
        print(row)
