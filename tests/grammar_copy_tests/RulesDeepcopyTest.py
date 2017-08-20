#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.08.2017 18:45
:Licence GNUv3
Part of grammpy

"""

from copy import deepcopy
from unittest import TestCase, main
from grammpy import *


class RulesAddingTest(TestCase):
    def test_copyOfSingleRule(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class R(Rule):
            rule = ([A], [0, B])
            attr = True

        first = Grammar(terminals=[0], nonterminals=[A, B], rules=[R])
        second = deepcopy(first)
        fR = first.get_rule(R)
        fR.attr = False
        self.assertFalse(fR.attr)
        self.assertTrue(second.rules()[0].attr)

    def test_copyOfMoreRules(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class R1(Rule):
            rule = ([A], [0, B])
            attr = True
        class R2(Rule):
            rule = ([A], [1, B])
            attr = 0

        first = Grammar(terminals=[0, 1], nonterminals=[A, B], rules=[R1, R2])
        second = deepcopy(first)
        fR1 = first.get_rule(R1)
        sR1 = list(filter(lambda x: x.right[0] == 0, second.get_rule()))[0]
        self.assertTrue(fR1.attr)
        self.assertTrue(sR1.attr)
        fR1.attr = False
        self.assertFalse(fR1.attr)
        self.assertTrue(sR1.attr)
        fR2 = first.get_rule(R2)
        sR2 = list(filter(lambda x: x.right[0] == 1, second.get_rule()))[0]
        self.assertFalse(fR2.attr)
        self.assertFalse(sR2.attr)
        sR2.attr = True
        self.assertFalse(fR2.attr)
        self.assertTrue(sR2.attr)

    def test_globalChangeOnRule(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class R(Rule):
            rule = ([A], [0, B])
            attr = True

        first = Grammar(terminals=[0], nonterminals=[A, B], rules=[R])
        second = deepcopy(first)
        fR = first.get_rule(R)
        sR = second.rules()[0]
        self.assertTrue(fR.attr)
        self.assertTrue(sR.attr)
        R.attr = False
        self.assertFalse(fR.attr)
        self.assertTrue(sR.attr)

    def test_globalChangeOnNonterminal(self):
        class A(Nonterminal): prop = True
        first = Grammar(nonterminals=[A])
        second = deepcopy(first)
        fA = first.nonterms()[0]
        sA = second.nonterms()[0]
        self.assertTrue(fA.prop)
        self.assertTrue(sA.prop)
        A.prop = False
        self.assertFalse(fA.prop)
        self.assertTrue(sA.prop)

    def test_globalChangeOnMoreNonterminal(self):
        class A(Nonterminal):
            i=0
            prop = True
        class B(Nonterminal):
            i = 1
            prop = 0
        class C(Nonterminal):
            i = 2
            prop = 'asdf'
        first = Grammar(nonterminals=[A, B, C])
        second = deepcopy(first)
        fA = list(filter(lambda x: x.i == 0, first.nonterms()))[0]
        sA = list(filter(lambda x: x.i == 0, second.nonterms()))[0]
        fB = list(filter(lambda x: x.i == 1, first.nonterms()))[0]
        sB = list(filter(lambda x: x.i == 1, second.nonterms()))[0]
        fC = list(filter(lambda x: x.i == 2, first.nonterms()))[0]
        sC = list(filter(lambda x: x.i == 2, second.nonterms()))[0]
        self.assertTrue(fA.prop)
        self.assertTrue(sA.prop)
        self.assertEqual(fB.prop, 0)
        self.assertEqual(sB.prop, 0)
        self.assertEqual(fC.prop, 'asdf')
        self.assertEqual(sC.prop, 'asdf')
        A.prop = False
        B.prop = 1
        C.prop = 'x'
        self.assertFalse(fA.prop)
        self.assertTrue(sA.prop)
        self.assertEqual(fB.prop, 1)
        self.assertEqual(sB.prop, 0)
        self.assertEqual(fC.prop, 'x')
        self.assertEqual(sC.prop, 'asdf')



if __name__ == '__main__':
    main()
