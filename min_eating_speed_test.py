import unittest
from min_speed_eating import min_eat


class min_speed_eating_test(unittest.TestCase):
    def test_min_speed(self):
        piles=[30,11,23,4,20]
        expected = min_eat(piles,6)
        self.assertEqual(expected, 23)


if __name__ == '__main__':
    unittest.main()
