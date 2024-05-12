from PyQt6.QtCore import pyqtWrapperType
from abc import ABCMeta

# Модуль реализации метакласса, необходимого для работы представления.
# pyqtWrapperType - метакласс, общий для оконных компонентов библиотеки QT
# ABCMeta - метакласс для реализации абстрактных суперклассов

# CplusDMeta - метакласс для представления.

class CplusDMeta(pyqtWrapperType, ABCMeta):
    pass
