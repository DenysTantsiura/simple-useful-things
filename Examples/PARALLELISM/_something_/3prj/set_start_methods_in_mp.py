import multiprocessing
from multiprocessing import JoinableQueue, Process, current_process, cpu_count, Manager


max_relevant_threads = cpu_count()


def fun1(inval):
    print(f"{max_relevant_threads=}")
    return inval


if __name__ == "__main__":

    # print(f"{max_relevant_threads=}")
    multiprocessing.set_start_method('fork')  # spawn  fork ...

    t1 = Process(target=fun1, args=(None,))
    t2 = Process(target=fun1, args=(None,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
