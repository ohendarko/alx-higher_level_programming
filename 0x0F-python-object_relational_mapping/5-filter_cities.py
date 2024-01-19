#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def list_cities_by_state(username, password, database_name, state_name):
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database_name)
    cursor = db.cursor()
    query = ("SELECT states.name, cities.name FROM cities "
             "INNER JOIN states ON cities.state_id = states.id "
             "ORDER BY cities.id ASC")
    cursor.execute(query)
    rows = cursor.fetchall()

    print(", ".join([cities[1] for cities in rows
                     if sys.argv[4] == cities[0]]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage:")
        sys.exit(1)
    username, password, database_name, state_name = sys.argv[1:5]
    list_cities_by_state(username, password, database_name, state_name)
