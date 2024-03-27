import random

# Task1
# class Animal:
#     def __init__(self, nickname):
#         self.nickname = nickname
#     def __str__(self):
#         return self.nickname
#
# class Cat(Animal):
#     def __init__(self, nickname):
#         super().__init__(nickname)
#         self.nickname = nickname
#
#     def voice(self):
#         return "Meow!!!"
#
#     def run(self):
#         return "Побежали!"
#
#
# class Parrot(Animal):
#     def __init__(self, nickname):
#         super().__init__(nickname)
#         self.nickname = nickname
#
#     def voice(self):
#         return "Kwarr!!!"
#
#     def fly(self):
#         return "Полетели!"

# Task2
# class Message:
#     def __init__(self, sender: str, recipien: str):
#         self.sender = sender
#         self.recipien = recipien
#     def showHeader(self):
#         return f"Отправитель: {self.sender}, Получатель: {self.recipien}"
#
# class TextMessage(Message):
#     def __init__(self, sender: str, recipien: str, text: str):
#         super().__init__(sender, recipien)
#         self.sender = sender
#         self.recipien = recipien
#         self.text = text
#     def send(self):
#         print(f"{self.showHeader()}\n{self.text}\n")
#
# class StickerMessage(Message):
#     def __init__(self, sender: str, recipien: str, sticker: str):
#         super().__init__(sender, recipien)
#         self.sender = sender
#         self.recipien = recipien
#         self.sticker = sticker
#         self.count = 1
#     def send(self):
#         print(f"{self.showHeader()}\n{self.sticker}\nСообщение было прочитано {self.count} раз\n")
#         self.count += 1
#
# textMes = TextMessage(sender="Evgeny", recipien="Darya", text="How are you")
# textMes.send()
#
# stickMes = StickerMessage(sender="Darya", recipien="Evgeny", sticker="ʕ•́ᴥ•̀ʔっ")
# stickMes.send()
# stickMes.sticker = "(─‿‿─"
# stickMes.send()


# Task3
# class MSDice:
#     def __init__(self, edge):
#         self.edge = edge
#         self.currentvalue = random.randint(1, self.edge)
#     def throw(self):
#         self.currentvalue = random.randint(1, self.edge)
#     def __str__(self):
#         return f"Кубик с {self.edge} гранями. Текущее значение {self.currentvalue}"
#
# class D4(MSDice):
#     def __init__(self):
#         super().__init__(edge=4)
# class D6(MSDice):
#     def __init__(self):
#         super().__init__(edge=6)
# class D10(MSDice):
#     def __init__(self):
#         super().__init__(edge=10)
# class D20(MSDice):
#     def __init__(self):
#         super().__init__(edge=20)
#
# dice4 = D4()
# dice6 = D6()
# dice10 = D10()
# dice20 = D20()
# for el in (dice4, dice6, dice10, dice20):
#     el.throw()
#     print(el)


# Task 4
# class Player:
#     def __init__(self, nickname):
#         self.nickname = nickname
#         self.exp_points = 0
#         self.inventory = []
#     def addExp(self, exp):
#         self.exp_points += exp
#     def addItem(self, item):
#         self.inventory.append(item)
#     def removeItem(self, item):
#         index = self.inventory.index(item)
#         self.inventory.pop(index)
#     def __str__(self):
#         return f"Player: {self.nickname}. Exp points: {self.exp_points}\nInventory: {self.inventory}"
#
# player1 = Player(nickname="Johne Doe")
# player1.addExp(500)
# player1.addItem("Knife")
# player1.addItem("Pistol")
# player1.addItem("Vodka")
# player1.removeItem("Knife")
# print(player1)


# Task 5
# from functools import reduce
# class Resistors:
#     def parallel(self, r1, r2):
#         return r1 + r2
#     def consec(self, lst: list):
#         return reduce(lambda acc, cur: acc*cur, lst)/sum(lst)
#
# res = Resistors()
# print(res.consec([5, 6, 12, 22]))
# print(res.parallel(5, 10))
