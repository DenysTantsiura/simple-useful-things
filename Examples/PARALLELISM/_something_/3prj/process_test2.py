from multiprocessing import JoinableQueue, Process, current_process, Manager
from time import sleep
import sys
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

jq = JoinableQueue()


def worker(jqueue: JoinableQueue, return_dict):
    name = current_process().name
    logger.debug(f'{name} started...')
    val = jqueue.get()
    logger.debug(f'{name} {val**2}')
    return_dict[val] = val**2
    sleep(1)
    jqueue.task_done()
    sys.exit(0)



if __name__ == '__main__':
    #w = {}
    manager = Manager()
    return_dict = manager.dict()
    for i in range(10):
        Process(target=worker, args=(jq, return_dict)).start()
        # p.start()
    result = []
    for i in range(10):
        jq.put(i)
        # result.append(jq.get_nowait())

    jq.join()
    # for i in w:
    #     print(f'Finished: {return_dict.values()}')
    print(f'Finished: {return_dict.values()}')
