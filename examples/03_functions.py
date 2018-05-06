# Wikipedia: In mathematics, a function is originally the idealization
#            of how a varying quantity depends on another
#            quantity. For example, the position of a planet is a
#            function of the time.
#
# >>> from math import cos


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


def get_integer(prompt='Enter a number: '):
    return int(input(prompt))