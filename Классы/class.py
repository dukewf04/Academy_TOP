class ExampleClass:
    counter = 0
    def __init__(self, val=1):
        self.__first = val
        self.__second = 0
        self.__third = 0
        ExampleClass.counter += 1

    def setSecond(self, val):
        self.__second = val

    def __str__(self):
        return f"{self.__first}, {self.__second}, {self.__third}"

example1 = ExampleClass()
print(example1.__dict__, example1.counter)

example2 = ExampleClass(2)
example2.setSecond(3)
print(example2.__dict__, example2.counter)

example3 = ExampleClass(4)
example3.__third = 5
print(example3.__dict__, example3.counter)

# Преобразование объекта в строку
print(example3)

#-----------------------------------------------------------
class ExampleClass2:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example4 = ExampleClass2(1)
print(example4.a)
try:
    print(example4.b)
except AttributeError:
    pass