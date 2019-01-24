#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 10:04
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase

from grammpy.old_api import Rule
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
