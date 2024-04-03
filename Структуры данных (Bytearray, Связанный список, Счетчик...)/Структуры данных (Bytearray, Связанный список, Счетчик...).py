# 1. Bytearray, принимает числа в диапазоне 0 <= x < 256
# a = bytearray((12, 7, 5, 3, 255))
# a.append(10)
# a.append(30)
# print(a)


# 2. Счетчик (Counter)
from collections import Counter
# print(Counter(["A", "B", "C", "D"]))

# counter = Counter({"A": 1, "B": 2, "C": 3})
# counter.update(["A"])
# counter.update(["A"])
# counter.update("B")
# counter.update("B")
# print(counter["B"])


# 3. DefaultDict
# from collections import defaultdict
# dict1 = defaultdict(int)
# list1 = [1, 2, 3, 4, 5, 6]
# for i in list1:
#     dict1[i] += i
# print(dict1)


# 4. ChainMap
# from collections import ChainMap
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4}
# d3 = {"e": 5, "f": 6}
# c = ChainMap(d1, d2, d3)
# print(c)
# print(c["a"])
# print(c["b"])


# 5. Связанный список
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def printList(self):
#         temp: Node = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.next
#
# # Создание элементов
# list = LinkedList()
# list.head = Node(1)
# second = Node(2)
# third = Node(3)
#
# # Ссылки на следующие элементы
# list.head.next = second
# second.next = third
#
# # Обход элементов
# list.printList()


# 6. Стек списком
# stack = []
# stack.append("g")
# stack.append("V")
# stack.append("C")
#
# print("Реализация стека:", stack)
# print("Удаление элементов в стеке:")
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# print("Стек очищен!")


# 7. Стек коллекцией
# from collections import deque
# stack = deque()
# stack.append("g")
# stack.append("V")
# stack.append("C")
#
# print("Реализация стека:", stack)
# print("Удаление элементов в стеке:")
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# stack.pop()
# print(stack)
# print("Стек очищен!")


# 8. Стек с использованием модуля очереди
# from queue import LifoQueue
# stack = LifoQueue(maxsize=3)
# print(stack.qsize())
# # Заполнение стека
# stack.put("g")
# stack.put("c")
# stack.put("s")
# # Вывод данных стека
# print("Весь стек:", stack.full())
# print("Размер стека:", stack.qsize())
# # Освобождение стека
# print(stack.get())
# print(stack.get())
# print(stack.get())
# print(stack.empty())


# 9. Очередь с приоритетом
class VipQueue(object):
    def __init__(self):
        self.queue = []
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return len(self.queue) == 0
    def insert(self, data):
        self.queue.append(data)
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

myQueue = VipQueue()
myQueue.insert(12)
myQueue.insert(5)
myQueue.insert(50)
myQueue.insert(3)
myQueue.insert(50)
print(myQueue)

while not myQueue.isEmpty():
    print("Удалил ", myQueue.delete())
    print("Текущий список:", myQueue)
