#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import TestCase, main
from grammpy import Rule as _R, Grammar, Nonterminal as _N
from ..grammar import *
from grammpy.exceptions import RuleSyntaxException


class InvalidAddTest(TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.g = Grammar()

    def setUp(self):
        g = Grammar()
        g.add_term([0, 1, 2, 'a', 'b', 'c'])
        g.add_nonterm([NFirst, NSecond, NThird, NFourth])
        self.g = g

    def test_invalidSelf(self):
        class Tmp(_R):
            def validate(*args):
                raise RuleSyntaxException(None, None)
        self.assertEqual(self.g.rules_count(), 0)
        with self.assertRaises(RuleSyntaxException):
            self.g.have_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.get_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.add_rule(Tmp)
        self.assertEqual(self.g.rules_count(), 0)
        with self.assertRaises(RuleSyntaxException):
            self.g.have_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.get_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.rule(Tmp)

    def test_invalidFirstInArray(self):
        class Tmp(_R):
            def validate(*args):
                raise RuleSyntaxException(None, None)
        class Valid(_R):
            rule = ([NFirst], ['a', 0])
        self.assertEqual(self.g.rules_count(), 0)
        with self.assertRaises(RuleSyntaxException):
            self.g.have_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.get_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.add_rule([Tmp, Valid])
        self.assertEqual(self.g.rules_count(), 0)
        with self.assertRaises(RuleSyntaxException):
            self.g.have_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.get_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.rule(Tmp)
        self.assertFalse(self.g.have_rule(Valid))
        self.assertIsNone(self.g.get_rule(Valid))
        self.assertIsNone(self.g.rule(Valid))

    def test_invalidSecondInArray(self):
        class Tmp(_R):
            def validate(*args):
                raise RuleSyntaxException(None, None)
        class Valid(_R):
            rule = ([NFirst], ['a', 0])
        self.assertEqual(self.g.rules_count(), 0)
        with self.assertRaises(RuleSyntaxException):
            self.g.have_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.get_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.add_rule([Valid, Tmp])
        self.assertEqual(self.g.rules_count(), 0)
        with self.assertRaises(RuleSyntaxException):
            self.g.have_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.get_rule(Tmp)
        with self.assertRaises(RuleSyntaxException):
            self.g.rule(Tmp)
        self.assertFalse(self.g.have_rule(Valid))
        self.assertIsNone(self.g.get_rule(Valid))
        self.assertIsNone(self.g.rule(Valid))


if __name__ == '__main__':
    main()
