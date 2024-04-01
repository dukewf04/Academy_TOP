# Общий синтаксис
# lambda parameters: expression
# parameters - переменные через запятую
# expression - условие, в котором нельзя использовать циклы, только условные вырожения, нельзя вызывать return!
# Результатом выполнения lambda выражения является анонимная функция. При вызове которой вычисляется значения при указанных параметрах.

# Example 1
# string = lambda x: "k" if x == 1 else "s"
# print(string(2))


# Example 2
# def area1(b, h):
#     return 0.5 * b * h
# print("area1", area1(6,5))
#
# area2 = lambda b, h: 0.5 * b * h
# print("area2", area2(6, 5))


# Example 3
# elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
# elements.sort(key=lambda e: (e[1], e[2]))
# elements.sort(key=lambda e: (e[0], e[1]))
# # elements.sort(key=lambda e: e[1:3])
# # elements.sort(key=lambda e: (e[2].lower(), e[1]))
# print(elements)


# Example 4
# c = lambda x=1, y=2, z=3: x + y + z
# print(c())


# Example 5
# y = lambda: 2 + 3
# print(y())

#-------------------------------------
# Работа со встроенными функциями
#-------------------------------------
from functools import reduce

list1 = [0, 1, 2, 3]
list2 = list(filter(lambda x: x%3 == 0, list1))
print(list2)

list3 = list(map(lambda x: x%3 == 0, list1))
print(list3)

# reduce - сводит элементы последовательности к одному значению. Принимает 2 аргумента: фукнцию и последовательность.
list4 = reduce(lambda x, y: y-x, list1)
print(list4)

def add(x, y):
    return x + y

summa = reduce(add, list1)
print(summa)