#!/usr/bin/env python


def foo(a, b):
    """function docstring"""
    return a + b


# test comments
class Point(object):
    """class docstring"""
    x = 100
    y = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def export(self):
        return self.x, self.y


c = 1
d = 3

for n in range(10):
    if n > 5:
        print(n)


print("123")

print(Point(5,5).export())
print(foo(c, d))

print(c > d)
