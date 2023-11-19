#!/usr/bin/python3
"""
Lists all cities of a given state from the database
"""

import sys
import MySQLdb


def list_cities_by_state():
    """
    Lists all cities of a given state from the database
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=username, passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name"
                   " FROM cities JOIN states \
                   ON cities.state_id = states.id"
                   " WHERE states.name = %s ORDER BY cities.id ASC",
                   (state_name,))

    rows = cursor.fetchall()
    if rows:
        print(', '.join(city[0] for city in rows))

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_by_state()
