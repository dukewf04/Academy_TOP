# Task 1 (Singleton)
class DataBase:
    """Интерфейс подключения к базе данных"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DataBase, cls).__new__(cls)
        return DataBase._instance

    def __init__(self, db_name, db_user, db_password, db_host, db_port):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port

    def connect(self):
        print(f"Подключение к базе данных {self.db_name} прошло успешно!")

db1 = DataBase(
    db_name="HomeDB",
    db_user="Postgres",
    db_password="Postgres",
    db_host="localhost",
    db_port="5432",
)

db2 = DataBase(
    db_name="WorkDB",
    db_user="root",
    db_password="herasebe",
    db_host="localhost",
    db_port="9999",
)

print(f"db1: {db1.__dict__}\ndb2: {db2.__dict__}")