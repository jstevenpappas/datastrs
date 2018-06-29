"""Loop Detection.


Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.


Definition

Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node,
so as to make a loop in the linked list.

E.g.,
Input:  A->B->C->D->E->C [same as the C earlier]

Output: C


"""
from linked_list_impl import LinkedList, Node


def loop_detector(head):
    slow = head  # moves 1 step at a time
    fast = head  # moves 2 steps at a time

    # step 1: find where they converge in loop
    while (fast is not None) and (fast.next is not None):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            print('slow and fast collided on node: {collision}'.format(collision=slow.data))
            break

    # if is a non-cylce, fast will be None so handle it
    if (fast is None) or (fast.next is None):
        print('No loop detected - returning None.')
        return None

    # leave fast at convergence-node but move slow to head
    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    # when while loop exits, both ptrs will have landed on loop-head
    print('slow starting at head and fast from collision-node, moving both 1 step lands'
          'them on the following loop-head: {lh}'.format(lh=fast.data))
    return fast


node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')
node_e = Node('e')


node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_e
# loop introduction where tail should be
node_e.next = node_c


loop_head = loop_detector(node_a)

print('head of loop: {lh}'.format(lh=loop_head.data))


'''
##
#   Alternate Solution using external datatructure.
#   Finds loop using a hash counter: the first node that occurs twice during iteration
#   is the beginning of the loop
##
from collections import defaultdict

def find_loop(head):
    looped_node = None
    tracker = defaultdict(int)
    node = head
    while node is not None:
        print('the value of this node: {data}'.format(data=node.data))
        tracker[node.data] += 1
        if tracker[node.data] > 1:
            looped_node = node.data
            break
        node = node.next
    return looped_node

print(find_loop(node_a))
'''








