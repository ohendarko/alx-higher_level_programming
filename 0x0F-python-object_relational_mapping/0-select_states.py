#!/usr/bin/python3
"""script that lists all states
from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def list_states(username, password, database_name):
    """lists all states from the database hbtn_0e_0_usa"""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database_name)
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: script.py <username> <password> <database")
        sys.exit(1)
    username, password, database_name = sys.argv[1:4]
    list_states(username, password, database_name)
