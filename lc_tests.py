#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from love_calculator import *

class TestAlgorithmCount(unittest.TestCase):

    def test_trivial_examples(self):
        name1 = "Zhen Mingzi" name2 = "Michelle Obama"

        self.assertEqual(count(name1, name2), sllist([2, 1, 0, 3, 0]))

        name1 = "Yong Cesuo"
        name2 = "John Crapper"

        self.assertEqual(count(name1, name2), sllist([0, 3, 0, 2, 1]))

class TestAlgorithmAdd(unittest.TestCase):
    def test_trivial_examples(self):
        my_sllist = sllist([2, 3, 0, 2, 1])
        self.assertEqual(add(my_sllist), 85)

        my_sllist = sllist([1, 0, 0, 3, 2])
        self.assertEqual(add(my_sllist), 52)

        my_sllist = sllist([1, 0, 0, 4, 1])
        self.assertEqual(add(my_sllist), 64)

class TestAlgorithm(unittest.TestCase):

    def test_trivial_examples(self):
        name1 = "Barack Obama"
        name2 = "Michelle Robinson"

        self.assertEqual(add(count(name1, name2)), 85)

    def test_infinite_loops_return_one_percent(self):
        name1 = "Esperanza Alvarez"
        name2 = "Elisabeth Ruiz"

        self.assertEqual(add(count(name1, name2)), 1)

if __name__=='__main__':
    unittest.main()

