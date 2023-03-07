import asyncio
import random
from time import sleep


async def random_value():
    print("start task")
    await asyncio.sleep(3)
    print("task finished")
    return random.random()


async def main():
    task = asyncio.create_task(random_value())
    print("task scheduled")
    sleep(5)
    await task
    print(f"result: {task.result()}")


if __name__ == '__main__':
    asyncio.run(main())

"""
доки не було викликано await task, завдання не виконувалося
"""
