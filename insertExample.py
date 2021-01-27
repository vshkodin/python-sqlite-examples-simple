import sqlite3
connection = sqlite3.connect("AnyName.db")
cursor = connection.cursor()

sql_command = """INSERT INTO people (id, Name, LastName, AGE, DOB)
    VALUES (1, "AnyName", "AnyLastName", "0", "08-08-1991");"""

cursor.execute(sql_command)
connection.commit()
connection.close()