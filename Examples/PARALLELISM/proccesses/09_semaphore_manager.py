from multiprocessing import Process, Semaphore, current_process, Manager
from random import randint
from time import sleep


def worker(semaphore: Semaphore, r: dict):  # or : Manager ?
    print('Wait')
    with semaphore:
        name = current_process().name
        print(f'Work {name}')
        delay = randint(1, 2)
        r[name] = delay  # = current_process().pid
        sleep(0.2)  # work imitation


if __name__ == '__main__':
    semaphore = Semaphore(3)
    with Manager() as m:
        result = m.dict()  # Plain
        prs = []
        for num in range(10):
            pr = Process(name=f'Process-{num}', target=worker, args=(semaphore, result))
            pr.start()
            prs.append(pr)

        for pr in prs:  # [pr.join() for pr in prs]
            pr.join()

        print(result)

    print('End program')

"""
Але є важливе зауваження. Проксі-об'єкти Manager
не можуть поширювати зміни, внесені до об'єктів,
що змінюються всередині контейнера. Іншими словами,
якщо у вас є об'єкт manager.list(), будь-які зміни
в самому керованому списку розповсюджуються на всі
інші процеси. Але якщо у вас є звичайний список Python
всередині цього списку, будь-які зміни у внутрішньому
списку не поширюються, тому що менеджер не має
можливості виявити зміни.

Щоб розповсюдити зміни, ви також повинні використовувати
об'єкти manager.list() для вкладених списків.
(необхідний Python 3.6 або вище) або вам потрібно
безпосередньо змінити об'єкт manager.list()
"""
