#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    st_name = sys.argv[4]
    curs.execute("""SELECT cities.name FROM cities INNER JOIN states ON
                 cities.state_id=states.id WHERE states.name=%s""",
                 (st_name,))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
