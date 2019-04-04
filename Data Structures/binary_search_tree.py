class BST(object):
    def __init__(self):
        self.root = None

    def insertion(self, key):
        if self.root:
            self.root.insertion(key)
        else:
            self.root = node(key)

    def child_count(self, node_found):
        count = 0
        if node_found.right_child:
            count += 1
        if node_found.left_child:
            count += 1
        return (count)

    def lookup(self, key, parent_node):
        if not (self.root):
            return None, None
        return self.root.lookup(key, parent_node)

    def deletion_wrapper(self, key):

        node_tobe_del, node_tobe_del_parent = self.lookup(key, None)
        count_child = self.child_count(node_tobe_del)

        if not (node_tobe_del_parent):
            if count_child is 1:
                if self.root.left_child:
                    self.root = self.root.left_child
                else:
                    self.root = self.root.right_child

            elif count_child is 2:
                minval = self.root.min_val(self.root.right_child)
                my_bst.deletion_wrapper(minval)
                self.root.data = minval
            else:
                self = None
        else:
            self.root.deletion(count_child, node_tobe_del, node_tobe_del_parent)


class node(object):
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None

    def insertion(self, key):
        if key > self.data:
            if self.right_child is None:
                self.right_child = node(key)
            else:
                self.right_child.insertion(key)
        else:
            if self.left_child is None:
                self.left_child = node(key)
            else:
                self.left_child.insertion(key)

    def deletion(self, count_child, node_found, parent):

        if count_child is 0:
            if parent.left_child is node_found:
                parent.left_child = None
            else:
                parent.right_child = None
            return

        elif count_child is 1:
            if parent.left_child is node_found:
                if node_found.left_child:
                    parent.left_child = node_found.left_child
                else:
                    parent.left_child = node_found.right_child
            elif parent.right_child is node_found:
                if node_found.left_child:
                    parent.right_child = node_found.left_child
                else:
                    parent.right_child = node_found.right_child
            return
        else:
            minval = self.min_val(node_found.right_child)
            my_bst.deletion_wrapper(minval)
            node_found.data = minval
            return

    def inorder_traversal(self):
        if self:
            if self.left_child:
                self.left_child.inorder_traversal()
            print(self.data, end='->')
            if self.right_child:
                self.right_child.inorder_traversal()

    def lookup(self, key, parent_node):

        if self.data > key:
            parent_node = self
            node_found = self.left_child
            return self.left_child.lookup(key, parent_node)
        elif self.data < key:
            parent_node = self
            node_found = self.right_child
            return self.right_child.lookup(key, parent_node)
        else:
            # print(root_tree.data, parent_node.data)
            return self, parent_node

    def min_val(self, node_found_rightchild):

        if node_found_rightchild.left_child:
            minval = node_found_rightchild.left_child.data
            return self.min_val(node_found_rightchild.left_child)

        else:
            minval = node_found_rightchild.data
            return minval


if __name__ == '__main__':
    my_bst = BST()

    my_bst.insertion(5)

    my_bst.insertion(4)
    my_bst.insertion(3)
    my_bst.insertion(10)
    my_bst.insertion(7)
    my_bst.insertion(11)

    my_bst.root.inorder_traversal()
    print('\n')

    my_bst.deletion_wrapper(3)

    my_bst.root.inorder_traversal()




