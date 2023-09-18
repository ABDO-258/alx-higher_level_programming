#!/usr/bin/python3
""" unitest for Square"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys


class TestSqure(unittest.TestCase):
    """test case for rectangle """

    def setUp(self):
        """ reset for test test """
        Base._Base__nb_objects = 0

    def test_square_01(self):
        s1 = Square(10)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

        r2 = Square(55, 20, 5, 8)
        self.assertEqual(r2.id, 8)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(r2.size, 55)
        self.assertEqual(r2.x, 20)
        self.assertEqual(r2.y, 5)

        r3 = Square(1, 5)
        self.assertEqual(r3.id, 2)

        r4 = Square(10, 0, 0, 12)
        self.assertEqual(r4.id, 12)

        
        

    def test_square_arg(self):
        
        s1 = Square(2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)

        with self.assertRaises(TypeError):
            s2 = Square()
        
        with self.assertRaises(TypeError):
            new = Square(10, 10, 10, 21, 61)


        #
        with self.assertRaises(ValueError):
            sec2 = Square(1, 1, -6)

        with self.assertRaises(TypeError):
            sec3 = Square("1", 1)

        with self.assertRaises(TypeError):
            sec4 = Square({}, 1)

        with self.assertRaises(TypeError):
            sec5 = Square([1, 2], 1)

    def test_square_area(self):

        r1 = Square(3)
        self.assertEqual(r1.area(), 9)

        r2 = Square(8, 7, 2, 4)
        self.assertEqual(r2.area(), 64)

    def test_the_display_0_method(self):
        r1 = Square(4)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()

        sys.stdout = sys.__stdout__
        outputvalue = captured_output.getvalue()

        self.assertEqual(outputvalue, "g####\n####\n####\n####\n")

    def test_the_display_1_method(self):
        r1 = Square(2, 3, 2, 2)
        captured_output = StringIO()
        sys.stdout = captured_output
        r1.display()

        sys.stdout = sys.__stdout__
        outputvalue = captured_output.getvalue()

        self.assertEqual(outputvalue, "\n\n   ##\n   ##\n")

    def test_the_str_method(self):

        r1 = Square(4, 6, 2, 12)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Square] (12) 6/2 - 4")

        r2 = Square(5, 5, 1)
        outbut2 = str(r2)
        self.assertEqual(outbut2, "[Square] (1) 5/1 - 5")

    def test_the_update_0_method(self):
        r1 = Square(10, 10, 10, 10)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Square] (10) 10/10 - 10")

        r1.update(89)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Square] (89) 10/10 - 10")

        r1.update(89, 2)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Square] (89) 10/10 - 2")

        r1.update(89, 2, 3)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Square] (89) 3/10 - 2")

        r1.update(89, 2, 3, 4)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Square] (89) 3/4 - 2")


    def test_the_update_1_method(self):
        r1 = Square(10, 10, 10, 10)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Square] (10) 10/10 - 10")

        r1.update(size=1)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Square] (10) 10/10 - 1")

        r1.update(width=15, x=2)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Square] (10) 2/10 - 15")

        r1.update(y=1, width=2, x=3, id=89)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Square] (89) 3/1 - 2")

        r1.update(x=1, height=2, y=3, width=4)
        outbut1 = str(r1)
        self.assertEqual(outbut1, "[Square] (89) 1/3 - 4")


if __name__ == '__main__':
    unittest.main()
