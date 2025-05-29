#!/usr/bin/python3
"""Unittest for max_integer([])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        """Test an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_max_at_beginning(self):
        """Test a list with max at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with positive and negative numbers"""
        self.assertEqual(max_integer([-10, 0, 5, 3]), 5)

    def test_floats(self):
        """Test a list with floats"""
        self.assertEqual(max_integer([1.5, 2.8, 3.3, 2.9]), 3.3)

    def test_strings(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(["abc", "def", "ghi"]), "ghi")

    def test_list_of_one_string(self):
        """Test a string as a list"""
        self.assertEqual(max_integer("string"), "t")


if __name__ == '__main__':
    unittest.main()
