

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


def insert_node(root, data):
    if data <= root.data:
        if root.left:
            insert_node(root.left, data)
        else:
            node = TreeNode(data=data)
            root.left = node
    elif data > root.data:
        if root.right:
            insert_node(root.right, data)
        else:
            node = TreeNode(data=data)
            root.right = node


def get_min_value_node(root):
    current = root
    while current.left is not None:
        current = current.left
    return current


def delete_node(root, val):
    # base case
    if root is None:
        return root
    # If the key to be deleted is smaller than the root's
    # key then it lies in  left subtree
    if val < root.data:
        root.left = delete_node(root.left, val)

    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif val > root.data:
        root.right = delete_node(root.right, val)
    else:
        # If key is same as root's key, then this is the node
        # to be deleted
        #
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        else:
            #
            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            tmp = get_min_value_node(root.right)
            # Copy the inorder successor's content to this node
            root.data = tmp.data
            # Delete the inorder successor
            root.right = delete_node(root.right, tmp.data)
    return root




def find(root, val):
    if root is None:
        return False

    if root.data == val:
        return True
    else:
        if val < root.data:
            return find(root.left, val)
        else:
            return find(root.right, val)


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

def pre_order_traversal(root):
    if root is not None:
        print(root.data)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
root = create_min_bst(sorted_arr, 0, len(sorted_arr)-1)

print(check_bst(root))



pre_order_traversal(root)

insert_node(root, 11)


print('after insert 11')
pre_order_traversal(root)

print(check_bst(root))

print(find(root, 11))

print(get_min_value_node(root).data)


new_root = delete_node(root, 11)

print(check_bst(new_root))


pre_order_traversal(new_root)