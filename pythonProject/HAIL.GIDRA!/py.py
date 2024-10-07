# from random import randint as rand
#
# spis = [i for i in range(10)]
# spis = [rand(-30, 30) for i in range(10)]
# cauntNega = 0
# cauntEven = 0
# cauntOdd = 0
# min1 = min(spis)
# max1 = max(spis)
# res3 = 1
# pros = 1
# print(spis)
# for j in range(len(spis)):
#     if spis[j] < 0:
#       cauntNega += 1
#     if spis[j] % 2 == 0:
#       cauntEven += 1
#     elif spis[j] != 0:
#         cauntOdd += 1
# for b in range(len(spis)):
#     if b % 3 == 0:
#         res3 *= spis[b]
# # for d in range(min1, max1):
# #         pros *= spis[d]
# print(f'Отрицательных чисел: {cauntNega}')
# print(f'Четные: {cauntEven}')
# print(f'Нечетные: {cauntOdd}')
# print(f'Произведение с индексами кратные трем: {res3}')
# print(f'Произведение чисел между min и max: {pros}')
#4 числа,
# devoperation4(value1, value2, value4, value4):
#2

# def operation4(value1, value2, value3, value4 ):
#  print(f'Max: {max(value1, value2, value3, value4)}')
#  print(f'Min: {min(value1, value2, value3, value4)}')
#  print(f'Sum: {(value1 + value2 + value3 + value4)}')
#  print(f'MediumA: {(value1 + value2 + value3 + value4) / 4}')
#
# value1 = int(input('Введите второе число: '))
#
# value2 = int(input('Введите первое число: '))
#
# value3 = int(input('Введите третье число: '))
#
# value4 = int(input('Введите четвертое число: '))
#
# operation4(value1, value2, value3, value4)

#3

# def line(string, k):
#     return string * k
# a = input('Enter sim: ')
# b = int(input('How much duplication: '))
# print(f'{line(a, b)}\n\t')

# def line(string, k):
#     s = ' '
#     for i in range(k):
#         s += string + "\n"
#     return s
# a = input('Enter sim: ')
# b = int(input('How much duplication: '))
# print(line(a, b))

# def sum(par1, par2):
#     if par1 > par2:
#         par1,par2 = par2,par1
#     summ = 0
#     for i in range(par1, par2):
#        summ += i
#     return summ
# par1 = int(input(''))
# par2 = int(input(''))
# print(sum(par1, par2))

def lep(digit):
        if int(digit[0]) +  int(digit[1]) +  int(digit[2]) == int(digit[-1]) +  int(digit[-2]) +  int(digit[-3]):
         return digit
        print(f'd {lep(digit)}')
digit = (input())
