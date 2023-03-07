from multiprocessing import Pool, current_process
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def worker(x):
    logger.debug(f"pid={current_process().pid}, x={x}")
    return x*x


if __name__ == '__main__':
    with Pool(processes=2) as pool:
        logger.debug(pool.map(worker, range(10)))
        
"""
Пул процесів з multiprocessing дає більше контролю,
ніж пул з concurrent.futures. Основні можливості:

розбиває вхідну послідовність на блоки та виконує
паралельну обробку поблочно, так можна зменшити
обсяг використовуваної пам'яті;
асинхронне виконання трохи прискорює отримання
результатів, якщо порядок не важливий;
передача кортежу аргументів у target-функцію;
"""
