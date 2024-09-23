import sqlite3

# Создание подключения к БД
connection = sqlite3.connect("my_database.db")

# Курсор - объект, связь нашего кода с БД. Позволяет отправлять изменения в БД и устанавливать с ней соединения.
cursor = connection.cursor()

# Создание таблицы
stmt = """
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER
    )
"""
cursor.execute(stmt)

# Отправка запроса в БД, сохранение изменений
connection.commit()

# --- Типы данных: int, text, real, blob (двоичные данные)
# DB Browser for SQLite (SQLite Studio) - графическое приложение для редактирование БД SQLite

#  Завершить подключение
connection.close()
