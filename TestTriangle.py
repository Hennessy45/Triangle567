# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: Ht
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        self.assertEqual(classify_triangle(3,4,5),'Right')

    def testRightTriangleB(self):
        self.assertEqual(classify_triangle(5,3,4),'Right')

    def testRightTriangleC(self):
        self.assertEqual(classify_triangle(13, 12, 5), 'Right')

    def testRightTriangleD(self):
        self.assertEqual(classify_triangle(8, 6, 10), 'Right')

    def testEquilateralTriangleA(self):
        self.assertEqual(classify_triangle(1,1,1),'Equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classify_triangle(10,10,10),'Equilateral')

    def testIsocelesTriangleA(self):
        self.assertEqual(classify_triangle(3, 3, 2),'Isoceles')

    def testIsocelesTriangleB(self):
        self.assertEqual(classify_triangle(4, 6, 6),'Isoceles')

    def testIsocelesTriangleC(self):
        self.assertEqual(classify_triangle(6, 4, 6),'Isoceles')

    def testIsocelesTriangleD(self):
        self.assertEqual(classify_triangle(6, 6, 4),'Isoceles')

    def testScaleneTriangleA(self):
        self.assertEqual(classify_triangle(10, 15, 12),'Scalene')

    def testInvalidInputA(self):
        self.assertEqual(classify_triangle(-1, -1, -1),'InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classify_triangle(201, 201, 201),'InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classify_triangle("200", "0", "0"),'InvalidInput')

    def testNotATriangleA(self):
        self.assertEqual(classify_triangle(5, 1, 1),'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classify_triangle(1, 5, 1),'NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classify_triangle(1, 1, 5),'NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
unittest.main()


