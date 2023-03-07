import asyncio
from time import sleep


async def baz() -> str:
    print('Before Sleep')
    await asyncio.sleep(7)
    print('After Sleep(3)')
    return 'Hello world'


async def main():
    r = baz()  # r = об'єкт coroutine
    sleep(2)
    print(r)  # r = об'єкт coroutine
    result = await r  # run buz
    print('Buz is RUN!')  # print after buz-return
    print(result)


if __name__ == '__main__':
    asyncio.run(main())

"""
Це найпростіший приклад на async/await.
Виклик print(r) нам повертає об'єкт coroutine.
Щоб отримати результат від асинхронної функції
baz, нам потрібен await. І тільки виконавши
result = await r ми отримаємо у
змінній result значення Hello world.
"""
