#!/usr/bin/python3
"""
Script that lists all states from the databse hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # Connecting to MySQL database
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, database=database, port=3306)

    # Creating cursor object
    cur = db.cursor()

    # Executing MySql Query
    cur.execute("SELECT * FROM states ORDER BY id")

    # Obtaining Query Result & prints the result in rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean Up
    cur.close()
    db.close()
