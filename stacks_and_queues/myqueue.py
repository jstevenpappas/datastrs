

"""Queue implementation.

Queues are FIFO datastructures - the first one is is the first out... think convenience store.

Queue functions are:
add()
remove()
peek()
is_empty()

"""


class QueueItem(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None


class MyQueue(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        item = QueueItem(data=data)
        if self.head is None:
            self.tail = item
            self.head = self.tail
        else:
            self.tail.next = item
            self.tail = item

    def remove(self):
        if self.head is not None:
            item = self.head
            next = self.head.next
            self.head = next
            return item.data
        else:
            return None

    def peek(self):
        if self.head is not None:
            return self.head.data

    def is_empty(self):
        empty = True
        if self.head is not None:
            empty = False

        return empty


mq = MyQueue()

for i in range(10):
    print('adding following to queue: {dat}'.format(dat=i))
    mq.add(data=i)


for i in range(10):
    print('removing following from queue: {dat}'.format(dat=mq.remove()))
    print('peeking what item is next in queue: {pk}'.format(pk=mq.peek()))
    print('is the queue empty yet?:  {empty}'.format(empty=mq.is_empty()))
