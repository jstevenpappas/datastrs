
"""Min Stack.

implement a function to return the min value within a Stack
where min(), push() and pop() continue to run in constant (O(1)) time.

"""

import sys
from mystack import MyStack


class MinStack(MyStack):

    def __init__(self):
        super(MinStack, self).__init__()
        self.minstack = MyStack()

    def push(self, data):
        if data <= self.minval():
            #print('data {d} was less than minval {mv}'.format(d=data, mv=self.minval()))
            self.minstack.push(data)
            #print('new value for  minval() {mv}'.format(mv=self.minval()))
        super(MinStack, self).push(data)

    def pop(self):

        popped_val = super(MinStack, self).pop()
        if popped_val == self.minval():
            self.minstack.pop()
        return popped_val

    def minval(self):
        if self.minstack.is_empty():
            return sys.maxint  # empty so return biggest num possible
        else:
            return self.minstack.peek()


ms = MinStack()
ms.push(5)
ms.push(2)
print('')
print('current minval(): {mv}'.format(mv=ms.minval()))
ms.push(99)
ms.push(4)
ms.push(6)
ms.push(3)
ms.push(1)

while not ms.minstack.is_empty():
    print(ms.minstack.pop())

'''
print('current minval(): {mv}'.format(mv=ms.minval()))
print('popping the following: {pop}'.format(pop=ms.pop()))

print('current minval(): {mv}'.format(mv=ms.minval()))
print('popping the following: {pop}'.format(pop=ms.pop()))

print('current minval(): {mv}'.format(mv=ms.minval()))
print('popping the following: {pop}'.format(pop=ms.pop()))

print('current minval(): {mv}'.format(mv=ms.minval()))
print('popping the following: {pop}'.format(pop=ms.pop()))
print('current minval(): {mv}'.format(mv=ms.minval()))

'''