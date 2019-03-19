#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.12.2017 19:28
:Licence MIT
Part of grammpy

"""
from unittest import main, TestCase
from grammpy import *
from grammpy.parsers import cyk
from grammpy.transforms import *


class S(Nonterminal): pass
class Rules(Rule):
    rules = [
        ([S], [1]),
        ([S], [0])
    ]


class SimpleTest(TestCase):
    def test_rewriteSimple0(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S],
                    rules=[Rules],
                    start_symbol=S)
        res = cyk(g, [0])
        res = InverseCommon.splitted_rules(res)
        self.assertIsInstance(res, S)
        self.assertIsInstance(res.to_rule, Rules)

    def test_rewriteSimple1(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S],
                    rules=[Rules],
                    start_symbol=S)
        res = cyk(g, [1])
        res = InverseCommon.splitted_rules(res)
        self.assertIsInstance(res, S)
        self.assertIsInstance(res.to_rule, Rules)


if __name__ == '__main__':
    main()
