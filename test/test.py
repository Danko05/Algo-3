import unittest

from src.main import max_chain


class TestMaxChain(unittest.TestCase):
    def test_max_chain(self):
        self.assertEqual(max_chain(['b', 'bcad', 'bca', 'bad', 'bd']), 4)
        self.assertEqual(max_chain(['abc', 'ab', 'a']), 3)
        self.assertEqual(max_chain(['word', 'anotherword', 'yetanotherword']), 1)
        self.assertEqual(max_chain(['crates', 'car', 'cats', 'crate', 'rate', 'at', 'ate', 'tea', 'rat', 'a']), 6)


if __name__ == '__main__':
    unittest.main()
