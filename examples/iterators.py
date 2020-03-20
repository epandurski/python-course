class RevListIterator:
    def __init__(self, l):
        self.list = l
        self.index = len(l) - 1
        
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.list[self.index]
        self.index -= 1
        return value

        
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def __iter__(self):
        return RevListIterator(self.tricks)  # or `self.tricks`


def rev(data):
    print('stated')
    index = len(data)
    while index > 0:
        index -= 1
        print('before yielding')
        yield data[index]
        print('after yielding')
    print('finished')


class Dog2:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def __iter__(self):
        for trick in self.tricks:
            yield trick
