import math


"""
enqueue or dequeue items in O(\log{n})O(logn)

BinaryHeap() creates a new, empty, binary heap.

    insert(k) adds a new item to the heap.
    find_min() returns the item with the minimum key value, leaving item in the heap.
    del_min() returns the item with the minimum key value, removing the item from the heap.
    is_empty() returns true if the heap is empty, false otherwise.
    size() returns the number of items in the heap.
    build_heap(list) builds a new heap from a list of keys.

"""


class BinaryHeap(object):

    def __init__(self):
        # single val 0 in list - not used
        #   but there for easier division
        self.items = list()

    def size(self):
        return len(self.items)

    def is_empty(self):
        empty = False
        if len(self.items) == 0:
            empty = True
        return empty

    def find_min(self):
        return self.items[0]

    # Remember - length of list - 1
    def idx_last_elem(self):
        return len(self.items) - 1


    def percolate_up(self):
        i = self.idx_last_elem()
        while i -1 // 2 > 0:
            if self.items[i] < self.items[i // 2]:
                self.items[i // 2], self.items[i] =  self.items[i], self.items[i // 2]
            i = i // 2

    # append to list (right) but compare to
    # parent and swap if it is less than
    def insert(self, k):
        self.items.append(k)
        self.percolate_up()


    def percolate_down(self, i):
        while i * 2 + 1 <= self.idx_last_elem():

            mc = self.min_child(i)
            if self.items[i] > self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc


    def min_child(self, i):

        if i * 2 + 2 > self.idx_last_elem():
            return i * 2 +1

        if self.items[i * 2 + 1] < self.items[i * 2 + 2]:
            return i * 2 + 1

        return i * 2 + 2




    # returning min val is just returning the root (at idx 1 - not zero)
    # Restore the Heap in 2 steps:
    #   1) Restore Heap Structure: restore the root by moving the last item to the root position
    #   2) Restore Heap Order: push new root down the tree to its proper position
    def delete_min(self):
        ret_val = self.items[0]  # min val at root

        # 1) restore Heap Structure
        self.items[0] = self.items[self.idx_last_elem()]

        # remove last item in list since we just moved it
        self.items.pop()

        # 2) restore Heap Order
        self.percolate_down(0)
        return ret_val


    def build_heap(self, alist):

        i = len(alist) // 2
        self.items = alist

        while i >= 0:
            self.percolate_down(i)
            i = i - 1



arr = [27, 17, 33, 21, 19, 18, 14, 11,  9, 5, 5]


bh = BinaryHeap()

for elem in arr:
    #print(bh.items)
    bh.insert(elem)
    #print(bh.find_min())



#bh.build_heap(arr)

print('initial heap')
print(bh.items)

ll = len(bh.items)


for i in range(ll):
    print('')
    print(bh.items)
    print('delete and return min: {del_min}'.format(del_min=bh.delete_min()))
    print('size of heap = {sz} is heap empty? {emp}'.format(sz=bh.size(), emp=bh.is_empty()))
