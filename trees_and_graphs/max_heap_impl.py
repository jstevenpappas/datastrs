
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
class BinaryHeapMax(object):

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


    """
    PercolateUp - Comparing to parents
        1) elem by elem comparing node to parent and percolating up
        
        
    """
    def percolate_up(self):
        i = self.idx_last_elem()
        while i -1 // 2 > 0:
            if self.items[i] > self.items[i // 2]:
                self.items[i // 2], self.items[i] =  self.items[i], self.items[i // 2]
            i = i // 2

    # append to list (right) but compare to
    # parent and swap if it is less than
    def insert(self, k):
        self.items.append(k)
        self.percolate_up()


    '''
    PercolateDown - comparing to children
    '''
    def percolate_down(self, i, end=-1):
        # while there is a left child
        while i * 2 + 1 <= end:
            mc = self.max_child(i, end=end)
            if self.items[i] < self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def max_child(self, i, end=-1):

        # if the right_child for this node is beyond the index
        if i * 2 + 2 > end:
            # return the left one
            return i * 2 +1

        # if the left is gtr than the right
        if self.items[i * 2 + 1] > self.items[i * 2 + 2]:
            # return the left
            return i * 2 + 1
        # else, return the right
        return i * 2 + 2



    # returning min val is just returning the root (at idx 1 - not zero)
    # Restore the Heap in 2 steps:
    #   1) Restore Heap Structure: restore the root by moving the last item to the root position
    #   2) Restore Heap Order: push new root down the tree to its proper position
    def delete_max(self):
        ret_val = self.items[0]  # min val at root

        # 1) restore Heap Structure
        self.items[0] = self.items[self.idx_last_elem()]

        # remove last item in list since we just moved it
        self.items.pop()

        end = self.idx_last_elem()
        # 2) restore Heap Order
        self.percolate_down(0, end=end)
        return ret_val


    def heapify(self, alist):

        i = len(alist) // 2
        self.items = alist

        end = self.idx_last_elem()

        while i >= 0:
            self.percolate_down(i, end=end)
            i = i - 1

    def heap_sort(self):

        end = self.idx_last_elem()

        while end > 0:
            self.items[0], self.items[end] = self.items[end], self.items[0]

            end = end - 1

            self.percolate_down(0, end=end)







arr = [27, 17, 33, 21, 19, 18, 14, 11,  9, 5]
bh = BinaryHeapMax()

'''
for elem in arr:
    #print(bh.items)
    bh.insert(elem)
    #print(bh.find_min())
'''

print('initial array')
print(arr)




print('initial heap')
bh.heapify(arr)
print(bh.items)

print('post sort')
bh.heap_sort()

print(bh.items)

'''
ll = len(bh.items)
for i in range(ll):
    print('')
    print(bh.items)
    print('delete and return max: {del_min}'.format(del_min=bh.delete_max()))
    print('size of heap = {sz} is heap empty? {emp}'.format(sz=bh.size(), emp=bh.is_empty()))
'''