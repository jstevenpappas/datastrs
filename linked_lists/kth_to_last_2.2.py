
"""Find the Kth to last element in the list (e.g., 2nd to last, 4th to last, etc - not 4th and all b/t until last).

Hints:
1) what if we knew the linked lists size?  What's the diff b/t finding the Kth to last or Nth element?
2) If you don't know the lists size, can you compute it?  How does it affect runtime?
3)

Note:  when k=1 or k=0 is acceptable to return last element

"""
from linked_list_impl import LinkedList






def find_kth_to_last(head, kth):

    if head is None:
        return 0

    idx = find_kth_to_last(head.next, kth) + 1

    if idx == kth:
        print('found kth from last val: {val}'.format(val=head.data))
    return idx








llist = LinkedList()


for i in range(0, 10):

    llist.append(i)

#llist.iterate()

print(find_kth_to_last(llist.get_head(), 2))

