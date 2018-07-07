

"""List of Depths.

#107:  Try modifying a graph algorithm to track the depth from the root.

#123:  A hash table or array that maps from level number to nodes at that level might be useful.

#135: You should be able to come up with an algoritm involving both depth-first and breadth-first search.

"""

from collections import defaultdict


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


def get_lists_of_depths(node, lists, depth):
    if node is None:
        return
    if depth not in lists.keys():
        dlist = list()
        lists[depth] = dlist
    else:
        dlist = lists[depth]

    dlist.append(node)
    get_lists_of_depths(node.left, lists, depth+1)
    get_lists_of_depths(node.right, lists, depth+1)


def list_of_depths(node):
    lists = defaultdict(list)
    get_lists_of_depths(node, lists, 0)
    return lists




sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root = create_min_bst(sorted_arr, 0, len(sorted_arr)-1)

lists_of_d = list_of_depths(root)

for k, v in lists_of_d.items():
    llist = lists_of_d.get(k)

    for n in llist:
        print('data of node for key/depth {kk}: {d}'.format(kk=k, d=n.data))

