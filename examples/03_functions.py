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


def calculate_pi():
    """A function without parameters."""

    return 3.14159265


def get_integer(prompt='Enter a number: '):
    """A function with given default value for its parameter."""

    return int(input(prompt))


def double(x):
    """Return the parameter multiplied by 2.

    This is a "pure function".

    Variables defined within the function exist only while the
    function is running. They "disappear" after the function is done.
    """

    result = 2 * x
    return result


def double2(x):
    """Print the parameter multiplied by 2.

    This is a function with "side effects".
    """

    print(2 * x)

    # if "return" is missing, returns `None`.


double(10)


######################################
#             Advanced               #
######################################

get_integer2 = get_integer  # `get_integer2` becomes an alias to `get_integer`.


def apply(fn, value):
    """A function that accepts other function as a parameter."""

    return fn(value)


def trigonometry_func(kind):
    """A function that returns another function."""

    import math
    if kind == 'sinus':
        return math.sin
    else:
        return math.cos


def create_multiply_function(multiply_by):
    """A function that defines another function and returns it."""

    def multiply(x):
        return multiply_by * x
    return multiply


def print_tuple(*args):
    """A function that accepts any number of parameters and prints them."""

    print(args)


def print_dict(**kwargs):
    """A function that accepts any keyword arguments and prints them."""

    print(kwargs)


def find_longest_word(first, *rest):
    """A function that accepts at least one (or more) parameters."""

    words = (first,) + rest
    return max([len(word) for word in words])


def create_dict(*args, **kwargs):
    """A function that passes all its received parameters to another function."""

    return dict(*args, **kwargs)
