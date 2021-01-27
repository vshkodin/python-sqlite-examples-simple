import sqlite3

connection = sqlite3.connect("AnyName.db")
cursor = connection.cursor()

sql_command = """
                CREATE TABLE people (
                id INTEGER,
                Name TEXT,
                LastName TEXT,
                AGE INTEGER,
                DOB DATE);"""

cursor.execute(sql_command)
connection.commit()
connection.close()
