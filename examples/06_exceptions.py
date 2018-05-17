import math


class NotANumberError(Exception):
    pass


class NonPositiveNumberError(Exception):
    pass


def get_integer(prompt='Enter a number: '):
    s = input(prompt)
    try:
        return int(s)
    except ValueError:
        raise NotANumberError(s)


def get_positive_integer():
    n = get_integer('Enter a positive number: ')
    if n > 0:
        return n
    else:
        raise NonPositiveNumberError(n)


try:
    x = get_positive_integer()
except NotANumberError as e:
    print(e.args[0], 'is not a number.')
except NonPositiveNumberError as e:
    print(e.args[0], 'is not a positive number.')
else:
    print('Square root of', x, 'is', math.sqrt(x))
print('Thank you for using this program!')
