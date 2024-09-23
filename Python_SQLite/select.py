import sqlite3

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

stmt = """
    SELECT * FROM Users
"""

cursor.execute(stmt)

# Возвращает список, кортеж
users = cursor.fetchall()

print(users)

connection.close()
