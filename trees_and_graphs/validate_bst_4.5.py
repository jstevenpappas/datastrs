

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






sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root = create_min_bst(sorted_arr, 0, len(sorted_arr)-1)


print(check_bst(root))