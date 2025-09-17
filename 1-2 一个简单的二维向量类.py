# -*- coding: utf-8 -*-
# @Time : 2024/10/6 18:31
# @Author : CSR
# @File : 1-2 一个简单的二维向量类.py

from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
    print(v1 * 3)
    print(v1)