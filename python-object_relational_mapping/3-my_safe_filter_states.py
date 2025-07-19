#!/usr/bin/python3
"""Safely lists states matching the input from the database."""

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
