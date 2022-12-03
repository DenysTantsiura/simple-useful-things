"""
Протокол ітератора в Python реалізований методом __iter__. Цей метод має повертати ітератор.
Ітератором може бути будь-який об'єкт, який має метод __next__, який при кожному виклику повертає значення.
Щоб створити ітератор, достатньо реалізувати метод __next__.
"""
"""
Реалізуємо ітератор, який виконує ітерацію задану кількість разів по заданій послідовності
"""
from random import randint

class PartIterator:

    def __init__(self, sequence, quantity):
        self.sequence = sequence
        self.quantity = quantity if len(sequence) >= quantity else len(sequence)  # Необіхніда кількість
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.quantity > 0:
            res = self.sequence[0]
            self.sequence.pop(0)
            self.quantity -= 1
            return res
        raise StopIteration

my_random_list = PartIterator([7,8,9,10,11,12,13], 5)

for item in my_random_list:

    print(item, end=" ")

print('-'*100)

class PartIterator2:

    def __init__(self, sequence, quantity):
        self.sequence = sequence
        self.quantity = quantity # if len(sequence) >= quantity else len(sequence)  # Необіхніда кількість
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.quantity > 0:
            self.quantity -= 1
            try:
                return self.sequence.pop(0)
            except Exception as err:
                print(f'END: {err}')

        raise StopIteration
                

my_random_list2 = PartIterator2([7,8,9,10,11,12,13], 8)

for item in my_random_list2:

    print(item, end=" ")



class PartIterator3:

    def __init__(self, sequence, quantity):
        self.sequence = sequence
        self.quantity = quantity
        self.copy_sequence = sequence[:]

    def __iter__(self):
        return self

    def __next__(self):
        if not len(self.copy_sequence):
            self.copy_sequence = self.sequence[:]
        if self.quantity > 0:
            self.quantity -= 1
            try:
                return self.copy_sequence.pop(0)
            except Exception as err:
                print(f'END: {err}')

        raise StopIteration
                

my_random_list3 = PartIterator3([7,8,9,10,11,12,13], 22)

for item in my_random_list3:

    print(item, end=" ")
