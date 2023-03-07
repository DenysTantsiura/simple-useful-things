import multiprocessing
from multiprocessing import JoinableQueue, Process, current_process, cpu_count, Manager
import logging
import requests
from timeit import default_timer
from concurrent.futures import ThreadPoolExecutor

max_relevant_threads = cpu_count()
url = 'https://picsum.photos/200/300'
path = 'images/image_{n}.jpg'

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')


def execute_time(fun):
    def inner(*args, **kwargs):
        start = default_timer()
        fun(*args, **kwargs)
        logging.info(f'{default_timer()-start=} sec')
        return args

    return inner


def download(n: int):

    file_path = path.format(n=n)
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

    # print(f"{max_relevant_threads=}")

    return url


@execute_time
def download_pack(count: int):
    with ThreadPoolExecutor(max_workers=max_relevant_threads) as executor:
        executor.map(download, range(count))


if __name__ == "__main__":

    # print(f"{max_relevant_threads=}")
    multiprocessing.set_start_method('fork')  # spawn  fork ...

    download_pack(15)
    # for n in range(10):
    #     print(f'{download(n)=}')

    # t1 = Process(target=download, args=(200,))
    # t2 = Process(target=download, args=(300,))
    #
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()
