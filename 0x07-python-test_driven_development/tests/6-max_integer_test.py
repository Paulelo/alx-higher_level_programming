#!/usr/bin/pyhton3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer"). max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, 2, 5, 3]), 5)
        self.assertAlmostEqual(max_integer([5, 4, 3, 2]), 5)
        self.assertAlmostEqual(max_integer([5, 6, 7, 8]), 8)
        self.assertAlmostEqual(max_integer([2, 9, 4]), 9)
        self.assertAlmostEqual(max_integer([5, 4, -7, 12]), 12)
        self.assertAlmostEqual(max_integer([-5, -2, -4, -3]), -2)
        self.assertAlmostEqual(max_integer([18]), 18)
        self.assertAlmostEqual(max_integer([]), None)
