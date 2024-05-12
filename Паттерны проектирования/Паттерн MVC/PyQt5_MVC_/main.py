import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from View.MainWindow import Ui_MainWindow

from Model.CplusDModel import CplusDModel
from Controller.CplusDController import CplusDController


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    qDialog = QDialog()
    window = Ui_MainWindow()
    window.setupUi(qDialog)

    # Создаем модель
    model = CplusDModel()

    # создаем контроллер и передаеи ему ссылку
    controller = CplusDController(model)

    # Запускаем приложение
    qDialog.exec_()


if __name__ == "__main__":
    main()
