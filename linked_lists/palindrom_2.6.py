

"""Palindrome.
Implement a function to check if a list is a palindrome.


#5: a palindrom is something which is the same when written forwards and backwards.
What if you reversed the linkedlist?

#13: Try using a stack.

#29: Assume you have the length of the linkedlist. Can you implement this recursively?

#

"""


from linked_list_impl import LinkedList, Node
from collections import deque


def is_palindrome_stack(linked_list):
    stk = deque()
    cmp_head = linked_list.head
    stk_head = linked_list.head
    while stk_head is not None:
        stk.appendleft(stk_head.data)
        stk_head = stk_head.next
    while cmp_head is not None:
        if cmp_head.data != stk.pop():
            return False
        cmp_head = cmp_head.next
    return True






# get the length of the LinkedList using recursion
def get_ll_len(head):

    if head is None:
        return 0

    len = get_ll_len(head.next) + 1

    return len


def get_rev(head, ll=LinkedList()):
    # base case is when we hit the tail
    if head.next is None:
        # we are at the tail so its data append it now...
        ll.append(head.data)
        return head
    tail = get_rev(head.next)
    # as we recurse out, we'll be doing so from the back of the list
    ll.append(head.data)
    return ll


def is_palindrome(orig_list):
    # get the reverse of the original list
    rev_list = get_rev(orig_list.head)
    forward_node = orig_list.head
    rev_node = rev_list.head
    while forward_node.next is not None:
        if forward_node.data != rev_node.data:
            return False
        else:
            forward_node = forward_node.next
            rev_node = rev_node.next
    return True

    '''
    # could have also used the length and a for loop though it seems unnecessary
    
    # get the len
    len = get_ll_len(orig_list.head)
    
    # now iterate over both and return False equal on any elements, otherwise True
    for i in range(len):
        if forward_node.data != rev_node.data:
            return False
        else:
            forward_node = forward_node.next
            rev_node = rev_node.next
    return True
    '''


mlist = LinkedList()

mlist.append('r')
mlist.append('a')
mlist.append('d')
mlist.append('a')
mlist.append('r')
#mlist.append('r')


print(is_palindrome(mlist))


print(is_palindrome_stack(mlist))

'''


mlist = LinkedList()

for i in range(10):
    mlist.append(i)

mlist.iterate()

print('')


ret_list = get_rev(mlist.head)

ret_list.iterate()


#llen = get_ll_len(mlist.head)
#print(llen)



#mlist.iterate()

'''
