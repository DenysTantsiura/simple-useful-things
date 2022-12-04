import time

'''
# bad var of recu
def f(x):
    return 0 if x == 0 else (f(x-1)+f(x-2)) if x > 1 else 1
'''

def fibon(fun):

    dict_fibo = {}

    def wrap(value):

        if value in dict_fibo:
            return dict_fibo[value]
        
        result = fun(value)
        dict_fibo[value] = result
        # print(dict_fibo)

        return result

    return wrap


@fibon
def fib(n):
    
    if n == 0:
        return 0
    
    elif n in (1, 2):
        return 1
    
    return fib(n-1) + fib(n-2)


def fibonachi_counter(number: int) -> int:
    
    if number == 0:
        return 0
    
    elif number in (1, 2):
        return 1
    
    return fibonachi_counter(number-1) + fibonachi_counter(number-2)


# print([fib(i) for i in range(12)])
print([fibonachi_counter(i) for i in range(12)])


def fibonachi_counter2(number: int) -> int:
    
    element_1, element_2 = 0, 1
    for element in range(number):
        element_1, element_2 = element_2, element_1 + element_2

    return element_1


print([fibonachi_counter2(i) for i in range(12)])

limit = 500

start = time.time()
print(fib(limit))  # print(fibonachi_counter(42)) # 42 = > 82s
print(time.time() - start)

start = time.time()
print(fibonachi_counter2(limit))  # 42 = > 3/10000 s
print(time.time() - start)

# ======================
# Of course Fibonacci numbers can be computed in O(n) by applying the Binet formula:

from math import floor, sqrt

def fib(n):                                                     
    return int(floor(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))+0.5))
# As the commenters note it's not O(1) but O(n) because of 2**n. Also a difference is that you only get one value, while with recursion you get all values of Fibonacci(n) up to that value.

print(fib(5))
# ================================
# If you want to get only few Fibonacci numbers, you can use matrix method.

from numpy import matrix

def fib(n):
    return (matrix('0 1; 1 1', dtype='object') ** n).item(1)
# It's fast as numpy uses fast exponentiation algorithm. You get answer in O(log n). And it's better than Binet's formula because it uses only integers. But if you want all Fibonacci numbers up to n, then it's better to do it by memorisation.

print(fib(5))
# ===============================
# We can do that using @lru_cache decorator and setrecursionlimit() method:

import sys
from functools import lru_cache

sys.setrecursionlimit(15000) #15000


@lru_cache(128)
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n - 2) + fib(n - 1)


print(fib(5)) # 14000
# =====================================
# As @alex suggested, you could use a generator function to do this sequentially instead of recursively.

# Here's the equivalent of the code in your question: !!!(for python 2.7??? xrange
# wrong!!!!!!!!!!!!!
def fib(n):
    def fibseq(n):
        """ Iteratively return the first n Fibonacci numbers, starting from 0. """
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b

    return sum(v for v in fibseq(n))

# print format(fib(1000), ',d')  # -> no recursion depth error if fib(100000)
print(fib(1000))

# ======================================

# Use generators?  for python

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibs = fib() #seems to be the only way to get the following line to work is to
             #assign the infinite generator to a variable

f = [next(fibs) for x in range(101)]

for num in f:
    print(num)
# ================================
# Many recommend that increasing recursion limit is a good solution however it is not because there will be always limit. Instead use an iterative solution.

def fib(n):
    
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
        
    return a

print(fib(5))
# ======================================

import sys
sys.setrecursionlimit(1500)

def fib(n, sum):
    if n < 1:
        return sum
    else:
        return fib(n-1, sum+n)

c = 998
print(fib(c, 0))
# ========================================

# We could also use a variation of dynamic programming bottom up approach

def fib_bottom_up(n):

    bottom_up = [None] * (n+1)
    bottom_up[0] = 1
    bottom_up[1] = 1

    for i in range(2, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]

    return bottom_up[n]

print(fib_bottom_up(200)) # 20000
# ==========================================
# ==========================================


from time import time

n = 37  # 12 # 37

fibo_cycle = time()
def fibonacci(n):
    a, b = 0, 1
    if n == 0:
        return a
    for item in range(n):
        a, b = b, a + b
    return a

print('fibo_cycle:')
print(fibonacci(n))
print(-fibo_cycle + time())


fibo_recursion_cache = time()
cashe = {}
def fiborc(n):
    if cashe.get(n, None):
        return cashe[n]
    if n == 0:
        cashe[n] = n
        return 0
    if n in (1, 2):
        cashe[n] = 1
        return 1
    cashe[n] = fiborc(n-1) + fiborc(n-2)
    #return fiborc(n-1) + fiborc(n-2)
    return cashe[n]

print('fibo_recursion_cache:')
print(fiborc(n))
print(-fibo_recursion_cache + time())

fibo_recursion_cache2 = time()
print(fiborc(n+1))
print(-fibo_recursion_cache2 + time())

fibo_recursion = time()
def fibor(n):
    if n == 0:
        return 0
    if n in (1, 2):
        return 1
    return fibor(n-1) + fibor(n-2)

print('fibo_recursion:')
print(fibor(n))
print(-fibo_recursion + time())

fibo_generator = time()
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()
for item in range(n):
    next(f)
print('fibo_generator:')    
print(next(f))
print(time() - fibo_generator)









