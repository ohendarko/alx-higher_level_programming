#!/usr/bin/python3
"""a script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, is safe from MySQL injections!"""
import MySQLdb
import sys


def search_states(username, password, database_name, state_name):
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database_name)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"
    cursor.execute(query, ('%' + state_name + '%',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ")
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1:5]
    search_states(username, password, database_name, state_name)
