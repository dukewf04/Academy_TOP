from tkinter import Frame, Label, Button
from controller import logicalc

class MainApp(Frame):
    """Отрисовка компонентов приложения"""
    def __init__(self, root):
        super(MainApp, self).__init__(root)
        self.build()

    def build(self):
        # Список кнопок
        button_list = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "0", "%", "X^2", ".",
        ]

        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        x = 10
        y = 140

        for btn in button_list:
            com = lambda x=btn: logicalc(self, x)
            Button(text=btn, bg="#FFF", font=("Times New Roman", 15), command=com).place(x=x, y=y, width=115, height=80)
            x += 110
            if x > 400:
                x = 10
                y += 80