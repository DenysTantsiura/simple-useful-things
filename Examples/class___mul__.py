""" DZ!
Реалізувати клас-список (list) у якому множення перевизначено як скалярне множення векторів
У випадку n-вимірного простору скалярний добуток векторів a = {a1 ; a2 ; ... ; an} і b = {b1 ; b2 ; ... ; bn} можна знайти скориставшись наступною формулою:

a · b = a1 · b1 + a2 · b2 + ... + an · bn
"""
from collections import UserList


class MyList(UserList):
    def __init__(self, data):
        if isinstance(data, list):
            self.data = data
        else:
            print('Need list on Enter! []')
            self.data = []

    def __mul__(self, other):
        if isinstance(other, list) and len(other) == len(self.data):
            return sum([self.data[i]*other[i] for i in range(len(other))])
        else:
            raise ValueError


b = [1, 2, 3]

a = MyList([1, 2, 3])

print(a*b)
#---------------------------------------------------------------------
