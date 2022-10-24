import contextlib


@contextlib.contextmanager
def connect(connection_string):
    print("Connecting on")
    connection = 'connection...'

    yield connection

    print("Closing connection")


with connect("mysql://qwerty") as conn:
    print(conn)

print("Final")

# ------------------OR:

class Connection:

    def __init__(self, connection_string):
        self.connection_string = connection_string

    def __enter__(self):

        print(f"Connecting to {self.connection_string}")
        self.connection = f'connection with {self.connection_string}'

        return self.connection

    def __exit__(self, exception_type, exception_value, traceback):

        self.connection = f'connection is closed'
        print(self.connection)

with Connection("mysql://qwerty") as conn:
    print(conn)


print("Final")
