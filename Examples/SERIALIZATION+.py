import csv
import json
import pickle

# _________________________________________________________________________
print("_____text into file_____:")

expenses = {
    "hotel": 150,
    "breakfast": 30,
    "taxi": 15,
    "lunch": 20
}

file_name = "expenses.txt"

with open(file_name, "w") as fh:
    for key, value in expenses.items():
        fh.write(f"{key}|{value}\n")
        
expenses = {}

print(expenses)

with open(file_name, "r") as fh:
    raw_expenses = fh.readlines()
    for line in raw_expenses:
        key, value = line.split("|")
        expenses[key] = int(value)
        
print(expenses)

# _________________________________________________________________________
print("___________pickle___(dict)________:")

some_data = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}
# import pickle     # help(ickle.dump)
byte_string = pickle.dumps(some_data, protocol=5)
unpacked1 = pickle.loads(byte_string)

print(unpacked1 == some_data)    # True
print(unpacked1 is some_data)    # False
print(some_data)
print(byte_string)
print(unpacked1)

file_name = 'data.bin'

with open(file_name, "wb") as fh:
    pickle.dump(some_data, fh)
    pickle.dump(file_name, fh)
    
with open(file_name, "rb") as fh:
    unpacked2 = pickle.load(fh)
    unpacked22 = pickle.load(fh)
    
print(unpacked2)
print(unpacked22)

# _________________________________________________________________________
print("___________pickle___(class)________:")


class Human:
    def __init__(self, name):
        self.name = name


bob = Human("Bob")
encoded_bob = pickle.dumps(bob)

decoded_bob = pickle.loads(encoded_bob)

print(bob.name == decoded_bob.name)    # True
print(Human)
print(bob)
print(encoded_bob)
print(decoded_bob)

# _________________________________________________________________________
print("______json___(dict!)________:")


some_data = {'key': 'value', 2: [1, 2, 3],
             'tuple': (5, 6), 'a': {'key': 'value'}}

byte_string = json.dumps(some_data)
unpacked = json.loads(byte_string)

unpacked is some_data    # False
unpacked == some_data    # False

unpacked['key'] == some_data['key']     # True
unpacked['a'] == some_data['a']         # True
unpacked['2'] == some_data[2]           # True
unpacked['tuple'] == [5, 6]             # True


file_name = 'data.json'

with open(file_name, "w") as fh:
    json.dump(some_data, fh)


with open(file_name, "r") as fh:
    unpacked = json.load(fh)


unpacked is some_data    # False
unpacked == some_data    # False

unpacked['key'] == some_data['key']     # True
unpacked['a'] == some_data['a']         # True
unpacked['2'] == some_data[2]           # True
unpacked['tuple'] == [5, 6]             # True

# _________________________________________________________________________
print("_______csv-file_______________:")


with open('eggs.csv', 'w', newline='') as fh:
    spam_writer = csv.writer(fh)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


with open('eggs.csv', newline='') as fh:
    spam_reader = csv.reader(fh)
    for row in spam_reader:
        print(', '.join(row))


with open('names.csv', 'w', newline='') as fh:
    field_names = ['first_name', 'last_name']
    writer = csv.DictWriter(fh, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


with open('names.csv', newline='') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        print(row['first_name'], row['last_name'])
        
# _________________________________________________________________________
print("___________pickle___(hard-class)________:")

class A:

    def __init__(self):
        self.file = open('file.txt', 'r')

    def __getstate__(self):
        self.__dict__['file'] = None

    def __setstate__(self):
        self.__dict__['file'] = open('file.txt', 'r')

    def method(self):
        pass

a = A()

with open('file.txt', 'wb') as file:
    pickle.dump(a, file)




