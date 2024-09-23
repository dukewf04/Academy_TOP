import sqlite3

connection = sqlite3.connect("my_database.db")

cursor = connection.cursor()

stmt = """
    DELETE FROM Users
    WHERE username = 'newuser'
"""

cursor.execute(stmt)

connection.commit()

connection.close()
