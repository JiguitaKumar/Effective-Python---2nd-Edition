#Item 39 - Using @classmethod polymorphism
#to read the input
class InputData:
    def read(self):
        raise NotImplementedError

class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def read(self):
        with open(self.path) as f:
            return f.read()

#to consume the input
class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    
    def map(self):
        raise NotImplementedError
    
    def reduce(self, other):
        raise NotImplementedError #allows the function to be override by subclasses
        
"""example of how map() function works:
def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

>>> [2, 4, 6, 8]    
"""

class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n') #counts the number of lines in data
    
    def reduce(self, other):
        other.result += self.result #other.result? New variable?

"""Worker is the parent class and LineCountWorker is the child class
    so the child class can call any function created in the parent class
"""

#building objects and orchestrating the MapReduce
import os

def generate_inputs(data_dir):
    for name in os.listdir(data_dir): #returns files and directories in the path
        yield PathInputData(os.path.join(data_dir, name)) #join paths

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

#execute Worker
from threading import Thread

def execute(workers):
    threads = [Thread(target = w.map) for w in workers] #w.map is the function
    for thread in threads: 
        thread.start()
    for thread in threads:
        thread.join()
        
    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result

#connecting all the pieces
def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)

#Running the function
import os
import random

def write_test_files(tmpdir):
    os.makedirs(tmpdir)
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), 'w') as f:
                  f.write('\n' * random.randint(0, 100))

tmpdir = 'test_inputs'
write_test_files(tmpdir)

result = mapreduce(tmpdir)
print(f'There are {result} lines')

"""the problem with this code is that it requires to rewrite the \
    the InputData and the Worker subclass whenever we want to use \
    something different.
"""

#solution - the class method
# Abstract class - for the input data
class GenericInputData:
    def read(self):
        raise NotImplementedError
    
    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

#concrete class - for the input data
class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path
    
    def read(self):
        with open(self.path) as f:
            return f.read()
    
    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))
    
#Abstract class & concrete subclass - for Worker
class GenericWorker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None
    
    def map(self):
        raise NotImplementedError
    
    def reduce(self, other):
        raise NotImplementedError
    
    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config): #creates a subclass from generate_inputs
            workers.append(cls(input_data))
        return workers

"""the input_class.generate_inputs is the class polyphormism.
    calling cls() provides an alternative way to construct objects \
    besides using __init__
"""

class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')
    
    def reduce(self, other):
        self.result += other.result

#now rewrite the mapreduce function
def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

config = {'data_dir': tmpdir}
result = mapreduce(LineCountWorker, PathInputData, config)
print(f'There are {result} lines')