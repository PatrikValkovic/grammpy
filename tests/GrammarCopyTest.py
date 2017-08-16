#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 16.08.2017 19:16
:Licence GNUv3
Part of grammpy

"""

from copy import deepcopy, copy
from unittest import main, TestCase
from grammpy import *


class A(Nonterminal):
    pass


class B(Nonterminal):
    pass


class RuleAtoB(Rule):
    rule = ([A], [B])


class GrammarCopyTest(TestCase):
    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.g = Grammar()

    def setUp(self):
        self.g = Grammar(terminals=[0, 1],
                         nonterminals=[A, B],
                         rules=[RuleAtoB],
                         start_symbol=A)

    def test_shouldNotDeleteTerminals(self):
        g = copy(self.g)
        g.remove_term()
        self.assertTrue(self.g.have_term([0, 1]))
        self.assertFalse(g.have_term(0))
        self.assertFalse(g.have_term(1))


    def test_shouldNotDeleteNonterminals(self):
        g = copy(self.g)
        g.remove_nonterm()
        self.assertTrue(self.g.have_nonterm([A, B]))
        self.assertFalse(g.have_term(A))
        self.assertFalse(g.have_term(B))

    def test_shouldNotDeleteRules(self):
        g = copy(self.g)
        g.remove_rule()
        self.assertTrue(self.g.have_rule(RuleAtoB))
        self.assertFalse(g.have_rule(RuleAtoB))

    def test_shouldNotChangeStartSymbol(self):
        g = copy(self.g)
        g.start_set(None)
        self.assertTrue(self.g.start_is(A))
        self.assertFalse(g.start_is(A))



if __name__ == '__main__':
    main()
