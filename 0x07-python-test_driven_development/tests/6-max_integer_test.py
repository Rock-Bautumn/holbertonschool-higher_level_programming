#!/usr/bin/python3
"""
Unittesting for 6-max_integer.py - max_integer([list])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unittest test class for max int testing
    """

    def test_docstring(self):
        """Tests for a function docstring"""
        doc = max_integer.__doc__
        self.assertTrue(len(doc) > 1)

    def test_empty(self):
        """Test if the list is empty"""
        self.assertEqual(max_integer([]), None)

    def test_type(self):
        """Testing to make sure the data is a valid list"""
        self.assertIs(list, list)
        self.assertRaises(TypeError, max_integer((1, 2)))

    def test_one_int(self):
        self.assertEqual(max_integer([42]), 42)

    def test_positives(self):
        """Testing only positive integers"""
        self.assertEqual(max_integer([5, 6, 7, 8]), 8)

    def test_negatives(self):
        """Testing only negative integers"""
        self.assertEqual(max_integer([-1, -5, -999999999999]), -1)

    def test_middle_is_max(self):
        """Testing when middle value is max integer"""
        self.assertEqual(max_integer([1, 2, 100, 98, 50]), 100)

if __name__ == "__main__":
    unittest.main()
