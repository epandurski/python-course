def get_year_of_birth(person):
    """Return the year of birth of some famous persons."""

    if person == 'Isaac Newton':
        return 1642
    elif person == 'Marie Curie':
        return 1867
    elif person == 'Albert Einstein':
        return 1879
    elif person == 'Guido van Rossum':
        return 1956
    else:
        return None


def fib1(n):
    """Print a Fibonacci series up to n."""

    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a + b
    return 'successfully done'


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
