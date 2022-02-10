import unittest
from primes.calculate_primes import calcualte_primes


class CalculatePrimesTests(unittest.TestCase):
    def test_calculate_primes(self):
        self.assertListEqual(calcualte_primes(start=1, end=10), [2, 3, 5, 7])
