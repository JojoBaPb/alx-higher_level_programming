#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
where name matches the given argument.
Safe from SQL injections.
Usage 4 args: ./3-my_safe_filter_states.py <mysql username> \
                                           <mysql password> \
                                           <database name> \
                                           <state name searched>
"""
import MySQLdb
from sys import argv
                                                                                                                    if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
            (argv[4],))
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    cursor.close()
    db.close()
