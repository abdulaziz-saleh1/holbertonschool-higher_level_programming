#!/usr/bin/python3
"""Lists states matching user input from the database."""

import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC".format(argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
