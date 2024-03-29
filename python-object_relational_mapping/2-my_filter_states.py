#!/usr/bin/python3
"""Script that takes in an argument and display all values"""

from sys import argv
from MySQLdb import connect

if __name__ == '__main__':

    db = connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE '{}'\
                   ORDER BY name ASC".format(argv[4]))

    rows = cursor.fetchall()

    for row in rows:
        print("{}".format(row))

    cursor.close()
    db.close()