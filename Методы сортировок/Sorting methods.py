import time
from random import randint

# Декоратор для определения времени выполнения программы
def get_func_time(func):
    def wrapper(*args, **kwargs):
        startt = time.time()
        func(*args, **kwargs)
        endt = time.time()
        print(f"Время работы функции: {endt-startt} секунд")

    return wrapper

# Сортировка средствами Python
@get_func_time
def standart_sort(list1):
    list1.sort()

# Сортировка методом пузырька
@get_func_time
def bubble_sort(list1):
    # Обеспечивает выход из цикла, если список уже отсортирован
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
                swapped = True

# Сортировка вставками
@get_func_time
def insert_sort(list1):
    for i in range(1, len(list1)):
        item_to_insert = list1[i]
        j = i-1
        while j>=0 and list1[j] > item_to_insert:
            list1[j+1] = list1[j]
            j-=1
        list1[j+1] = item_to_insert

# ---------------------Метод выборки -----------------------------------------
@get_func_time
def select_sort(list1):
    for i in range(0, len(list1)-1):
        smallist = i
        for j in range(i+1, len(list1)):
            if list1[j] < list1[smallist]:
                smallist = j
        list1[i], list1[smallist] = list1[smallist], list1[i]

# Метод пирамидальной сортировки (кучей)
def heapify(nums, heap_size, root_index):
    # Индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2 * root_index)+1
    right_child = (2 * root_index)+2
    # Если левый потомок корня - допустимый индекс, а элемент больше,
    # чем текущий наибольший, то обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

@get_func_time
def heapsort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
# ------------------------------------------------------------------------

# ----------- Метод сортировки слиянием ----------------------------------
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = 0
    right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for i in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            #Сравниваем первые элементы в начале каждого списка
            #Если первый элемент левого подспика меньше, добавляем его
            # в отсортированный список
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            #если первый элемент прового списка меньше, то добавляем его
            #в отсортированный список
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        #Если достигнут конец левого списка, элементы правого списка
        #добавляются в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        #Если достигнут конец правого списка, элементы левого списка
        #добавляются в конец результирующего списка
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(list1):
    #Возвращаем список, если в нем 1 элемент
    if len(list1) <= 1:
        return list1
    #находим середину списка
    mid = len(list1)//2
    #Сортируем и объединяем подсписки
    left_list = merge_sort(list1[:mid])
    right_list = merge_sort(list1[mid:])
    #Объединяем и возвращаем один список
    return merge(left_list, right_list)
# ----------------------------------------------------------------------


# ------------------ Метод быстрой сортировки -----------------------------
def partition(list1, low, high):
    # Выбираем средний элемент как опорный
    pivot = list1[(low + high)//2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while list1[i] < pivot:
            i += 1
        j -= 1
        while list1[j] > pivot:
            j -= 1
        if i >= j:
            return j
        list1[i], list1[j] = list1[j], list1[i]
@get_func_time
def quick_sort(list1):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index+1, high)
    _quick_sort(list1, 0, len(list1)-1)
# --------------------------------------------------------------------------

# Сортировка методом Шелла
@get_func_time
def shellsort(list1):
    nlen = len(list1)
    k = int(math.log2(nlen))
    interval = 2**k-1
    while interval > 0:
        for i in range(interval, nlen):
            temp = list1[i]
            j = i
            while j >= interval and list1[j-interval] > temp:
                list1[j] = list1[j-interval]
                j -= interval
            list1[j] = temp
        k -= 1
        interval = 2**k - 1
    return list1

list_1 = [randint(-9999, 9999) for i in range(100000)]
# print('До:', list_1)
# bubble_sort(list_1)
# insert_sort(list_1)
# select_sort(list_1)
# heapsort(list_1)
# standart_sort(list_1)
# print(merge_sort(list_1))
quick_sort(list_1)
# print('После:', list_1)



