



"""Intersection.

Given 2 (singly) linked lists, determine if the 2 lists interstect.
Return the intersecting node.
Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list is the same exact node (by reference)
as the jth node of the second linked list, then they are intersecting.

"""
from linked_list_impl import LinkedList, Node


##
#   function to find the tail of a list
##
def find_tail(l1):
    if (l1.next is None):
        return l1
    tail = find_tail(l1.next)
    return tail


# this returns a tuple consisting of both the list-tail and length of list
def find_tail_and_sz(l1, sz):
    if l1.next is None:
        return l1, 1
    tail, sz = find_tail_and_sz(l1.next, sz)
    sz = sz + 1
    return tail, sz


# we don't really remove but just iterate ahead
def trim_list(head, number_of_nodes):
    node = head
    for i in range(number_of_nodes):
        node = node.next
    return node


# both lists now have same len and can therefore be iterated at the same time to
# find where they are reference same node and, therefore, intersect
def find_intersect(l1, l2):
    if (l1 is not None and l1 is not None) and l1 == l2:
        return l1
    intersect = find_intersect(l1.next, l2.next)
    return intersect



# common list that insects
node_h = Node('h')
node_i = Node('i')
node_j = Node('j')
node_h.next = node_i
node_i.next = node_j

# head start list 1
node_a = Node('a')
node_b = Node('b')
node_c = Node('c')
node_d = Node('d')

# head start list 2
node_e = Node('e')
node_f = Node('f')
node_g = Node('g')

# create the 2 lists that intersect with node_h
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_h # intersection

node_e.next = node_f
node_f.next = node_g
node_g.next = node_h # intersection


##
#   need to confirm they are intersection lists by testing if they share the same tail
##
tail_a = find_tail(node_a)
tail_e = find_tail(node_e)

print(find_tail(node_a).data)
if tail_a == tail_e:
    print('both point to same tail')

tail_node_l1, list_len = find_tail_and_sz(node_a, 0)
print('tail node val = {v} and size of list = {sz}'.format(v=tail_node_l1.data, sz=list_len))

tail_node_l2, list_len = find_tail_and_sz(node_e, 0)
print('tail node val = {v} and size of list = {sz}'.format(v=tail_node_l2.data, sz=list_len))


# need to add in logic to test which node has greater len and therefore needs to be trimmed
# but for now, I know it is node_a the larger and needs shortening
trimmed_node = trim_list(node_a, 1)

# both lists are same size and point of intersection can be found via recursion
intersecting_node = find_intersect(node_e, trimmed_node)

print(intersecting_node.data)