# class Programmer:
#     __doljnost_list = {
#         'Junior': 10,
#         'Middle': 15,
#         'Senior': 20,
#     }
#     def __init__(self, name: str, doljnost: str):
#         self.name = name
#         self.doljnost = doljnost
#         self.oklad = self.__doljnost_list[doljnost]
#         self.work_hours = 0
#
#
#     def work(self, time: int):
#         self.work_hours += time
#
#     def rise(self):
#         key_list = tuple(self.__doljnost_list.keys())
#         cur_index = key_list.index(self.doljnost)
#         if self.doljnost == 'Senior':
#             self.oklad += 1
#         else:
#             self.doljnost = key_list[cur_index+1]
#             self.oklad = self.__doljnost_list[self.doljnost]
#
#     def info(self):
#         print(f"{self.name}, должность {self.doljnost}, оклад {self.oklad}, количество отработанных часов {self.work_hours}. Накопленная зарплата {self.oklad * self.work_hours} тгр.")
#
#
# programmer1 = Programmer(name="Max", doljnost='Middle')
#
# programmer1.work(time=50)
# programmer1.info()
#
# programmer1.work(2)
# programmer1.rise()
# programmer1.info()
#
# programmer1.work(20)
# programmer1.rise()
# programmer1.rise()
# programmer1.rise()
# programmer1.info()
import random


# class NPC:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
#     def __str__(self):
#         return f"Имя: {self.name}, Очки здоровья: {self.hp}"
#
#     def attack(self):
#         return "NPC наносит урон"

# class SwordMan(NPC):
#     def __init__(self, name, hp, min_damage, max_damage):
#         super().__init__(name, hp)
#         self.name = name
#         self.hp = hp
#         self.min_damgae = min_damage
#         self.max_damage = max_damage
#
#     def attack(self):
#         damage = random.randint(self.min_damgae, self.max_damage)
#         return damage
#
#     def __str__(self):
#         print(super().__str__())
#         return f"Мечник {self.name} нанёс {self.attack()} урона!"
#
#
# class Mage(NPC):
#     def __init__(self, name, hp, mana: int):
#         super().__init__(name, hp)
#         self.name = name
#         self.hp = hp
#         self.mana = mana
#
#     def attack(self):
#         damage = self.mana*2
#         return damage
#
#     def __str__(self):
#         print(super().__str__())
#         if self.mana != 0:
#             return f"Маг {self.name} нанёс {self.attack()} урона!"
#         else:
#             return "Не могу атаковать! Мана закончилась"
#
#
# sword1 = SwordMan(name="Бильбо", hp=20, min_damage=2, max_damage=30)
# sword2 = SwordMan(name="Арагорн", hp=45, min_damage=40, max_damage=60)
# mage1 = Mage(name="Гендальф", hp=50, mana=20)
# mage2 = Mage(name="Мега Маг", hp=60, mana=0)
#
# print(sword1, '\n')
# print(sword2, '\n')
#
# print(mage1, '\n')
# print(mage2, '\n')
