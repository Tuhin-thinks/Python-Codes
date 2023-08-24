
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert_node(self, data):

        x = self.root
        y = None

        # iterative approach
        while x is not None:
            y = x
            if data < x.data:
                x = x.left
            else:
                x = x.right

        if y is None:
            y = Node(data)
        elif data < y.data:
            y.left = Node(data)
        else:
            y.right = Node(data)

        return y

    def inorder_traversal(self, node: Node):
        if node is None:
            return

        if node.left is not None:
            self.inorder_traversal(node.left)

        print(node.data, end=" ")

        if node.right is not None:
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node: Node):
        if node is None:
            return

        print(node.data, end=" ")

        if node.left is not None:
            self.preorder_traversal(node.left)

        if node.right is not None:
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node: Node):
        if node is None:
            return

        if node.left is not None:
            self.postorder_traversal(node.left)

        if node.right is not None:
            self.postorder_traversal(node.right)

        print(node.data, end=" ")

    def level_order_traversal(self):
        if self.root is None:
            return

        queue = [self.root]

        while len(queue) > 0:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)


if __name__ == '__main__':
    tree = Tree()
    _root = tree.root = tree.insert_node(1)
    _root.left = Node(2)
    _root.right = Node(3)
    _root.left.left = Node(4)
    _root.left.right = Node(5)
    # tree.insert_node(2)
    # tree.insert_node(3)
    # tree.insert_node(4)
    # tree.insert_node(5)

    print("InOrder Traversal")
    tree.inorder_traversal(_root)

    print("\nLevel Order Traversal")
    tree.level_order_traversal()

    print("\nPreOrder Traversal")
    tree.preorder_traversal(tree.root)
