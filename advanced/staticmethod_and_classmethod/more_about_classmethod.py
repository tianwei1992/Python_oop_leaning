# coding:utf-8

"""类方法用在模拟java定义多个构造函数的情况。
由于python类中只能有一个初始化方法，不能按照不同的情况初始化类。"""
class Book(object):

    def __init__(self, title):
        self.title = title

    @classmethod
    def create1(cls, title):
        book = cls(title=title)
        return book

    @classmethod
    def create2(cls, title):
        book = cls(title=title)
        return book

book1 = Book("python")
book2 = Book.create1("python and django")
book3 = Book.create1("python and flask")
print(book1.title)
print(book2.title)
print(book3.title)
"""静态方法调用另一个静态方法，如果改用类方法调用静态方法，可以让cls代替类，
让代码看起来精简一些。也防止类名修改了，不用在类定义中修改原来的类名。"""


class Foo(object):
    X = 1
    Y = 2

    @staticmethod
    def averag(*mixes):
        return sum(mixes) / len(mixes)

    @staticmethod
    def static_method():
        return Foo.averag(Foo.X, Foo.Y)

    @classmethod
    def class_method(cls):
        return cls.averag(cls.X, cls.Y)

foo = Foo()
print(foo.static_method())
print(foo.class_method())