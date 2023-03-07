import pathlib
from queue import Queue
from threading import Thread, Event
import logging


class Writer:
    def __init__(self, filename, event: Event):
        self.data_queue = Queue()
        self.event = event
        self.file = open(filename, 'x', encoding='utf-8')

    def __call__(self, *args, **kwargs):
        while True:
            if self.data_queue.empty():
                if self.event.is_set():
                    break
            else:
                r_file, data = self.data_queue.get()
                self.file.write(f"{data}\n")

    def __del__(self):
        self.file.close()


def reader(data_queue: Queue):
    while True:
        if files.empty():
            logging.info('Operation completed!')
            break
        r_file = files.get()
        with open(r_file, 'r', encoding='utf-8') as fd:
            data = []
            for line in fd:
                data.append(line)
            all_data = ''.join(data)
            data_queue.put((r_file, all_data))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    event = Event()
    files = Queue()

    list_files = pathlib.Path('.').joinpath('files').glob('*.js')
    print(list_files)
    [files.put(file) for file in list_files]

    writer = Writer('main.js', event)
    if files.empty():
        logging.info('Nothing!')
    else:
        tw = Thread(target=writer)
        tw.start()

        threads = []
        for folder in range(2):
            th = Thread(target=reader, args=(writer.data_queue, ))
            th.start()
            threads.append(th)

        [th.join() for th in threads]
        event.set()

Цей скрипт є базовим прикладом використання багатопоточності в Python.
Він використовує класи Queue та Thread з модулів queue та threading відповідно.

Ми визначаємо клас Writer, який приймає ім'я файлу, куди ми будемо збирати всі файли js та подію event через яку взнаємо, що файли для обєднання всі прочитані функцієми reader і більше немає файлів для обробки.
Метод __call__, в нескінченому циклі, перевіряє, чи порожня черга даних self.data_queue.empty(), і якщо ні, записує дані у файл конкатенації.

Функція reader, в потоках читає файли з папки files та поміщає дані у чергу даних self.data_queue класу Writer. Якщо файли закінились if files.empty() функція в потоці завершує свою роботу.

У головному потоці ми створюємо подію event = Event() та чергу для файлів files = Queue(), потім використовучи glob отримуємо всі файли .js в папці 'files' та поміщаємо їх у чергу файлів files.

Потім створюємо потік для запису tw = Thread(target=writer) і два потоки для читання файлів th = Thread(target=reader, args=(writer.data_queue, )) та запускаємо їх.

Нам треба дочекатися завершення всіх потоків reader та встановити подію закінчення процесу читання event.set(), що призводить до завершення потоку запису Writer :

if self.data_queue.empty():
                if self.event.is_set():
                    break