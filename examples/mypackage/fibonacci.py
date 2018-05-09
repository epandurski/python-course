def fib1(n):
    """Return Fibonacci series up to `n` as a list.

    This is a "pure function".
    """

    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


def fib2(n):
    """Print a Fibonacci series up to `n`.

    This is a function with "side effects".
    """

    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b
    return 'successfully done'
