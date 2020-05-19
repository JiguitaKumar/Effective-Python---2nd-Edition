#Item 40 - Using super() in classes
#the old simple way (__init__)
class MyBaseClass:
    def __init__(self, value):
        self.value = value

class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)

#Limitations
## 1. multiple inheritance
class TimesTwo:
    def __init__(self):
        self.value *= 2

class PlusFive:
    def __init__(self):
        self.value += 5

class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo = OneWay(5)
print('First ordering value is (5 * 2) + 5 =', foo.value)

mychild = MyChildClass()
mychild.value

mybase = MyBaseClass(3)
mybase.value

class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self) #the order wasn't changes on purpose

bar = AnotherWay(5)
print('Second ordering value is', bar.value) #outputs 15 - problem!

"""the order of the parents classes must be changed in order to reflect \
    the new calculation process. The order followed for the calculations \
    is the order by which the Class.__init__ are organized and not by \
    the reverse order presented in the beginning (AnotherWay \
    (MyBaseClass, PlusFive, TimesTwo))
"""

## 2. Diamond inheritance
class TimesSeven(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 7

class PlusNine(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 9

class ThisWay(TimesSeven, PlusNine):
    def __init__(self, value):
        TimesSeven.__init__(self, value)
        PlusNine.__init__(self, value)

foo = ThisWay(5)
print('Should be (5 * 7) + 9 = 44 but is', foo.value) #outputs 14 - problem!

"""As the subclasses TimesSeven and PlusNine have the same parent class \
    calling PlusNine causes the self.value to reset to 5 instead of \
    building upon 35
"""

#Solution - the super built-in function
class PlusNineCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value += 9

class TimesSevenCorrect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value *= 7

class GoodWay(TimesSevenCorrect, PlusNineCorrect):
    def __init__(self, value):
        super().__init__(value)

foo = GoodWay(5)
print('Should be 7 * (5 + 9) = 98 and is', foo.value)

"""The result is 98 instead of 44 because the order of the operations \ 
   is not defined by the order by which we provide the classes but \
   instead by what MRO (method resolution order) defines for the class
"""

mro_str = '\n'.join(repr(cls) for cls in GoodWay.mro())
print(mro_str)

"""according to the output, TimesSeven calls PlusNine, which in turn \
   class MyBaseClass. Once reached the top of the diamond, the operations \
   are performed backwards (MyBaseClass + 9) * 7
   So the calculations are always performed backwards from the order \
   from which they were called. If we've written GoodWay(PlusNine, \
   TimesSeven) we would get 44
"""

#The super function can also be called with 2 parameters
##however these 3 classes are equivalent
class ExplicitTrisect(MyBaseClass):
    def __init__(self, value):
        super(ExplicitTrisect, self).__init__(value)
        self.value /= 3

class AutomaticTrisect(MyBaseClass):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        self.value /= 3

class ImplicitTrisect(MyBaseClass):
    def __init__(self, value):
        super().__init__(value)
        self.value /= 3

assert ExplicitTrisect(9).value == 3
assert AutomaticTrisect(9).value == 3
assert ImplicitTrisect(9).value == 3