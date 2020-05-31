#Item 42 - Public Attributes vs Private Attributes
#Example
class MyObject:
    def __init__(self):
        self.public_field = 5 #Public
        self.__private_field = 10 #Private (because of the double underscore)
    
    def get_private_field(self):
        return self.__private_field

foo = MyObject()
assert foo.public_field == 5

assert foo.get_private_field() == 10 #can only be called through methods

foo.__private_field #doesn't work when called directly

#private attributes of class methods
class MyOtherObject:
    def __init__(self):
        self.__private_field = 71
    
    @classmethod
    def  get_private_field_of_instance(cls, instance):
        return instance.__private_field

bar = MyOtherObject()
assert MyOtherObject.get_private_field_of_instance(bar) == 71

#a subclass can't access its parent class's private fields
class MyParentObject:
    def __init__(self):
        self.__private_field = 71
    
class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field

baz = MyChildObject()
baz.get_private_field() #does not work, as expected

#to call the attribute we should rather do the following
assert baz._MyParentObject__private_field == 71

print(baz.__dict__) #here we can see how the attribute is stored

#do not use private attr to prevent access by subclasses
class MyStringClass:
    def __init__(self, value):
        self.__value = value
    
    def get_value(self):
        return str(self.__value)

foo = MyStringClass(5)
assert foo.get_value() == '5'

"""you may want to change the behavior of your attribute eventually \
    through your subclasses
"""

class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value)

foo = MyIntegerSubclass('5')
assert foo.get_value() == 5 

"""if the hierarchy changes beneath, the classes will break be the \
    private attr reference is no longer valid
"""

class MyBaseClass:
    def __init__(self, value):
        self.__value = value
    
    def get_value(self):
        return self.__value
    
class MyStringClass(MyBaseClass):
    def get_value(self):
        return str(super().get_value()) #changed

class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return int(self._MyStringClass__value) #not changed (Error)

foo = MyIntegerSubclass(5)
foo.get_value() #AttributeError

#Always document which attributes are private and why
class MyStringClass:
    def __init__(self, value):
        #This stores the user-supplied value for the object.
        #It should be coercible to a string. Once assigned in the object
        #it should be treated as immutable.
        self._value = value
    
    def get_value(self):
        return str(self._value)


class MyIntegerSubclass(MyStringClass):
    def get_value(self):
        return self._value

foo = MyIntegerSubclass(5)
assert foo.get_value() == 5

#only use private attr when worried about naming conflicts with subclasses
class ApiClass:
    def __init__(self):
        self._value = 5
    
    def get(self):
        return self._value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello' #conflict
        
a = Child()
print(f'{a.get()} and {a._value} should be different') #both print 'hello'

#solving the issue with private attribute (double underscore)
class ApiClass:
    def __init__(self):
        self.__value = 5
    
    def get(self):
        return self.__value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'

a = Child()
print(f'{a.get()} and {a._value} are different') #works! 