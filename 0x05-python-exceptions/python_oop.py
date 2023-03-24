#!/usr/bin/python3
class Robots:
    def __init__(self, name, build = ''):
        self.__name = name
        self.__build = ''
        self.__flip = 'mute'
        self.other = 5
    def say_hi(self):
        if self.__name:
            print('Hi i am', self.__name)
        else:
            print('I am a robot without a name')
    def set_n(self, name, build_year):
        self.__name = name
        self.__build = build_year
    def get_n(self):
        return (self.__name, self.__build)

a = Robots('G2_50')
##a.set_n('G2_50', 2016)
#a.say_hi()
#b = Robots('G3_50')
##b.set_n('G3-50', 2017)
#c = Robots('G4_50')
#a.get_n()
#b.get_n()
#c.get_n()
#print(a.get_n(), '\n', b.get_n(), '\n', c.get_n())
#print(OB
#print(a.Robots__name)
print(a.other)
print(a.__flip)
