import unittest

from src.main import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        patterns = ["asdf", "asghj", "qazx", "asuikmn"]
        for pattern in patterns:
            self.trie.insert(pattern)

    def test_search(self):
        self.assertTrue(self.trie.search("asdf"))
        self.assertEqual(self.trie.search("asghj"), True)
        self.assertEqual(self.trie.search("ghjkjg"), False)
        self.assertFalse(self.trie.search("gfdjjdfp"))

    def test_starts_with(self):
        self.assertTrue(self.trie.start_whit("as"))
        self.assertEqual(self.trie.start_whit("qaz"), True)


if __name__ == "__main__":
    unittest.main()
