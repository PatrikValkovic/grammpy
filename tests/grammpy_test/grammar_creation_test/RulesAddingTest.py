#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 22:13
:Licence MIT
Part of grammpy

"""

from unittest import TestCase, main

from grammpy.exceptions import NotRuleException, RuleException
from grammpy.old_api import Nonterminal, Grammar, Rule


class A(Nonterminal):
    pass


class B(Nonterminal):
    pass


class C(Nonterminal):
    pass


class D(Nonterminal):
    pass


class RuleAtoB(Rule):
    fromSymbol = A
    toSymbol = B


class RuleBtoC(Rule):
    fromSymbol = B
    right = [C]


class RuleCto0D(Rule):
    fromSymbol = B
    right = [0, D]


class RuleDtoA(Rule):
    fromSymbol = D
    toSymbol = A


class RuleWithoutLeftSide(Rule):
    toSymbol = B

class EmptyRule(Rule):
    pass


class RulesAddingTest(TestCase):
    def test_shouldAddOneRule(self):
        g = Grammar(nonterminals=[A, B, C, D],
                    rules=[RuleAtoB])
        self.assertTrue(g.have_rule(RuleAtoB))
        self.assertFalse(g.have_rule(RuleBtoC))
        self.assertFalse(g.have_rule([RuleAtoB, RuleCto0D]))

    def test_shouldAddMoreRules(self):
        g = Grammar(terminals=[0],
                    nonterminals=[A, B, C, D],
                    rules=[RuleAtoB, RuleBtoC, RuleCto0D])
        self.assertTrue(g.have_rule(RuleAtoB))
        self.assertTrue(g.have_rule([RuleAtoB, RuleBtoC, RuleCto0D]))
        self.assertFalse(g.have_rule([RuleAtoB, RuleCto0D, RuleDtoA]))

    def test_shouldNotAddOneNotRule(self):
        with self.assertRaises(NotRuleException):
            Grammar(rules=[0])

    def test_shouldNotAddOneNotRuleInMore(self):
        with self.assertRaises(NotRuleException):
            g = Grammar(terminals=[0],
                        nonterminals=[A, B, C, D],
                        rules=[RuleAtoB, RuleBtoC, RuleCto0D, 'asdf'])

    def test_shouldNotAddInvalidRule(self):
        with self.assertRaises(RuleException):
            Grammar(terminals=[0],
                    nonterminals=[A, B, C, D],
                    rules=[RuleAtoB, RuleBtoC, RuleCto0D, RuleWithoutLeftSide])

    def test_shouldNotAddRuleWithoutRuleSpecified(self):
        with self.assertRaises(RuleException):
            Grammar(rules=[EmptyRule])

if __name__ == '__main__':
    main()
