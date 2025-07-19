#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Input validation
    if len(argv) != 4:
        print("Usage: {} username password database".format(argv[0]))
        exit(1)

    try:
        # Establish connection
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,  
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8"
        )
        
        # Create cursor and execute query
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM states ORDER BY id ASC")
            
            # Fetch and print results
            for row in cur.fetchall():
                print(row)
                
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        exit(1)
        
    finally:
        # Ensure connection is closed
        if 'conn' in locals():
            conn.close()
