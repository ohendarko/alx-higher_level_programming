#!/usr/bin/python3
"""script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def list_states_starting_with_n(username, password, database_name):
    """Function that..."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database_name)
    c = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <username> <password> <database_name>")
        sys.exit(1)
    username, password, database_name = sys.argv[1:4]
    try:
        list_states_starting_with_n(username, password, database_name)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)
