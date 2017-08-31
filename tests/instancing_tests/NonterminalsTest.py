#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 11:55
:Licence GNUv3
Part of grammpy

"""


from unittest import TestCase, main
from grammpy import *
from grammpy.exceptions import TreeDeletedException

class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class From(Rule): rule = ([C], [A, B])
class To(Rule): rule = ([A], [B, C])


class NonterminalsTest(TestCase):
    def test_correctChild(self):
        a = A()
        t = To()
        a._set_to_rule(t)
        self.assertEqual(a.to_rule, t)

    def test_correctParent(self):
        a = A()
        f = From()
        a._set_from_rule(f)
        self.assertEqual(a.from_rule, f)

    def test_deleteParent(self):
        a = A()
        f = From()
        a._set_from_rule(f)
        self.assertEqual(a.from_rule, f)
        del f
        with self.assertRaises(TreeDeletedException):
            a.from_rule

    def test_shouldNotDeleteChild(self):
        a = A()
        t = To()
        a._set_to_rule(t)
        del t
        a.to_rule



if __name__ == '__main__':
    main()
