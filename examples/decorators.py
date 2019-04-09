import math
from contextlib import contextmanager


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_area(self, a):
        self.width = self.height = math.sqrt(a)

    area = property(get_area, set_area)

    def calc_area(self):
        return self.width * self.height

    @staticmethod
    def print_name():
        print('Rectangle')

    @classmethod
    def print_class(cls):
        print(cls.__name__)


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)


def print_debug_message_decorator(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print('{} was executed.'.format(f.__name__))
        return result
    return wrapper


@print_debug_message_decorator
def sq(x):
    return x * x


# # This is equivalent to the previous
# def sq(x):
#     return x * x
# sq = print_debug_message_decorator(sq)


@contextmanager
def open_for_write(filename):
    f = open('ddd.txt', 'w+')
    print('open')
    yield f
    f.close()
    print('closed')


print('sq({}) = {}'.format(5, sq(5)))
with open_for_write('ddd.txt') as f:
    f.write('Hello!')
    print('written')
print('done')
