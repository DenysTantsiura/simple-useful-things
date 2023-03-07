import concurrent.futures
import math


PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor(4) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

"""
Створення процесів за допомогою пакета concurrent
Пакет concurrent.futures також реалізує API Executor
для пулу процесів у класі ProcessPoolExecutor.

Основні можливості обмежені API Executor. Зручно
використовувати ProcessPoolExecutor там, де потрібно
виконати CPU-bound завдання в async коді та реалізовано
саме для підтримки виконання блокуючих CPU-bound задач
в async додатках (з async ми познайомимося в
"Модуль 5: Асинхронне програмування в Python").

Зараз приклад на виконання
CPU-bound завдання
"""
