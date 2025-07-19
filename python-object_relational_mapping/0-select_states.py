#!/usr/bin/python3
"""
Script to list all states from the database 
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor and execute query
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all rows exactly as required
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    db.close()
