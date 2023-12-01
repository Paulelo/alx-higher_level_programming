#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_normal(self):
        result = max_integer([1, 5, 3, 7])
        self.assertEqual(result, 7)
    def test_none(self):
        result1 = max_integer([])
        self.assertEqual(result1, None)
    def test_equalist(self):
        result = max_integer([1, 1, 1, 1])
        self.assertEqual(result, 1)
