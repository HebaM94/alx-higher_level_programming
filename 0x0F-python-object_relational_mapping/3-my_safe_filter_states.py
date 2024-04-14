#!/usr/bin/python3
"""script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
that is safe from MySQL injections"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    st_name = sys.argv[4]
    curs.execute("SELECT * FROM states WHERE name LIKE %s", (st_name,))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
