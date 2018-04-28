def fib1(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
