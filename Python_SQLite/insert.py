import sqlite3

connection = sqlite3.connect("my_database.db")

cursor = connection.cursor()

stmt = """
    INSERT INTO Users (username, email, age)
        VALUES ('Луиза', 'luizianf@gmail.com', 29)
"""

cursor.execute(stmt)
connection.commit()
connection.close()
