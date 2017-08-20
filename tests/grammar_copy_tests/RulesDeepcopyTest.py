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

    def test_globalChange(self):
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


if __name__ == '__main__':
    main()
