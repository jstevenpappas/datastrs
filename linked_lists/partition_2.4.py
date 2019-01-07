


from linked_list_impl import LinkedList

"""

    Partition:
    
        Write code to partition a linkedlist around a value x, such that all nodes less 
        than x come before all nodes greater than or equal to x.
        If x is contained within the list, the values of x only need to be after the elements less
        than x.  
        The partition element x can appear anywhere in the 'right partition'; it does not need to appear
        between the left and right partitions
        
        Input:  3->5->8->5->10->2->1  [partition 5]
        Output  3->1->2->10->5->5->8 
"""

# using only Node
def partlong(node, part_val):

    before_start = None
    before_end = None
    after_start = None
    after_end = None

    while node is not None:

        next = node.next
        node.next = None

        if node.data < part_val:
            if before_start is None:
                before_end = node
                before_start = before_end
            else:
                before_end.next = node
                before_end = node
        else:
            if after_start is None:
                after_end = node
                after_start = after_end
            else:
                after_end.next = node
                after_end = node

        node = next


    before_end.next = after_start

    return before_start


# using existing LinkedList impl
def partition(linked_list, part_val):
    before = LinkedList()
    after = LinkedList()
    n = linked_list.head
    while n is not None:
        if n.data < part_val:
            before.append(n.data)
        else:
            after.append(n.data)
        n = n.next
    before.tail.next = after.head
    return before


llist = LinkedList()

llist.append(3)
llist.append(5)
llist.append(8)
llist.append(5)
llist.append(10)
llist.append(2)
llist.append(1)

llist.iterate()


new_part = partition(llist, 5)

print('')
new_part.iterate()

'''
new_part = partlong(llist.head, 5)
print('')
n = new_part
while n is not None:
    #print(n.data)
    print(n.data)
    n = n.next
'''