#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..]) function"""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        unordered = [1, 4, 2, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with max value at beginning"""
        max_at_beginning = [4, 1, 2, 3]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a one element"""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_negatives(self):
        """Test a list of negative numbers"""
        negatives = [-5, -9, -1.25, -1.53, -0.5, -2.13]
        self.assertEqual(max_integer(negatives), -0.5)

    def test_floats(self):
        """Test a list of floats numbers"""
        floats = [0.33, 0.83, 1.0, -1.53, 1.67, -2.13]
        self.assertEqual(max_integer(floats), 1.67)

    def test_ints_and_floats(self):
        """Test a list of ints and floats"""
        ints_and_floats = [0.67, 1.33, 2, 2.67, 3.33, 4]
        self.assertEqual(max_integer(ints_and_floats), 4)

    def test_string(self):
        """Test a string"""
        string = "Number"
        self.assertEqual(max_integer(string), 'u')

    def test_list_of_strings(self):
        """Test a list of strings"""
        strings = ["Try", "new", "a", "number"]
        self.assertEqual(max_integer(strings), "number")

    def test_empty_string(self):
        """Test an empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
