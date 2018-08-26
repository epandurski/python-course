from contextlib import contextmanager


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def calc_area(self):
        return self.width * self.height

    @staticmethod
    def get_name():
        return 'Rectangle'

    @classmethod
    def get_class(cls):
        print(cls)


class Square(Rectangle):
    pass


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
