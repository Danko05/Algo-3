import unittest
from search import search, arr


class TestSearch(unittest.TestCase):
    def test_search_with_valid_k(self):
        k = len(arr)
        result = search(arr, k)
        self.assertTrue(result is not None)
        print("Тест пройшов успішно")

    def test_search_with_invalid_k(self):
        k = len(arr) + 1
        with self.assertRaises(IndexError):
            search(arr, k)

    def test_search_with_k_equals_1(self):
        arr = [15, -7, 22, 9, 36, 2, 42, 18]
        k = 1
        result = search(arr, k)
        self.assertEqual(result, "елемент за індексом- 42, позиція елементу- 6")





if __name__ == '__main__':

    unittest.main()
