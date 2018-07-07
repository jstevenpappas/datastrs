

"""Check Balanced

Write a function to check if a binary tree is balanced.
For this ques., a balanced tree is defined to be a tree such that the heights of the 2 subtrees
of any node never differ by more than 1.


"""

import sys
import math



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



def check_height(node):

    if node is None:
        return -1

    left = check_height(node.left) + 1
    right = check_height(node.right) + 1

    #print('left height = {lh}'.format(lh=left))
    #print('right height = {rh}'.format(rh=right))

    diff = left - right

    if abs(diff) > 1:
        return 0
    else:
        return max(left, right)




sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root = create_min_bst(sorted_arr, 0, len(sorted_arr)-1)


print(check_height(root))

