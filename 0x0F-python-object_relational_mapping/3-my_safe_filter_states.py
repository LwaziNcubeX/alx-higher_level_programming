#!/usr/bin/python3
"""safe from MySQL injections"""
import MySQLdb
import sys


def list_states_with_name():
    """
    List all states with a name matching the given
    argument (safe from MySQL injections)
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states_with_name()
