import json
import sqlite3

# 1. Объединение операторов, создание профильного запроса

connection = sqlite3.connect("my_database.db")
cursor = connection.cursor()

stmt = """
    SELECT username, age
    FROM Users
    WHERE age > ?
"""

cursor.execute(stmt, (25,))

# Возвращает список, кортеж
users = cursor.fetchall()

print("1. Простой SELECT:", users)

# ----------- 2. Операторы GROUP BY, HAVING -----------
stmt = """
    SELECT age, AVG(age)
    FROM Users
    GROUP BY age
    HAVING AVG(age) > ?
"""

cursor.execute(stmt, (20,))

# Возвращает список, кортеж
users = cursor.fetchall()

print("2. GROUP BY:", users)

# ----------- 3. Оператор ORDER BY -----------
stmt = """
    SELECT username, age
    FROM Users
    ORDER BY age ASC
"""

cursor.execute(stmt)

# Возвращает список, кортеж
users = cursor.fetchall()

print("3. ORDER BY:", users)

# ----------- 4. Комбинирование (композиция) операторов -----------
stmt = """
    SELECT username, age, AVG(age)
    FROM Users
    GROUP BY age
    HAVING AVG(age) > ?
    ORDER BY age DESC
"""

cursor.execute(stmt, (25,))

# Возвращает список, кортеж
users = cursor.fetchall()

print("4. Комбинирование:", users)

# ----------- 5. Агрегатные функции COUNT, SUM, AVG, MIN, MAX -----------
stmt = """
    SELECT COUNT(*)
    FROM Users
"""

cursor.execute(stmt)

total_user = cursor.fetchone()[0]
print("5.1. Агрегатные функции (COUNT):", total_user)
# *****
stmt = """
    SELECT SUM(age)
    FROM Users
"""

cursor.execute(stmt)

sum_age = cursor.fetchone()[0]
print("5.2. Агрегатные функции (SUM):", sum_age)
# *****
stmt = """
    SELECT MIN(age)
    FROM Users
"""

cursor.execute(stmt)

min_age = cursor.fetchone()[0]
print("5.3. Агрегатные функции (MIN):", min_age)

# ----------- 6. Преобразование -----------
stmt = """
    SELECT *
    FROM Users
"""

cursor.execute(stmt)
users = cursor.fetchall()

user_list = []
for user in users:
    user_dict = {"id": user[0], "username": user[1], "email": user[2], "age": user[3]}
    user_list.append(user_dict)

print("6. Преобразование:", json.dumps(user_list, indent=3, ensure_ascii=False))

connection.close()
