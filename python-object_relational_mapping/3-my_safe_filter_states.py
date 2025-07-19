#!/usr/bin/python3
"""
Prevents SQL injection by using parameterized queries.

This script connects to a MySQL database and safely retrieves all rows from
the `states` table where the name matches a user-provided value.
The query uses placeholders (%s) instead of string formatting to protect
against SQL injection attacks (e.g. inputs like 'Arizona'; DROP TABLE ...').
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (sys.argv[4],))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
