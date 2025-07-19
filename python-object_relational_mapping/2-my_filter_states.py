#!/usr/bin/python3
"""Lists states matching the input from the database."""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    c = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}%' ORDER BY id ASC".format(sys.argv[4])
    c.execute(query)
    for state in c.fetchall():
        print(state)
    c.close()
    db.close()
