"""Linked List implementation."""


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def append(self, data):
        new_node = Node(data)
        # empty LL so set head, here - head and tail are same b/c only 1 Node
        if self.head is None:
            self.tail = new_node
            self.head = self.tail
        else:
            self.tail.next = new_node # add to node to chain
            self.tail = new_node      # set new value for tail


    def iterate(self):

        _head = self.head

        while _head is not None:
            print('Curr node val: {data}'.format(data=_head.data))
            _head = _head.next


    def remove_node(self, data):

        if self.head.data == data:
            self.head = self.head.next
            return self.head

        n = self.head
        while n.next is not None:
            if n.next.data == data:
                n.next = n.next.next
                return self.head
            n = n.next



    def get_node(self, data):
        print('entry')

        if self.head.data == data:
            return self.head

        n = self.head
        while n.next is not None:
            if n.next.data == data:
                print('llooking for node')
                return n.next
            n = n.next

        return None