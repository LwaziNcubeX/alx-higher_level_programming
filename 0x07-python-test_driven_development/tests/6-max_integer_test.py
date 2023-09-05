#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function"""
    def test_positive_integers(self):
        """Test for a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        """Test for a list of negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_zero(self):
        """Test for a list containing 0"""
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 0, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, 0, 3]), 3)

    def test_empty_list(self):
        """Test for an empty list"""
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

    def test_single_value(self):
        """Test for a list with a single value"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_all_identical_values(self):
        """Test for a list with all identical values"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_repeated_maximum_values(self):
        """Test for a list with repeated maximum values"""
        self.assertEqual(max_integer([1, 2, 3, 4, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 4, 2]), 4)

    def test_repeated_minimum_values(self):
        """Test for a list with repeated minimum values"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -4, -2]), -1)

    def test_mixed_values(self):
        """Test for a list with mixed positive, negative, and zero values"""
        self.assertEqual(max_integer([1, -2, 3, 0]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 0]), 2)
        self.assertEqual(max_integer([-1, 2, 3, 0]), 3)

    def test_noninteger_values(self):
        """Test for a list with non-integer values"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])

    def test_large_values(self):
        """Test for a list with large values"""
        self.assertEqual(max_integer([1, 2, 3, 10**26]), 10**26)


if __name__ == '__main__':
    unittest.main()
