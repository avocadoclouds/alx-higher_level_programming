#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':

    import MYSQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name\
                FROM cities LEFT JOIN states\
                ON states.id = cities.state_id\
                ORDER BY cities.id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)