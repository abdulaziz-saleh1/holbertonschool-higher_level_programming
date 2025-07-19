#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )

        # Create a cursor object
        cur = db.cursor()

        # Execute SQL query to select all states ordered by id
        cur.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        rows = cur.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close cursor and connection
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()
