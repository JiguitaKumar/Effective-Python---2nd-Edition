#Item 23 - Optional behavior with Keyword arguments 
#pass arguments by position
def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6

#pass arguments by keyword
remainder(20, 7)
remainder(20, divisor = 7)
remainder(number = 20, divisor = 7)
remainder(divisor = 7, number = 20)
remainder(number = 20, 7)
remainder(20, number = 7)

#when you already have a dictionary (using **)
my_kwargs = {
    'number': 20,
    'divisor': 7,
}

assert remainder(**my_kwargs) == 6
remainder(**my_kwargs)

my_kwargs2 = {
    'divisor': 7,
}

remainder(20, **my_kwargs2)

my_kwargs3 = {
    'number': 20,
}

remainder(**my_kwargs3, **my_kwargs2)

#function receives any named keyword arguments
def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

print_parameters(alpha = 1.5, beta = 9, gamma = 4)

#examples of benefits of using keyword arguments
def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = 0.5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print(f'{flow:.3} kg per second')

def flow_rate2(weight_diff, time_diff, period):
    return (weight_diff / time_diff) * period
flow_per_second = flow_rate2(weight_diff, time_diff, period=1)

def flow_rate3(weight_diff, time_diff, period=1):
    return (weight_diff / time_diff) * period

flow_per_second = flow_rate3(weight_diff, time_diff)
flow_per_hour = flow_rate3(weight_diff, time_diff, period = 3600)

def flow_rate4(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff * units_per_kg) / time_diff) * period

pounds_per_hour = flow_rate4(weight_diff, time_diff, 3600, 2.2)
pounds_per_hour
