import unittest
from primes.calculate_primes import calculate_primes


class CalculatePrimesTests(unittest.TestCase):

    def test_calculate_primes_to_10(self):
        self.assertListEqual(calculate_primes(start=1, stop=10), [2, 3, 5, 7])

    def test_calculate_primes_to_100(self):
        self.assertListEqual(calculate_primes(start=1, stop=100),
                             [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                              89, 97])
