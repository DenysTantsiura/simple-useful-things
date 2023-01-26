import logging
from random import shuffle
# from time import time
from timeit import default_timer


logging.basicConfig(level=logging.DEBUG, format="%(threadName)12s %(message)90s")


def duration(fun):
    def inner(*args, **kwargs):
        start = default_timer()
        rez = fun(*args, **kwargs)
        logging.info(f"Args:{args}, {default_timer()-start=} sec")

        return rez

    return inner


@duration
def function_shuffle(variable):
    shuffle(variable)
    variable = variable[::-1]
    shuffle(variable)
    return variable


def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # print(default_timer())
    print(function_shuffle(input_list))


if __name__ == "__main__":
    main()
