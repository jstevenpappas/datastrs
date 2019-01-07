
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


def find_size(head):
    if head is None:
        return 0
    idx = find_size(head.next) + 1
    return idx


def find_kth_to_last_2(head, kth):
    sz = find_size(head)
    nodes_up = sz - kth
    n = head
    while nodes_up > 0:
        n = n.next
        nodes_up -= 1
    return n.data


def find_kth_slow_fast_runners(head, kth):
    slow = head
    fast = head
    # move fast kth places up in the Linked List
    for i in range(kth):
        fast = fast.next
    # now move both at same pace, when fast hits None, slow will be at right place
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow.data




llist = LinkedList()


for i in range(0, 10):

    llist.append(i)

#llist.iterate()


#sz = find_size(llist.head)


#print(find_kth_to_last_2(llist.get_head(), 2))


#print(find_kth_to_last(llist.get_head(), 2))


print(find_kth_slow_fast_runners(llist.head, 2))

# size
#print(find_size(llist.get_head()))