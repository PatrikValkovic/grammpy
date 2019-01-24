#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 10:04
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase

from grammpy.old_api import Rule
from grammpy.exceptions import NotASingleSymbolException


class Single(Rule):
    rule = ([0], [1])


class TwoRight(Rule):
    rule = ([0], [1, 2])


class ThreeLeft(Rule):
    rule = ([0, 1, 'a'], [2])


class Multiple(Rule):
    rule = ([0, 1, 2], [3, 4])


class FromRuleComputeTest(TestCase):
    def test_single(self):
        self.assertEqual(Single.left, [0])
        self.assertEqual(Single.right, [1])
        self.assertEqual(Single.fromSymbol, 0)
        self.assertEqual(Single.toSymbol, 1)

    def test_twoRight(self):
        self.assertEqual(TwoRight.left, [0])
        self.assertEqual(TwoRight.right, [1, 2])
        self.assertEqual(TwoRight.fromSymbol, 0)
        with self.assertRaises(NotASingleSymbolException):
            x = TwoRight.toSymbol

    def test_threeLeft(self):
        self.assertEqual(ThreeLeft.left, [0, 1, 'a'])
        self.assertEqual(ThreeLeft.right, [2])
        with self.assertRaises(NotASingleSymbolException):
            x = ThreeLeft.fromSymbol
        self.assertEqual(ThreeLeft.toSymbol, 2)

    def test_multiple(self):
        self.assertEqual(Multiple.left, [0, 1, 2])
        self.assertEqual(Multiple.right, [3, 4])
        with self.assertRaises(NotASingleSymbolException):
            x = Multiple.fromSymbol
        with self.assertRaises(NotASingleSymbolException):
            x = Multiple.toSymbol


if __name__ == '__main__':
    main()
