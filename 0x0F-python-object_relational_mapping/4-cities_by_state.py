#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def list_all_states(username, password, database):
    """ function that lists all states from the database hbtn_0e_0_usa"""

    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)
    cursor = connection.cursor()
    query = "SELECT cities.id, cities.name, states.name from cities\
    JOIN states ON states.id = cities.state_id\
    ORDER BY cities.id ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    connection.close()


if __name__ == "__main__":

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    list_all_states(username, password, database)
