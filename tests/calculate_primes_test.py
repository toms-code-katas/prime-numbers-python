import unittest
from primes.calculate_primes import calculate_primes, InvalidRangeException


class CalculatePrimesTests(unittest.TestCase):

    def test_calculate_primes_to_10(self):
        self.assertEqual(calculate_primes(start=1, stop=10), [2, 3, 5, 7])

    def test_calculate_primes_to_100(self):
        self.assertEqual(calculate_primes(start=1, stop=100),
                                 [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                                  47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_calculate_primes_for_negative_ranges(self):
        self.assertRaises(InvalidRangeException, calculate_primes, -100, 0)
        self.assertRaises(InvalidRangeException, calculate_primes, -100, 100)
        self.assertRaises(InvalidRangeException, calculate_primes, 10, -50)

    def test_stop_smaller_than_start(self):
        self.assertRaises(InvalidRangeException, calculate_primes, 50, 10)
