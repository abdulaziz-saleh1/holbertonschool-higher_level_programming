#!/usr/bin/python3
"""
Prints all cities of a given state from the database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = connection.cursor()

    query = ("SELECT cities.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")

    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    connection.close()
