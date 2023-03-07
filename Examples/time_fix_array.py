from array import array
import pickle
import time
#from time import time
#from timeit import default_timer


start = time.time()
int_array = array('i', range(0, 1000000))
print(time.time() - start)

start = time.time()
int_list = list(range(0, 1000000))
print(time.time() - start)

start = time.time()
[i**2 for i in int_array]
print(time.time() - start)

start = time.time()
[i**2 for i in int_list]
print(time.time() - start)

start = time.time()
pickle.dumps(int_array)
print(time.time() - start)

start = time.time()
pickle.dumps(int_list)
print(time.time() - start)


def check_performance(func):

    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        print(time() - start)
    return wrapper


@check_performance
def func1():
    pass


"""
from time import time


def check_performance(a):

    def inner_function(func):
        print(a)

        def wrapper(*args, **kwargs):
            start = time()
            func(*args, **kwargs) # OR return func(*args, **kwargs)
            print(time() - start) # return result
        return wrapper

    return inner_function


@check_performance
def func1():
    pass


@check_performance(1)
def func2():
    pass

"""


def format_ingredients(data):
    last = data.pop(-1)
    last1 = data.pop(-1)
    data.insert(len(data), f"{last1} and {last}")
    data1 = ""
    for el in data:
        data1 = data1 + " " + el + ","
    data1 = data1[:-1]
    return data1


print(format_ingredients(['ab c', 'de f', 'gh j', '1 23', 'qwerty']))
print(format_ingredients(['фіф', 'qwe']))


def format_ingredients1(items):
    # return items.join
    if len(items) == 1:
        return str(items[0])
    elif len(items) < 1:
        return ''
    itwol = items[0:-2]
    vstrit = ''
    for i in itwol:
        vstrit += (str(i) + ', ')
    vstrit += (str(items[-2]) + ' and ' + str(items[-1]))
    return vstrit


print(format_ingredients1([]))
