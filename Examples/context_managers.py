class FileWriter:
    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "w")
        self.opened = True
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
        self.opened = False

if __name__ == "__main__":

    with FileWriter("new_file.txt") as f:
        
        f.write("Hello world\n")
        f.write("The end\n")

# __________________________________________________


from datetime import datetime
from time import sleep


class FileReader:
    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename
        self.log = ""
        self.timestamp = None

    def __enter__(self):
        self.file = open(self.filename, "r")
        self.opened = True
        self.timestamp = datetime.now().timestamp()
        msg = "{:<20}|{:^15}| open \n".format(self.timestamp, self.filename)
        self.log += msg
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
            timestamp = datetime.now().timestamp()
            diff = timestamp - self.timestamp
            msg = "{:<20}|{:^15}| closed: {:>15} \n".format(timestamp, self.filename, round(diff, 6))
            self.log += msg
        self.opened = False

reader = FileReader("new_file.txt")

with reader as f:
    sleep(2)
    print(f.read())

with reader as f:
    sleep(1)
    print(f.read())

print(reader.log)

# _____________________________________________________________

from contextlib import contextmanager

@contextmanager
def managed_resource(*args, **kwargs):
    file_handler = open(*args, **kwargs)
    try:
        yield file_handler
    finally:
        file_handler.close()


with managed_resource("new_file.txt", "r") as f:
    print(f.read())
    
