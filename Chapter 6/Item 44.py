#Item 44 - Plain attributes vs Setter or Getter methods
#Setter and Getter examples
class OldResistor:
    def __init__(self, ohms):
        self._ohms = ohms
    
    def get_ohms(self):
        return self._ohms
    
    def set_ohms(self, ohms):
        self._ohms = ohms

r0 = OldResistor(50e3)
print('Before:', r0.get_ohms())
r0.set_ohms(10e3)
print('After', r0.get_ohms())

r0.set_ohms(r0.get_ohms() - 4e3)
assert r0.get_ohms() == 6e3

#simple public attributes with the same result
class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0
    
    def print_(self):
        return self.ohms
    
r1 = Resistor(50e3) #set operation
r1.print_()
r1.ohms = 10e3 #set operation
r1.print_()

r1.ohms += 5e3 #increment operation
r1.print_()

#using @property to have special behavior when an attribute is set
class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0
    
    @property
    def voltage(self):        #it is important for the function names to match
        return self._voltage  #getter
    
    @voltage.setter
    def voltage(self, voltage):       #again, they must match
        self._voltage = voltage       #setter
        self.current =self._voltage / self.ohms

r2 = VoltageResistance(1e3)
print(f'Before: {r2.current:.2f} amps')
r2.voltage = 10
print(f'After:  {r2.current:.2f} amps')

#specify a setter helps to check the values passed to the class
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
    
    @property
    def ohms(self):
        return self._ohms
    
    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'ohms must be > 0; got {ohms}')
        self._ohms = ohms

r3 = BoundedResistance(1e3)
r3.ohms = 0 #error, as expected

BoundedResistance(-5) #error, as expected

#@property to make parent attributes immutable
class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
    
    @property
    def ohms(self):
        return self._ohms
    
    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("ohms is immutable")
        self._ohms = ohms

r4 = FixedResistance(3e3)
r4.ohms = 2e3
r4.ohms

#Mistakes when using @property for getter and setter
#don't set other attributes in getter property method
class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms
    
    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms

r5 = MysteriousResistor(10)
r5.current = 0.01
print(f'Before: {r5.voltage:.2f}')
r5.ohms
print(f'After: {r5.voltage:.2f}') #weird output