class binary_tree:
    def __init__(self):
        self.root = None


class tree_node:
    def __init__(self, data):
        self.left_pntr = None
        self.right_pntr = None
        self.data = data


def inorder_traversal(root_tree):
    if root_tree:
        inorder_traversal(root_tree.left_pntr)
        print(root_tree.data, end='->')
        inorder_traversal(root_tree.right_pntr)


def postorder_traversal(root_tree):
    if root_tree:
        postorder_traversal(root_tree.left_pntr)
        postorder_traversal(root_tree.right_pntr)
        print(root_tree.data, end='->')


def preorder_traversal(root_tree):
    if root_tree:
        print(root_tree.data, end='->')
        preorder_traversal(root_tree.left_pntr)
        preorder_traversal(root_tree.right_pntr)


my_tree = binary_tree()
node1 = tree_node(1)
node2 = tree_node(2)
node3 = tree_node(3)
node4 = tree_node(4)
node5 = tree_node(5)

my_tree.root = node1
node1.left_pntr = node2
node1.right_pntr = node3
node2.left_pntr = node4
node2.right_pntr = node5

print('Tree made')
print('here is the inorder traversal of this tree:')
inorder_traversal(my_tree.root)
print('\nhere is the postorder traversal of this tree:')
postorder_traversal(my_tree.root)
print('\nhere is the preorder traversal of this tree:')
preorder_traversal(my_tree.root)
