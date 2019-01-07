

"""Validate BST.


"""

"""boilerplate below"""


class TreeNode(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def create_min_bst(arr, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    root = TreeNode(data = arr[mid])
    root.left = create_min_bst(arr, start, mid-1)
    root.right = create_min_bst(arr, mid+1, end)

    return root


'''
def create_min_bst(arr):
    if len(arr) == 0:
        return None

    mid = len(arr) // 2
    root = TreeNode(data = arr[mid])
    root.left = create_min_bst(arr[:mid])
    root.right = create_min_bst(arr[mid+1:])

    return root
'''



"""boilerplate above"""


def check_bst(node):
    return check_bst_rec(node, None, None)


def check_bst_rec(node, min, max):

    if node is None:
        return True

    if (max is not None and node.data >= max) or (min is not None and node.data <= min):
        return False

    if (not check_bst_rec(node.left, min, node.data)) or (not check_bst_rec(node.right, node.data, max)):
        return False

    return True


def check_bst2(node):
    return check_bst_rec2(node, None, None)


def check_bst_rec2(node, min, max):
    if node is None:
        return True
    if min is not None and max is None:
        if node.data >= min:
            return False
    if max is not None and min is None:
        if node.data <= max:
            return False
    if (not check_bst_rec2(node.right, min, node.data)) or (not check_bst_rec2(node.left, node.data, max)):
        return False

    return True



from collections import deque


def build_arr_from_root(root, d):

    if root is not None:
        d.append(root.data)
        #print(root.data)
        build_arr_from_root(root.left, d)

        build_arr_from_root(root.right, d)

    return d







sorted_arr = [2, 4, 6, 8, 10, 20]


root = create_min_bst(sorted_arr, 0, len(sorted_arr)-1)
#root = create_min_bst(sorted_arr)

print(check_bst(root))
print(check_bst2(root))



print('')

d = deque()

queue = build_arr_from_root(root, d)

'''
tree_arr = list()
for elem in queue:
    tree_arr.append(elem)
    print(elem)

print('')
print(*tree_arr)

'''


# left visited first, then root, then rightmost
# so data output in ascending order
# you want to flatten the tree back into its original sequence,
def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.data)
        in_order_traversal(root.right)

# in bst arr form
# explore the roots before inspecting any leaves, you pick pre-order
# to create a copy of the tree in an array output or stack


def pre_order_traversal(root):
    if root is not None:
        print(root.data)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

# when you want to explore the leaves first before the roots
# maybe you want to delete a tree from leaf to root


def post_order_traversal(root):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data)


#in_order_traversal(root)

pre_order_traversal(root)
print('')
post_order_traversal(root)

