import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("""
CREATE TABLE TEACHERS(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEXT NOT NULL,
AGE INT,
SALARY REAL 
)
""")

print("Table created successfully")
conn.close()