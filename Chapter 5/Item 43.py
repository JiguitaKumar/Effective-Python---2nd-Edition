#Item 43 - Custom container types (collections.abc)
#built-in list type
class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)
    
    def frequency(self):
        counts = {}
        for item in self:
            counts[item] = counts.get(item, 0) + 1
        return counts
    
foo = FrequencyList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
print('Length is', len(foo))
foo.frequency()

foo.pop()
print('After pop:', repr(foo))
print('Frequency:', foo.frequency())

#what if i want an object that feels like a list and allows indexing but
#is not a list subclass
class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#Python automatically indexes the sequences
bar = [1, 2, 3]
bar[0]

#how to make BinaryNode to act like a sequence
class IndexableNode(BinaryNode):
    def _traverse(self):
        if self.left is not None:
            yield from self.left._traverse()
        yield self
        if self.right is not None:
            yield from self.right._traverse()
    
    def __getitem__(self, index):
        for i, item in enumerate(self._traverse()):
            if i == index:
                return item.value
        raise IndexError(f'Index {index} is out of range')
    
tree = IndexableNode(
    10, 
    left = IndexableNode(
        5, 
        left = IndexableNode(2),
        right = IndexableNode(
            6,
            right = IndexableNode(7))),
    right = IndexableNode(
        15,
        left = IndexableNode(11)))

print('Tree is', list(tree))
print('LRR is', tree.left.right.right.value)
print('Index 0 is', tree[0])
print('Index 1 is', tree[1])
print('11 in the tree?', 11 in tree)
print('17 in the tree?', 17 in tree)

len(tree) #does not work - Problem!

#solution
class SequenceNode(IndexableNode):
    def __len__(self):
        for count, _ in enumerate(self._traverse(), 1):
            pass
        return count

tree = SequenceNode(
    10, 
    left = SequenceNode(
        5, 
        left = SequenceNode(2),
        right = SequenceNode(
            6,
            right = SequenceNode(7))),
    right = SequenceNode(
        15,
        left = SequenceNode(11)))

print('Tree lenght is', len(tree))

"""However this isn't enough. Defining your own class also implies 
    defining every operation you may want to do with the function.
    To avoid this, we will use the built-in collections.abc
"""
from collections.abc import Sequence

class BadType(Sequence):
    pass

foo = BadType() #error - implement __getitem__ and __len__

#Correcting (afyer implementing the methods above, it provides the 
#remaining methods like index and count automatically)
class BetterNode(SequenceNode, Sequence):
    pass

tree = BetterNode(
    10, 
    left = BetterNode(
        5, 
        left = BetterNode(2),
        right = BetterNode(
            6,
            right = BetterNode(7))),
    right = BetterNode(
        15,
        left = BetterNode(11)))

print('Index of 7 is', tree.index(7))
print('Count of 10 is', tree.count(10))