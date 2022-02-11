import unittest
from primes.calculate_primes import calculate_primes


class CalculatePrimesTests(unittest.TestCase):

    def test_calculate_primes(self):
        self.assertListEqual(calculate_primes(start=1, stop=10), [2, 3, 5, 7])
