"""

    Remove Dupes:

        Write code to remove duplicates from an unsorted LinkedList
        Additional ques: how to solve if temp buffer is not allowed?

        Hints:
            1) try a HashTable?  You can do this in a single pass of the LinkedList
            2) w/out extra space you'll need O(N^2) time.
                Try using 2 ptrs where the 2nd searches ahead of the first

"""
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
            self.head = self.head.next
            return self.head

        n = self.head
        while n.next is not None:
            if n.next.data == data:
                n.next = n.next.next
                return self.head
            n = n.next

    def remove_dupes(self):
        data_hash = dict()

        n = self.head

        # add the first val to table
        while n is not None:
            if n.data in data_hash.keys():
                self.remove_node(n.data)

            # otherwise just put the data the table for further inspection
            data_hash.update({n.data: n.data})
            # iterate to next node
            n = n.next

        print(data_hash)


    def remove_dupes_no_ds(self):

        current = self.head

        while current is not None:

            runner = current

            while runner.next is not None:

                if runner.next.data == current.data:
                    self.remove_node(current.data)

                runner = runner.next

            current = current.next



def main():

    ll = LinkedList()
    for i in range(0, 5):
        ll.append(i)

    ll.append(4)
    ll.append(4)

    ll.iterate()

    print('')

    ll.remove_dupes_no_ds()
    #ll.remove_dupes()

    ll.iterate()




if __name__ == "__main__":
    main()