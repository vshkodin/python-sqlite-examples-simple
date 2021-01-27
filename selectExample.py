import sqlite3

connection = sqlite3.connect("AnyName.db")
cursor = connection.cursor()

sql_command = "SELECT * FROM people"
cursor.execute(sql_command)

result = cursor.fetchall()
for r in result:
    print(r)