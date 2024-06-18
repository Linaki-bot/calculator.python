import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO TEACHERS VALUES(1,'James','Kariuki', 45, 58000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(2,'Jamleck','Matara', 45, 58000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(3,'Makai','Yusuf', 45, 58000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(4,'Rita','Mogiti', 45, 58000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(5,'Zayn','Malik', 45, 58000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(6,'Jahleel','Kinyanjui', 45, 58000.00)")


print("Successfully added records")

conn.close()
