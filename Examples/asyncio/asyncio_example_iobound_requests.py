import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor
from time import time

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com']


def preview_fetch_sync(url):
    r = requests.get(url)
    return url, r.text[:150]


if __name__ == '__main__':
    start = time()
    for url in urls:
        r = preview_fetch_sync(url)
        print(r)
    print(time() - start)
    
# -------async:-------------------------
def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[:150]


async def preview_fetch_async():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(3) as pool:
        futures = [loop.run_in_executor(pool, preview_fetch, url) for url in urls]
        result = await asyncio.gather(*futures, return_exceptions=True)
        return result


if __name__ == '__main__':
    start = time()
    r = asyncio.run(preview_fetch_async())
    print(r)
    print(time() - start)

"""
Ми робимо функцію обгортку preview_fetch_async
над функцією preview_fetch. Всередині беремо
поточний виконуваний
Event loop loop = asyncio.get_running_loop()
та за допомогою ThreadPoolExecutor поміщаємо
функцію preview_fetch у Executor -
[loop.run_in_executor(pool, preview_fetch, url) for url in urls].
Отриманий список об'єктів Futures передаємо
в asyncio.gather(*futures) для отримання
остаточного результату.

Параметр 'return_exceptions' відповідає за обробку помилок,
за замовчуванням встановлено значення False.
Перший згенерований виняток негайно поширюється
на завдання, що очікує в gather. Якщо
return_exceptions має значення True, винятки
обробляються так само, як і успішні результати,
та об'єднуються у списку результатів.
"""
