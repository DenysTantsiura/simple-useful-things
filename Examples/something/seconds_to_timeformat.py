"""
Функція приймає додатнє число, значення секунд, вивести в форматі hh:mm:ss,
наприлад 08:12:02
"""

import logging
from random import shuffle
import random
from time import sleep, time
from timeit import default_timer
import datetime


logging.basicConfig(level=logging.DEBUG, format="%(threadName)12s %(message)90s")


def duration(fun):
    def inner(*args, **kwargs):
        start = default_timer()
        logging.info(f"Input:{args}, {default_timer()-start=} sec")
        rez = fun(*args, **kwargs)
        logging.info(f"Rez:{rez}, {default_timer()-start=} sec")

        return rez

    return inner


@duration
def function(variable):
    variable = str(datetime.timedelta(seconds=variable))
    if variable[1] ==':':
        variable = f'0{variable}'

    return variable if len(variable) == 8 else variable[:8]


def main():
    
    print(int(default_timer()))
    print(int(time()))
    print(f'{function(default_timer())=}')
    print(f'''{function(int(input('Enter seconds: ')))=}''')


if __name__ == "__main__":
    main()
