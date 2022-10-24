class Iterable:

    def __init__(self):
        self.my_list = [1, 2, 3, 4]
        self.index = 0

    def __next__(self):
        if self.index >= len(self.my_list):
            raise StopIteration

        element = self.my_list[self.index]
        self.index += 1
        return element

    def __iter__(self):
        return self


iterable = Iterable()
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))

# ==============================


def iterator(): # generator ?
    index = 0
    a = [1, 2, 3]
    while index < len(a):
        yield a[index]
        index += 1
    raise StopIteration

b = iterator()
print(next(b))
print(next(b))
print(next(b))

# ==============================

a = [i for i in range(10)] # list
print(a)

a = (i for i in range(10)) # generator
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(tuple(a)) # tuple -> (4, 5, ... 9)
# ===============================
class AddressBook:

    def __init__(self):

        self.page_size = 10
        self.offset = 0
        self.addresses = list(range(31))

    def __next__(self):
        self.offset += self.page_size
        if self.offset > len(self.addresses):
            raise StopIteration
        return self.addresses[self.offset-self.page_size:self.offset]

    def __iter__(self):
        return self


ad_book = AddressBook()
print(next(ad_book))
print(next(ad_book))
print(next(ad_book))
