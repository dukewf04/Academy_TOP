import sys
from PyQt6.QtGui import QGuiApplication

from Model.CplusDModel import CplusDModel
from Controller.CplusDController import CplusDController

def main():
    app = QGuiApplication(sys.argv)

    # Создаем модель
    model = CplusDModel()
    # Создаем контроллер и передаем ему ссылку
    controller = CplusDController(model)
    # Запускаем приложение
    app.exec()

if __name__ == "__main__":
    main()