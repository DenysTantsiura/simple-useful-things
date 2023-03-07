from  concurrent.futures import ThreadPoolExecutor
import logging
from random import randint
from time import sleep, time
import multiprocessing
# import psutil
from threading import Thread


# max_threads = psutil.cpu_count()
max_relevant_threads = multiprocessing.cpu_count()

def greeting(name):
    logging.debug(f"greeting for: {name}")
    sleep(randint(0, 1))
    return f"Hello {name}"


def greeting2(name, number=time()):
    logging.debug(f"greeting for: {name}")
    sleep(randint(1, 3))
    print(f"N: {name}, #:{number}")


arguments = (
    "Bill",
    "Jill",
    "Till",
    "Sam",
    "Tom",
    "John",
)


def fun(a):
    logging.debug(f"Start element for: {a}")
    sleep(randint(0, a[0]**2))
    logging.debug(f"End element for: {a}")
    if len(a) > 1:
        # if len(a) > 2:
        #     print(a[0] + fun(a[1:]))
        return a[0] + fun(a[1:])
    return a[0]


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    print(f'MAX FLOWS: {max_relevant_threads}\n')
    with ThreadPoolExecutor(max_workers=max_relevant_threads) as executor:
        results = list(executor.map(greeting, arguments))

    with ThreadPoolExecutor(max_workers=max_relevant_threads) as executor2:
        executor2.map(greeting2, [1], [2])
        # for i in range(10):
        #     executor2.submit(greeting2, i, i*i).result()

    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # for i in range(len(a)):
    #     fun(a)
    rez = []
    executor3 = ThreadPoolExecutor(max_workers=max_relevant_threads)
    # for i in range(len(a)):
    #     # print(f'SUM(a): {fun(a[i:])}')
    #     # print(f'SUM(a): {list(executor3.map(fun, [a[i:]]))}')
    #     executor3.map(fun, [a[i:]])

    for i in range(6):
        thread = Thread(target=fun, args=([i],))
        thread.start()

    logging.debug(results)
