#!/usr/bin/python3
""" unitest for Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """test case for rectangle """

    def setUp(self):
        """ reset for test test """
        Base._Base__nb_objects = 0

    def test_rectangle_t01(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(55, 20, 5, 8)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 55)
        self.assertEqual(r2.height, 20)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 8)

        r3 = Rectangle(1, 5)
        self.assertEqual(r3.id, 3)

        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r4.id, 12)

    def test_rectangle_arg(self):
        # one arg
        with self.assertRaises(TypeError):
            rec1 = Rectangle(1)
        #
        with self.assertRaises(ValueError):
            rec2 = Rectangle(1, 1, -6)

        with self.assertRaises(TypeError):
            rec3 = Rectangle("1", 1)

        with self.assertRaises(TypeError):
            rec4 = Rectangle({}, 1)

        with self.assertRaises(TypeError):
            rec5 = Rectangle([1, 2], 1)

    def test_rectangle_area(self):

        r1 = Rectangle(2, 4)
        self.assertEqual(r1.area(), 8)

        r2 = Rectangle(8, 7, 2, 4)
        self.assertEqual(r2.area(), 56)

    def test_the_display_0_method(self):

        r1 = Rectangle(4, 3)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()

        sys.stdout = sys.__stdout__
        outputvalue = captured_output.getvalue()

        self.assertEqual(outputvalue, "####\n####\n####\n")

    def test_the_str_method(self):

        r1 = Rectangle(4, 6, 2, 1, 12)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        outbut2 = str(r2)
        self.assertEqual(outbut2, "[Rectangle] (1) 1/0 - 5/5")

    def test_the_display_1_method(self):
        r1 = Rectangle(2, 3, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()

        sys.stdout = sys.__stdout__
        outputvalue = captured_output.getvalue()

        self.assertEqual(outputvalue, "\n\n  ##\n  ##\n  ##\n")

    def test_the_str_method(self):

        r1 = Rectangle(4, 6, 2, 1, 12)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (12) 2/1 - 4/6")

        r2 = Rectangle(5, 5, 1)
        outbut2 = str(r2)
        self.assertEqual(outbut2, "[Rectangle] (1) 1/0 - 5/5")

    def test_the_update_0_method(self):
        r1 = Rectangle(10, 10, 10, 10)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (1) 10/10 - 10/10")

        r1.update(89)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (89) 10/10 - 10/10")

        r1.update(89, 2)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (89) 10/10 - 2/10")

        r1.update(89, 2, 3)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (89) 10/10 - 2/3")

        r1.update(89, 2, 3, 4)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (89) 4/10 - 2/3")

        r1.update(89, 2, 3, 4, 5)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (89) 4/5 - 2/3")

    def test_the_update_1_method(self):
        r1 = Rectangle(10, 10, 10, 10)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (1) 10/10 - 10/10")

        r1.update(height=1)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (1) 10/10 - 10/1")

        r1.update(width=1, x=2)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (1) 2/10 - 1/1")

        r1.update(y=1, width=2, x=3, id=89)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (89) 3/1 - 2/1")

        r1.update(x=1, height=2, y=3, width=4)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Rectangle] (89) 1/3 - 4/2")


if __name__ == '__main__':
    unittest.main()
