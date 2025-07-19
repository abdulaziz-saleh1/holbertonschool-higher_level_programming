#!/usr/bin/python3
"""
Safely filters states by name from the database using parameterized query.

This script connects to a MySQL database and retrieves rows from the `states`
table where the name matches a given argument, while preventing SQL injection.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    query = db.cursor()
    query.execute("""
        SELECT * FROM states
        WHERE name = %s
        ORDER BY id ASC
    """, (sys.argv[4],))

    rows = query.fetchall()

    for row in rows:
        print(row)
