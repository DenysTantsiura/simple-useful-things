from multiprocessing import JoinableQueue, Process, current_process, cpu_count, Manager
import logging
import sys
from time import time

max_relevant_threads = cpu_count()

logger = logging.getLogger("Logging factorize")
logger.setLevel(logging.DEBUG)
command_line_hendler = logging.StreamHandler()
command_line_hendler.setLevel(logging.DEBUG)
log_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
command_line_hendler.setFormatter(log_formatter)
logger.addHandler(command_line_hendler)


def fix_duration(my_function):
    def inner(*args):
        start = time()
        rezult = my_function(*args)
        print(f"Duration({my_function.__name__}): {time() - start} sec")

        return rezult

    return inner


def all_divisors_of_the_number_1(number: int) -> list:

    if number == 0:
        return []

    subnumber_group = [1]
    for i in range(1, number + 1):  # (number//2)+1
        if number % i == 0:
            subnumber_group.append(i)
    #         subnumber_group.append(int(number / i))
    # 
    # subnumber_group.append(number)
    # subnumber_group.sort()

    return subnumber_group


@fix_duration
def factorize(*numbers):
    logger.debug("START factorize")
    rez = []
    for number in numbers:
        subnumber_group = all_divisors_of_the_number_1(number)
        rez.append(subnumber_group)

    logger.debug("END factorize")

    return rez


@fix_duration
def factorize_1(*numbers):
    logger.debug("START factorize_1")
    rez = []
    for number in numbers:
        subnumber_group = [1]
        for i in range(2,  number + 1):  # (number//2)+1      | int(pow(number, 0.5))
            if number % i == 0:
                subnumber_group.append(i)
        #         subnumber_group.append(int(number / i))
        #
        # subnumber_group.append(number)
        # subnumber_group.sort()
        rez.append(subnumber_group)

    logger.debug("END factorize_1")

    return rez


def all_divisors_of_the_number(
    jqueue: JoinableQueue, return_dict: Manager().dict()
) -> None:
    name = current_process().name
    logger.debug(f"{name} started...")
    number = jqueue.get()

    if number == 0:
        jqueue.task_done()
        return_dict[number] = []

    subnumber_group = [1]
    for i in range(2, number + 1):  # (number//2)+1
        if number % i == 0:
            subnumber_group.append(i)
    #         subnumber_group.append(int(number / i))
    #
    # subnumber_group.append(number)
    # subnumber_group.sort()
    return_dict[number] = subnumber_group
    jqueue.task_done()
    sys.exit(0)


@fix_duration
def factorize_process(*numbers):
    logger.debug("START factorize_process")
    manager = Manager()
    return_dict = manager.dict()

    joinable_queue = JoinableQueue()

    [
        joinable_queue.put(number)
        for number in numbers
        if not Process(
            target=all_divisors_of_the_number, args=(joinable_queue, return_dict)
        ).start()
    ]

    joinable_queue.join()
    logger.debug("END factorize_process")

    return return_dict.values()


if __name__ == "__main__":

    print(f"{max_relevant_threads=}")

    a, b, c, d = factorize_1(20651060, 10651060, 106510600, 206510600)

    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    print(d[-2])

    a, b, c, d = factorize(20651060, 10651060, 106510600, 206510600)

    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    print(d[-2])

    a, b, c, d = factorize_process(20651060, 10651060, 106510600, 206510600)

    # assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    # assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    # assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    print(d[-2])

