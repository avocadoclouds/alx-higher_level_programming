#!/usr/bin/python3
"""a script that lists  all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    
    import MYSQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]
