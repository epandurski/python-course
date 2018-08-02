class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


def rev(data):
    print('stated')
    index = len(data)
    while index > 0:
        index -= 1
        print('before yielding')
        yield data[index]
        print('after yielding')
    print('finished')


class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def __iter__(self):
        for trick in self.tricks:
            yield trick
