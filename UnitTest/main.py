class Person:
    def __init__(self):
        self.name = None
        self.age = 25

    def print_age(self):
        return self.age

def ff():
    p = Person()
    print(f"\nМеня зовут {p.name}")
    print(f"Мой возраст {p.print_age()}")
