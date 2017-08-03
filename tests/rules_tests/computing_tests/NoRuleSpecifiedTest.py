#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase
from grammpy import Rule
from grammpy.exceptions import RuleNotDefinedException


class NoRuleSpecifiedTest(TestCase):
    def test_noRule(self):
        class tmp(Rule):
            x = 5

        with self.assertRaises(RuleNotDefinedException):
            x = tmp.rules
        with self.assertRaises(RuleNotDefinedException):
            x = tmp.rule
        with self.assertRaises(RuleNotDefinedException):
            x = tmp.left
        with self.assertRaises(RuleNotDefinedException):
            x = tmp.right
        with self.assertRaises(RuleNotDefinedException):
            x = tmp.fromSymbol
        with self.assertRaises(RuleNotDefinedException):
            x = tmp.toSymbol


if __name__ == '__main__':
    main()