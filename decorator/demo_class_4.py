def add_str(cls):
    def __str__(self):
        return str(self.__dict__)
    cls.__str__ = __str__
    return cls


@add_str
class MyObject:
    def __init__(self, a, b):
        self.a = a
        self.b = b


o = MyObject(1, 2)
print(o)
