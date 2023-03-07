from multiprocessing import Queue, Process, current_process
from time import sleep
import sys
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

q = Queue()


def worker(queue: Queue):
    name = current_process().name
    logger.debug(f"{name} started...")
    val = queue.get()
    logger.debug(f"{name} {val**2}")
    sys.exit(0)


if __name__ == "__main__":
    # w1 = Process(target=worker, args=(q,))
    # w2 = Process(target=worker, args=(q,))
    # w3 = Process(target=worker, args=(q,))
    # #w4 = Process(target=worker, args=(q,))

    w = {}
    for i in range(8):
        w[i] = Process(target=worker, args=(q,))
        w[i].start()

    q.put(2)
    sleep(2)
    q.put(4)
    q.put(5)
    q.put(6)
    q.put(8)
    sleep(3)
    q.put(16)

    print("Finish?")
