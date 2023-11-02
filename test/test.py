import unittest

from source.main import min_depth


class TestMinDepth(unittest.TestCase):
    def test_min_depth(self):
        self.assertEqual(min_depth(None), 0)


if __name__ == "__main__":
    unittest.main()
