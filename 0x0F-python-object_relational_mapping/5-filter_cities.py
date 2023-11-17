#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def list_all_states(username, password, database, state_name):
    """ function that lists all states from the database hbtn_0e_0_usa"""

    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)
    cursor = connection.cursor()
    query = "SELECT cities.name FROM cities\
    JOIN states ON cities.state_id = states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))
    results = cursor.fetchall()
    cities = ', '.join(city[0] for city in results)
    print(cities)
    cursor.close()
    connection.close()


if __name__ == "__main__":

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]
    list_all_states(username, password, database, state_name)
