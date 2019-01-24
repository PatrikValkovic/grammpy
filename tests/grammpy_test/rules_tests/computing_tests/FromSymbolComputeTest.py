#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 10:04
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy.old_api import Rule


class Simple(Rule):
    fromSymbol = 0
    toSymbol = 1


class FromSymbolComputeTest(TestCase):
    def test_rules_simple(self):
        r = Simple.rules
        self.assertIsInstance(r, list)
        self.assertEqual(len(r), 1)
        self.assertIsInstance(r[0], tuple)
        self.assertEqual(r[0][0], [0])
        self.assertEqual(r[0][1], [1])

    def test_rule_simple(self):
        r = Simple.rule
        self.assertIsInstance(r, tuple)
        self.assertEqual(r[0], [0])
        self.assertEqual(r[1], [1])

    def test_leftRight_simple(self):
        self.assertEqual(Simple.left, [0])
        self.assertEqual(Simple.right, [1])


if __name__ == '__main__':
    main()
