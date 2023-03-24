#!/usr/bin/python3
class P:
    def __init__(self, x):
        self.x = x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        if x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    def __repr__(self):
        return self.x
c = P(1001)

print(c)
