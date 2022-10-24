def decor1(func1):
    dict ={}
    def indecor(val1):
        print("start")
        if val1 in dict:
            return dict[val1]
        result = func1(val1)
        dict[val1] = result
        print("finish")
        
        return result
    
    return indecor


@decor1
def func(num_1):
    print("calculating...")
    return num_1**10


print(func(1))
print(func(2))
print(func(3))
print(func(1))
print(func(2))
