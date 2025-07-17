#!/usr/bin/python3
"""Script that lists all states from the database."""
import MySQLdb
import sys

if __name__ == "__main__":
    # arguments: username, password, database name
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # create a cursor
    cur = db.cursor()
    # execute the query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # fetch and print the results
    for row in cur.fetchall():
        print(row)

    # close cursor and connection
    cur.close()
    db.close()
