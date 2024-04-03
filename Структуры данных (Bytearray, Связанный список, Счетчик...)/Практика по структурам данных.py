class MyList:
    def __init__(self, lst: list):
        self.mylist = lst
    def addElement(self, num):
        if num in self.mylist:
            print("Такое число уже есть в списке!")
        else:
            self.mylist.append(num)
        print(self.mylist)
    def delElement(self, num):
        while num in self.mylist:
            self.mylist.remove(num)
        print(self.mylist)
    def showList(self, reversed: int = 1):
        # Протестировать, так как список может сохранить свое состояние после reverse
        if reversed == 1:
            print(self.mylist)
        else:
            for i in range(len(self.mylist)):
                print(self.mylist[-(i+1)], end=" ")
            print()
    def isElement(self, num):
        if num in self.mylist:
            print(f"Элемент {num} есть в списке")
        else:
            print(f"Элемента {num} нет в списке")
    def replaceElement(self, old, new, all: int = 1):
        for i in range(len(self.mylist)):
            if self.mylist[i] == old:
                self.mylist[i] = new
                if all == 1: break
        print(self.mylist)

lst = list(map(int, input("Введите список чисел через пробел> ").strip().split()))
lst = MyList(lst)

while True:
    print("[1] Добавить новое число в список")
    print("[2] Удалить все вхождения числа из списка")
    print("[3] Показать содержимое списка")
    print("[4] Проверить есть ли значение в списке")
    print("[5] Заменить значение в списке")
    print("[0] Выход")

    choise = int(input("> ").strip())
    if choise == 0: break

    if choise == 1:
        num = int(input("Введите новое число> "))
        lst.addElement(num)
    elif choise == 2:
        num = int(input("Введите число> "))
        lst.delElement(num)
    elif choise == 3:
        r = int(input("1 - c начала, 2 - с конца списка> "))
        lst.showList(reversed=r)
    elif choise == 4:
        num = int(input("Введите число> "))
        lst.isElement(num)
    elif choise == 5:
        old = int(input("Введите заменяемое число> "))
        new = int(input("Введите новое число> "))
        b = int(input("1 - Заменить только первое вхождение, 2 - Заменить все вхождения> "))
        lst.replaceElement(old=old, new=new, all=b)
    print("*"*30)