#!/usr/bin/python3
"""Search states by name"""
import MySQLdb
import sys


def search_states():
    """Search states by name"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name =" \
            "'{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    search_states()
