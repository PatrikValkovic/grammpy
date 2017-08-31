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


class RulesTest(TestCase):
    def test_correctChild(self):
        t = To()
        b = B()
        c = C()
        t._to_nonterms.append(b)
        t._to_nonterms.append(c)
        self.assertEqual(t.to_nonterms[0], b)
        self.assertEqual(t.to_nonterms[1], c)
        self.assertEqual(t.to_nonterms, [b, c])






if __name__ == '__main__':
    main()
