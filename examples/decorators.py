import math
from contextlib import contextmanager


class Square:
    def __init__(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.width

    def set_area(self, a):
        self.width = math.sqrt(a)

    area = property(get_area, set_area)

    @staticmethod
    def print_name():
        print('Square')

    @classmethod
    def print_class(cls):
        print(cls.__name__)



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

print('sq({}) = {}'.format(5, sq(5)))



@contextmanager
def open_for_write(filename):
    f = open('ddd.txt', 'w+')
    print('open')
    yield f
    f.close()
    print('closed')

##with open_for_write('ddd.txt') as f:
##    f.write('Hello!')
##    print('written')
##print('done')
