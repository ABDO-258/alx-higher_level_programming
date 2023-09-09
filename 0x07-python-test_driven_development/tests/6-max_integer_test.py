#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_list1(self):
        list1 = [1, 2, 3, 4]
        self.assertEqual(max_integer(list1), 4)
        list2 = [1, -2, 3, -4]
        self.assertEqual(max_integer(list2), 3)

    def test_list2(self):
        list1 = [1, 3, 4, 2]
        self.assertEqual(max_integer(list1), 4)
        list2 = [1, 2.6, 3, 4.6]
        self.assertEqual(max_integer(list2), 4.6)

    def test_list3(self):
        list1 = []
        self.assertEqual(max_integer(list1), None)
        list2 = [12]
        self.assertEqual(max_integer(list2), 12)

    def test_list4(self):
        list1 = [0]
        self.assertEqual(max_integer(list1), 0)
        list2 = [12.9, 2.6, 3, 4.6]
        self.assertEqual(max_integer(list2), 12.9)

    def test_string(self):
        list1 = "abdelhadi"
        self.assertEqual(max_integer(list1), 'l')
        list2 = ""
        self.assertEqual(max_integer(list2), None)

    def test_list_of_string(self):
        list1 = ["first", "abdelhadi", "last", "karbal"]
        self.assertEqual(max_integer(list1), 'last')


if __name__ == '__main__':
    unittest.main()
