import asyncio
from random import randint
from time import sleep, time

fake_users = [
    {'id': 1, 'name': 'April Murphy', 'company': 'Bailey Inc', 'email': 'shawnlittle@example.org'},
    {'id': 2, 'name': 'Emily Alexander', 'company': 'Martinez-Smith', 'email': 'turnerandrew@example.org'},
    {'id': 3, 'name': 'Patrick Jones', 'company': 'Young, Pruitt and Miller', 'email': 'alancoleman@example.net'}
]


def get_user_sync(uid: int) -> dict:
    sleep(randint(0, 3))  # 0.5
    user, = list(filter(lambda user: user["id"] == uid, fake_users))
    return user


if __name__ == '__main__':
    start = time()
    for i in range(1, 4):
        print(get_user_sync(i))
    print(time() - start)

"""
Тут ми імітуємо запити до бази даних за допомогою
функції get_user_sync і в циклі запитуємо фейкових
користувачів з id від 1 до 3.
"""

async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(randint(0, 3))  # 0.5
    user, = list(filter(lambda user: user["id"] == uid, fake_users))
    return user


async def main():  # coroutine
    r = []  # list for coroutines
    for i in range(1, 4):
        r.append(get_user_async(i))
        # print(r)
    return await asyncio.gather(*r)  # покласти в чергу,


if __name__ == '__main__':
    start = time()
    result = asyncio.run(main())  # main() = coroutine object
    for r in result:
        print(r)
    print(time() - start)

"""
Допоміжна функція asyncio.gather потрібна,
щоб покласти в чергу кілька співпрограм та
дозволити Event loop виконувати їх у будь-якому
порядку. Крім того, asyncio.gather повертає
результат виконання coroutine у тому порядку,
в якому вони були викликані.
"""
