"""
Написати програму на Пайтоні для сортування списку кортежів з використаннм лямбда-функції.
Приклад:
[('Math', 98),('Lab', 96),('Info', 99),('Core', 95),]
out:
[('Core', 95),('Lab', 96),('Math', 98),('Info', 99),]
"""

import logging
from timeit import default_timer


logging.basicConfig(level=logging.DEBUG, format="%(threadName)12s %(message)90s")


def duration(fun):
    def inner(*args, **kwargs):
        start = default_timer()
        logging.info(f"Start with Args:{args}")
        rez = fun(*args, **kwargs)
        logging.info(f"Args:{args}, {default_timer()-start=} sec")

        return rez

    return inner


@duration
def function(subj: list) -> list:
    subj.sort(key = lambda x: x[1])
    return subj


def main():

    print(default_timer())
    print(function([('Math', 98),('Lab', 96),('Info', 99),('Core', 95),]))
    

if __name__ == "__main__":
    main()
