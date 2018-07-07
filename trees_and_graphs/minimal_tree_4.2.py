

"""Minimal Tree.
Given a sorted (increasing order) array with uniq integer elements, write an algorithm
to create a binary search tree with minimal height.

#19: a min BST has about the same number of nodes on the left as on the right.
Focusing on the root for now, how would you ensure the same number of nodes are on the left as on the right?

#73: You could implement this by finding the 'ideal' next element to add and repeatedly calling insertValue().
This will be inefficient as you would continually have to traverse the tree.
Try recursion instead.
Can you divide this problem into subproblems?

#116:


"""

class TreeNode(object):

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def pre_order_trav(node):
    if node is not None:
        print('node.data = {d}'.format(d=node.data))
        pre_order_trav(node.left)
        print('done left')
        pre_order_trav(node.right)
        print('done right')

def in_order_trav(node):
    if node is not None:
        in_order_trav(node.left)
        print('node.data = {d}'.format(d=node.data))
        in_order_trav(node.right)


def create_min_bst(arr, start, end):

    if end < start:
        return None

    mid = (start + end) // 2

    root = TreeNode(data = arr[mid])

    root.left = create_min_bst(arr, start, mid-1)
    root.right = create_min_bst(arr, mid+1, end)

    return root





sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


root = create_min_bst(sorted_arr, 0, len(sorted_arr)-1)

in_order_trav(root)

