from threading import Condition, Thread
from time import sleep
import logging


def master(con: Condition):
    logging.debug('Master work hard')
    sleep(1)
    with con:
        logging.debug('Работайте сонце ще високо!')
        con.notify_all()
        # con.notify(1)


def worker(con: Condition):
    logging.debug(f'waiting...')
    with con:
        con.wait()
        # some work
        logging.debug(f'finished')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    con = Condition()

    master = Thread(name='master', target=master, args=(con, ))

    w1 = Thread(name='worker_one', target=worker, args=(con, ))
    w2 = Thread(name='worker_two', target=worker, args=(con, ))

    w1.start()
    w2.start()
    master.start()
