#!/usr/bin/python3
"""a script that lists all cities
from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def list_cities(username, password, database_name):
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database_name)
    cursor = db.cursor()
    query = ("SELECT cities.id, cities.name, states.name "
             "FROM cities INNER JOIN states On cities.state_id = states.id"
             " ORDER BY cities.id ASC")
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ")
        sys.exit(1)
    username, password, database_name = sys.argv[1:4]
    list_cities(username, password, database_name)
