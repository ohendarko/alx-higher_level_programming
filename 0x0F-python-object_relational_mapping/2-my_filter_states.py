#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys


def search_states(username, password, database_name, state_name):
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database_name)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: script.py <username> <password> <database> <state>")
        sys.exit(1)
    username, password, database_name, state_name = sys.argv[1:5]
    search_states(username, password, database_name, state_name)
