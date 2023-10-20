class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.right = None
        self.left = None


def invert_binary_tree(tree) -> BinaryTree:
    if tree is None:
        return None

    invert_binary_tree(tree.right)
    invert_binary_tree(tree.left)
    tree.left, tree.right = tree.right, tree.left
    return tree


def print_binary_tree(tree: BinaryTree):
    if tree is not None:
        print(tree.value)
        print_binary_tree(tree.left)
        print_binary_tree(tree.right)


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

new_root = invert_binary_tree(root)
print_binary_tree(new_root)


