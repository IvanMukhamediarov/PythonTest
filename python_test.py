import sys
import cx_Oracle

DataSource = sys.argv[1]
UserId = sys.argv[2]
Password = sys.argv[3]

con = cx_Oracle.connect(UserId, Password, DataSource)
cursor = con.cursor();
cursor.execute(""" select * from all_objects where owner='DATAINF' """)

for row in cursor:
	print(row)

cursor.close()
con.close()
