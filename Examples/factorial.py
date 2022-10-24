def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


def factorial2(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

print(factorial2(5))

def factorial3(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial3(5))