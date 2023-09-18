#!/usr/bin/python3
""" unitest for Bases"""
import unittest
from models.base import Base


class Testbase(unittest.TestCase):
    def test_base_task1(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        b5 = Base(12)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)
        self.assertEqual(b5.id, 12)


if __name__ == '__main__':
    unittest.main()
