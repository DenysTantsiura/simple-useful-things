from threading import Thread, RLock
import logging
from time import time, sleep

lock = RLock()


def func(locker, delay):
    timer = time()  # фіксується у всіх потоків "водночас"
    locker.acquire()  # Блокування ресурсу досягається виконанням команди (призупинили одночасне виконання
    sleep(delay)
    locker.release()  # коли потік закінчить роботу із загальним ресурсом, він відпускає lock (дозволили продовження
    logging.debug(f"Done {time() - timer}")


# менеджер контексту
# def func(locker, delay):
#     timer = time()
#     with locker:
#         sleep(delay)
#     logging.debug(f"Done {time() - timer}")

def func1(delay):
    timer = time()
    sleep(delay)
    logging.debug(f"Done: {time() - timer}")
    sleep(delay*5)
    logging.debug(f"Done: {time() - timer}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    logging.debug("Start:") # start time = 0
    # start time = 0.0001
    t1 = Thread(target=func, args=(lock, 1))  # Thread-1
    t2 = Thread(target=func, args=(lock, 2))  # Thread-2
    t3 = Thread(target=func, args=(lock, 2))  # Thread-3
    t2.start()  # 2s
    t3.start()  # 2s -> 4s?
    t4 = Thread(target=func1, args=(0.5,))  # Thread-4
    t4.start()  # 0.5s
    t1.start()  # 1s -> 5s?
    logging.debug("- End") # start time = 0.0000000001
