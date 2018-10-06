import unittest
from homework_2.func_distance import distance_two_dots


class DistanceTest(unittest.TestCase):
    def test_zero(self):
        res = distance_two_dots(0, 0, 0, 0)
        self.assertEqual(res, 0)

    def test_one(self):
        res = distance_two_dots(0, 0, 0, 1)
        self.assertEqual(res, 1)

    def test_two(self):
        res = distance_two_dots(0, 0, 1, 1)
        self.assertEqual(res, 2**0.5)



