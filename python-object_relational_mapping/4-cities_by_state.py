#!/usr/bin/python3
"""Script that lists all cities from the database"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM\
        cities JOIN states ON cities.ctates_id = states.id"
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
