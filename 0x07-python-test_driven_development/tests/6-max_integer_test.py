#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""

    def test_doc(self):
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 0)

        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_max_integer_positive(self):
        """postive numbers edge cases"""

        test_list = [4, 6, 9, 10, 5]
        self.assertEqual(max_integer(test_list), 10)

        test_list = (5, 20, 1, 100)
        self.assertEqual(max_integer(test_list), 100)

        test_list = ((5, 20, 1, 100), (4, 6, 9, 10, 5))
        self.assertEqual(max_integer(test_list), (5, 20, 1, 100))

        test_list = [[5, 20, 1, 100], [4, 6, 9, 10, 5]]
        self.assertEqual(max_integer(test_list), [5, 20, 1, 100])

        test_list = ["Victor", "Ade"]
        self.assertEqual(max_integer(test_list), "Victor")

    def test_max_integer_negative(self):
        test_list = [-1, -90, -10, -2]
        self.assertEqual(max_integer(test_list), -1)

    def test_max_integer_none_or_zero(self):
        """None and zero edge cases"""

        test_list = []
        self.assertEqual(max_integer(test_list), None)

        test_list = [0, 0, 0, 0]
        self.assertEqual(max_integer(test_list), 0)

        test_list = {}
        self.assertEqual(max_integer(test_list), None)

        test_list = ()
        self.assertEqual(max_integer(test_list), None)

        self.assertEqual(max_integer(), None)

    def test_not_list(self):
        """test not correct data type edge cases"""

        test_list = [1, 2, "tope", 6]
        self.assertRaises(TypeError)

        test_list = [[5, 6], 70, 2]
        self.assertRaises(TypeError)

        test_list = 5
        self.assertRaises(TypeError)

        test_list = (1, 5, 9, 0)
        self.assertRaises(TypeError)

        test_list = {1, 5, 9, 0}
        self.assertRaises(TypeError)

        test_list = "Tope"
        self.assertRaises(TypeError)

        test_list = None
        self.assertRaises(TypeError)


if __name__ == "__main__":
    unittest.main()
