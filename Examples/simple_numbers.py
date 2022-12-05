# Simple numbers < 1000

from functools import reduce
from time import time

LIMIT = 10000 # in (1,100000) = 9593 simple numbers; in (1,10000) = 1230 simple numbers
QUANTITY = 1230  # 9593  # 1230

start1 = time()
print([1]+list(filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,
map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,LIMIT)))))
print(time() - start1)

# need twice as fast?
start1 = time()
print(list(filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0,
map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(1,LIMIT, 2)))))
print(time() - start1)

# need even faster?
start1 = time()
def simple_numbers2(right_boundary: int):
    res = [1, 2]
    
    def simpl(num):
        for item in range(2, int(pow(num, 0.5) + 1)):
            if num % item == 0:
                return False
        return num

    res += [num for num in range(3, right_boundary, 2) if simpl(num)]
                
    return res

print(simple_numbers2(LIMIT))
print(time() - start1)

# print(len(simple_numbers2(LIMIT)))

# generator
start1 = time()
def simple_number_generator(num: int = 0):
    while True:
        num += 1
        max_devider = int(pow(num, 0.5))
        item = 1
        for item in range(2, max_devider+1):
            if num % item == 0:
                item = None
                break
        if item:
            yield num


g = simple_number_generator()
# print(next(g))
# print(next(g))
print([next(g) for _ in range(QUANTITY)])
print(time() - start1)

# gg = simple_number_generator(1230) # for next simple number after 
# print(next(gg))

# for next simple number after:...

start1 = time()
gg = simple_number_generator(99990)
print(next(gg))
print(time() - start1)

start1 = time()
print(simple_numbers2(100000)[-1]) # 99991
print(time() - start1)
