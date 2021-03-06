#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 24.12.2017 11:40
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import *
from grammpy.parsers import cyk
from grammpy.transforms import *


class A(Nonterminal): pass
class Rules(Rule):
    rule=([A], [0])


class TraversingTraverseTest(TestCase):
    def testTraversingOwnTypes(self):
        g = Grammar(terminals=[0],
                    nonterminals=[A],
                    rules=[Rules],
                    start_symbol=A)
        res = cyk(g, [0])
        def trav(item, callback):
            self.assertTrue(isinstance(item, (A, Rules, Grammar)))
        Traversing.traverse(res, trav)

    def testAIn(self):
        g = Grammar(terminals=[0],
                    nonterminals=[A],
                    rules=[Rules],
                    start_symbol=A)
        res = cyk(g, [0])
        def trav(item, callback):
            self.assertTrue(isinstance(item, A))
        Traversing.traverse(res, trav)


if __name__ == '__main__':
    main()
