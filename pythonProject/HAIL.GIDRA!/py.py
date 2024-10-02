from random import randint as  rand

list = [i for i in range(10)]
print(list)
list = [rand(-20, 20) for i in range(10)]
print(list)

caunt = 0
caunt2 = 0
caunt3 = 0
res = 1
res1 = 1
min1 = min(list)
max1 = max(list)
for j in range(len(list)):
    if list[j] < 0:
        caunt += list[j]
    if list[j] % 2 == 0:
        caunt2 += list[j]
    elif list[j] % 2 != 0:
        caunt3 += list[j]
    if j % 3 == 0:
         res *= list[j]
    for b in range(min1, max1):
          res1 *= list[j]

print(caunt)
print(caunt2)
print(caunt3)
print(res)
print(res1)