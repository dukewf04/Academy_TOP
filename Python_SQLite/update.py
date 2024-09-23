import sqlite3

connection = sqlite3.connect("my_database.db")

cursor = connection.cursor()

stmt = """
    UPDATE Users SET age = 33
    WHERE username = 'newuser'
"""

cursor.execute(stmt)

connection.commit()

connection.close()
