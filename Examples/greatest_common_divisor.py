# Найбільший спільний дільник:

first = int(input("Enter ineger 1: ")) # int
second = int(input("Enter ineger 2: ")) # int

while second > 0:
    gcd = first % second
    first = second
    second = gcd

print(first)


while second > 0:
    first, second = second, first % second

print(first)
