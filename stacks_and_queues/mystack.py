

"""Stack implemenation.

Stacks use LIFO ordering - the last one to go in is the first out...  think stack dinner plates

Stack functions are:
push()
pop()
peek()
is_empty()


"""


class StackItem(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyStack(object):

    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = StackItem(data=data)
        else:
            item = StackItem(data=data)
            item.next = self.top
            self.top = item

    def pop(self):
        item = self.top
        if self.top is not None:
            self.top = item.next
        return item.data

    def is_empty(self):
        empty = True
        if self.top is not None:
            empty = False
        return empty

    def peek(self):
        if self.top is not None:
            return self.top.data
        else:
            return None


'''
ms = MyStack()

for i in range(10):
    ms.push(i)
    print('current top of stack: {top}'.format(top=ms.peek()))

print('')

for i in range(12):

    if not ms.is_empty():
        print(ms.pop())
    else:
        print('stack empty')
    print('current top of stack: {top}'.format(top=ms.peek()))
'''