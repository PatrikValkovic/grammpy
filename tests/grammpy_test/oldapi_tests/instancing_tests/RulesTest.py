#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 11:55
:Licence MIT
Part of grammpy

"""


from unittest import TestCase, main

from grammpy.exceptions import TreeDeletedException
from grammpy.old_api import Nonterminal, Rule


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class From(Rule): rule = ([C], [A, B])
class To(Rule): rule = ([A], [B, C])


class RulesTest(TestCase):
    def test_correctChild(self):
        t = To()
        b = B()
        c = C()
        t._to_symbols.append(b)
        t._to_symbols.append(c)
        self.assertEqual(t.to_symbols[0], b)
        self.assertEqual(t.to_symbols[1], c)
        self.assertEqual(t.to_symbols, [b, c])

    def test_correctParent(self):
        t = To()
        a = A()
        t._from_symbols.append(a)
        self.assertEqual(t.from_symbols[0], a)
        self.assertEqual(t.from_symbols, [a])

    def test_correctDeleteParent(self):
        t = To()
        a = A()
        t._from_symbols.append(a)
        del a
        with self.assertRaises(TreeDeletedException):
            t.from_symbols[0]
        with self.assertRaises(TreeDeletedException):
            t.from_symbols

    def test_shouldNotDeleteChild(self):
        t = To()
        b = B()
        c = C()
        t._to_symbols.append(b)
        t._to_symbols.append(c)
        del b
        del c
        self.assertIsNotNone(t.to_symbols[0])
        self.assertIsNotNone(t.to_symbols[1])
        self.assertIsNotNone(t.to_symbols)






if __name__ == '__main__':
    main()
