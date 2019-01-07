



from linked_list_impl import LinkedList


"""
    Delete Middle Node
    
    Implement an algorithm to delete a node in the middle  (i.e., any node but the first and last, not nec. the exact 
    middle) of a singly linked list given only access to that node.


"""


'''
This will not work where the node to remove is the tail.
This is b/c the list is a singlylinked list and the only way to manipulate pointers is via next... 
unless you set the last node to a dummy

'''


def remove_node(node):
    if node is None or node.next is None:
        return False
    # get a handle to the next node
    next = node.next
    node.data = next.data
    node.next = next.next
    return True




llist = LinkedList()


for i in range(0, 10):

    llist.append(i)


llist.iterate()


n = llist.get_node(9)

if n is not None:
    print(n.data)
    remove_node(n)
else:
    print('node not found')


llist.iterate()