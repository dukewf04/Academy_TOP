from View.CplusDView import CplusDView


class CplusDController:
    """Класс представляет реализацию контроллера. Согласоваывает работу представления с моделью."""
    def __init__(self, inModel):
        # Конструктор принимает ссылку на модель, создает и отображает представление.
        self.model = inModel
        self.mView = CplusDView(self, self.mModel)

        self.mView.show()

    def setC(self):
        """При завершении редактирования поля ввода данных для C. Контроллер изменяет свойство модели."""
        c = self.mView.ui.le_c.text()
        self.mModel.setC(c)

    def setD(self):
        """При завершении редактирования поля ввода данных для D. Контроллер изменяет свойство модели."""
        d = self.mView.ui.le_d.text()
        self.mModel.setD(d)