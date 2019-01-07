"""Remove Dupes.

Write code to remove duplicates from an unsorted LinkedList
Additional ques: how to solve if temp buffer is not allowed?

Hints:
1) try a HashTable?  You can do this in a single pass of the LinkedList
2) w/out extra space you'll need O(N^2) time.
Try using 2 ptrs where the 2nd searches ahead of the first

"""

from collections import defaultdict

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, data):
        new_node = Node(data)
        # empty LL so set head, here - head and tail are same b/c only 1 Node
        if self.head is None:
            self.tail = new_node
            self.head = self.tail
        else:
            self.tail.next = new_node
            self.tail = new_node


    def iterate(self):

        _head = self.head

        while _head is not None:
            print('Curr node val: {data}'.format(data=_head.data))
            _head = _head.next


    def remove_node(self, data):

        if self.head.data == data:
            print('REMOVING HEAD')
            self.head = self.head.next
            return self.head

        n = self.head
        while n.next is not None:
            print('SEARCHING FOR NODE TO REMOVE')
            if n.next.data == data:
                n.next = n.next.next
                return self.head
            n = n.next

    def remove_dupes(self):
        data_hash = defaultdict(int)
        n = self.head
        # iterate over the Linked List
        while n is not None:
            # increment the counter for this node
            data_hash[n.data] += 1
            # see if the node is in the dict
            if data_hash[n.data] > 1:
                # if so, call remove on it
                self.remove_node(n.data)
            # iterate to next node
            n = n.next

    def remove_dupes_no_ds(self):
        current = self.head
        while current is not None:
            runner = current
            while runner.next is not None:
                print('using runner to find dupes and eliminate them')
                if runner.next.data == current.data:
                    print('found a dupe to remove: dupe = {dupe}'.format(dupe=current.data))
                    self.remove_node(current.data)
                runner = runner.next
            current = current.next



def main():

    ll = LinkedList()
    for i in range(0, 10):
        ll.append(i)

    ll.append(4)
    ll.append(4)

    ll.iterate()

    elem = 9

    print('')

    ll.remove_dupes_no_ds()
    #ll.remove_dupes()

    ll.iterate()




if __name__ == "__main__":
    main()