#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 16.03.2019 17:16
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import *
from grammpy.parsers import cyk
from grammpy.transforms import *


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class Rule1(Rule): rule = ([A], [B, C])
class Rule2(Rule): rule = ([B], [0])
class Rule3(Rule): rule = ([C], [1])


class SeparatedTraversingTest(TestCase):
    def test_shouldTraverse(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C],
                    rules=[Rule1, Rule2, Rule3],
                    start_symbol=A)
        root = cyk(g, [0, 1])
        def traverse_func(item, callback):
            if isinstance(item, Rule):
                yield item
                for el in item.to_symbols:
                    yield callback(el)
            elif isinstance(item, Nonterminal):
                yield item
                yield callback(item.to_rule)
            else:
                yield item
        gen = Traversing.traverse(root, traverse_func)
        res = list(gen)
        self.assertTrue(isinstance(res[0], A))
        self.assertTrue(isinstance(res[1], Rule1))
        self.assertTrue(isinstance(res[2], B))
        self.assertTrue(isinstance(res[3], Rule2))
        self.assertTrue(isinstance(res[4], Terminal))
        self.assertEqual(res[4].s, 0)
        self.assertTrue(isinstance(res[5], C))
        self.assertTrue(isinstance(res[6], Rule3))
        self.assertTrue(isinstance(res[7], Terminal))
        self.assertEqual(res[7].s, 1)


if __name__ == '__main__':
    main()
