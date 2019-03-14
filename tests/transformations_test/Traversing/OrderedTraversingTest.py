#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 24.12.2017 12:21
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


class OrderedTraversingTest(TestCase):
    def testTraversePreOrder(self):
        g = Grammar(terminals=[0],
                    nonterminals=[A],
                    rules=[Rules],
                    start_symbol=A)
        res = cyk(g, [0])
        resp = Traversing.preOrder(res)
        self.assertIsInstance(resp[0], A)
        self.assertIsInstance(resp[1], Rules)
        self.assertIsInstance(resp[2], Terminal)
        self.assertEqual(resp[2].s, 0)

    def testTraversePostOrder(self):
        g = Grammar(terminals=[0],
                    nonterminals=[A],
                    rules=[Rules],
                    start_symbol=A)
        res = cyk(g, [0])
        resp = Traversing.postOrder(res)
        self.assertIsInstance(resp[2], A)
        self.assertIsInstance(resp[1], Rules)
        self.assertIsInstance(resp[0], Terminal)
        self.assertEqual(resp[0].s, 0)


if __name__ == '__main__':
    main()
