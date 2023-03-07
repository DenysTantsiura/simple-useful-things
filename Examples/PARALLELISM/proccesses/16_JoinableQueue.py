from multiprocessing import JoinableQueue, Process, current_process
from time import sleep
import sys
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

jq = JoinableQueue()


def worker(jqueue: JoinableQueue):
    name = current_process().name
    logger.debug(f'{name} started...')
    val = jqueue.get()
    logger.debug(f'{name} {val**2}')
    sleep(1)
    jqueue.task_done()
    sys.exit(0)


if __name__ == '__main__':
    w1 = Process(target=worker, args=(jq, ))
    w2 = Process(target=worker, args=(jq, ))

    w1.start()
    w2.start()

    jq.put(8)
    sleep(1)
    jq.put(16)
    jq.join()
    print('Finished')

"""
У цьому прикладі master-процес (основний процес) очікує
виконання завдань від робочих процесів за допомогою виклику
методу jq.join() у екземпляра черги JoinableQueue. Самі
worker-процеси повідомляють master про успішне виконання
завдання через виклик методу черги jqueue.task_done().
Це дозволяє тримати в курсі master-процес про стан завершення
робочого процесу та рядок коду print('Finished') виконається
тільки, коли всі робочі процеси будуть завершені.
"""
