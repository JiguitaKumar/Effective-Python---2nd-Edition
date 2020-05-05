#Item 25 - Keyword-only and Positional-only argument
#simple function
def safe_division(number, divisor,
                  ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division(1.0, 10**500, True, False)
print(result)

result2 = safe_division(1.0, 0, False, True)
print(result2)

#simplifying the logic by only calling arguments when needed
def safe_division2(number, division,
                   ignore_overflow = False,
                   ignore_zero_division = False):
    try:
        return number / division
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result3 = safe_division2(1.0, 10**500, ignore_overflow = True)
print(result3)

result4 = safe_division2(1.0, 0, ignore_zero_division = True)
print(result4)

assert safe_division2(1.0, 10*500, True, False) == 0 #didn't work for me

assert safe_division2(1.0, 0, False, True) == float('inf')

#forcing the correct use of the keywords-only (*)
def safe_division3(number, divisor, *,
                   ignore_overflow = False,
                   ignore_zero_division = False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

safe_division3(1.0, 10*500, True, False) #has the expected effect

result5 = safe_division3(1.0, 0, ignore_overflow = False,
                         ignore_zero_division = True)
print(result5)

result6 = safe_division3(1.0, 0, ignore_zero_division = True)
assert result6 == float('inf')

try:
    result = safe_division3(1.0, 0)
except ZeroDivisionError:
    pass

assert safe_division3(number = 2, divisor = 5) == 0.4
assert safe_division3(divisor = 5, number = 2) == 0.4
assert safe_division3(2, divisor = 5) == 0.4

#changing the name of the arguments (might cause problems when called)
def safe_division3(numerator, denominator, *,
                   ignore_overflow,
                   ignore_zero_division):
    try:
        return numerator / denominator
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

safe_division3(number=2, divisor=5) #not gonna work now

#what if i don't want to attribute names to the arguments (position-only)
def safe_division4(number, divisor, /, *, 
                   ignore_overflow = False,
                   ignore_zero_division = False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

assert safe_division4(2, 5) == 0.4

safe_division4(number = 2, divisor = 4) #works great!

def safe_division5(number, divisor, /,
                   ndigits = 10, *,
                   ignore_overflow = False,
                   ignore_zero_division = False):
    try:
        fraction = number / divisor
        return round(fraction, ndigits)
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result7 = safe_division5(22, 7)
print(result7)

result8 = safe_division5(22, 7, 5)
print(result8)

result9 = safe_division5(22, 7, ndigits=3)
print(result9)