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
    def test_maxAtEndOfList(self):
        result = max_integer([8, 3, 5, 6, 7])
        self.assertEqual(result, 8)
    def test_maxInMiddle(self):
        result = max_integer([1, 1, 2, 1, 0])
        self.assertEqual(result, 2)
    def test_oneNegNumInList(self):
        result = max_integer([1, -1, 1, 3])
        self.assertEqual(result, 3)
    def test_listOfNegNum(self):
        result = max_integer([-2, -1, -4, -3])
        self.assertEqual(result, -1)
    def test_listWithOneEle(self):
        result = max_integer([1])
        self.assertEqual(result, 1)
