# import MainWindow_rc

from PyQt6.QtGui import QDoubleValidator, QMainWindow
from PyQt6.QtCore import PYQT_SIGNAL
from Utility.CplusDObserver import CplusDObserver
from Utility.CplusDMeta import CplusDmeta
from View.MainWindow import Ui_MainWindow

class CplusDview(QMainWindow, CplusDObserver, metaclass=CplusDmeta):
    """Класс, отвечающий за визуальное представление"""
    def __init__(self, inController, inModel, parent=None):
        self.mController = inController
        self.mModel = inModel

        # Подключение визуального представления
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Регистрируем представление в качестве наблюдателя
        self.mModel.addObserver(self)

        # Устанавливаем валидаторы полей ввода данных
        self.ui.le_c.setValidator(QDoubleValidator())
        self.ui.le_d.setValidator(QDoubleValidator())

        # Связываем событие завершение редактирования с метод контроллера
        self.connect(self.ui.le_c, PYQT_SIGNAL("editingFinished()"), self.mController.setC)
        self.connect(self.ui.le_d, PYQT_SIGNAL("editingFinished()"), self.mController.setD)