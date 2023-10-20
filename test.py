import unittest
from main import BinaryTree
from main import invert_binary_tree


class TestBinaryTree(unittest.TestCase):

    def test_invert_binary_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        invert = invert_binary_tree(root)

        self.assertEqual(invert.value, 3)
        self.assertEqual(invert.left.value, 20)
        self.assertEqual(invert.right.value, 9)


if __name__ == '__main__':
    unittest.main()


