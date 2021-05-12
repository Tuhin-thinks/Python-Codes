class Tree:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    
def preOrder(node, p=None):
    if not p:
        p = []
    if not node:
        return p
    p.append(node.data)
    preOrder(node.left, p)
    preOrder(node.right, p)
    return p

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data, end="  ")
    inOrder(root.right)

def updateTree(root, p):
    if not root:
        return
    root.data = int(p / root.data)
    updateTree(root.left, p)
    updateTree(root.right, p)

def create_tree():
    # tree = Tree(15)
    # tree.left = Tree(10)
    # tree.right = Tree(20)
    # tree.left.left = Tree(8)
    # tree.left.right =Tree(12)
    # tree.right.left = Tree(16)
    # tree.right.right = Tree(25)
    tree = Tree(1)
    tree.left = Tree(2)
    tree.right = Tree(3)

    tree.right.left = Tree(4)
    tree.right.right = Tree(5)

    print(f"Initial Inorder traversal:")
    inOrder(tree)

    pre_ordered = preOrder(tree)
    mul = 1
    for i in pre_ordered:
        mul *= i
    # print("multiplication of all nodes result =", mul)
    updateTree(tree, mul)
    print(f"\n\nAfter updating inorder traversal:")
    inOrder(tree)
    

create_tree()