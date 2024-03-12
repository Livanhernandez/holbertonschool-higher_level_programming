#!/usr/bin/python3
"""Takes argument and display all values in the state table"""

from sys import argv
from MySQLdb import Connect

if __name__ == '__main__':
    db = connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE %s\
        ORDER BY name ASC"
    cursor.execute(query, (argv[4],))

    rows = cursor.fetchall()

    for row in rows:
        print("{}".format(row))

    cursor.close()
    db.close()
