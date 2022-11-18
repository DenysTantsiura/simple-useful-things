def decor1(func1):
    dict = {}

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


def decorator(func):
    def inner(*args, **kwargs):
        print('Func decorator')
        return func(*args, **kwargs)
    return inner


@decorator
def func0():
    print('hello Den')


func0()

# or other Style:


class Decorator:
    def __call__(self, func):
        def inner(*args, **kwargs):
            print('Class decorator')
            return func(*args, **kwargs)
        return inner


@Decorator()
def func():
    print('hello Den')


func()
# ____________________________________________


class Decorator:

    def __init__(self, arg):
        self.arg = arg

    def __call__(self, func):
        def inner(*args, **kwargs):
            print(f'Class decorator {self.arg}')
            return func(*args, **kwargs)
        return inner


@Decorator(123)
def func():
    print('hello world')


func()

# _______________________


def thr_decorator(min_val, max_val):
    def check(func):
        def inner(*args):
            for arg in args:
                if arg < min_val or arg > max_val:
                    raise ValueError
            return func(*args)
        return inner
    return check


@thr_decorator(0, 5)
def foo(x, y):
    pass


@thr_decorator(-5, 0)
def baz(x, y):
    pass
