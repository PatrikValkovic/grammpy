#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 22:00
:Licence MIT
Part of grammpy

"""

from unittest import TestCase, main

from grammpy import *
from grammpy.exceptions import \
    RuleNotDefinedException, \
    TerminalDoesNotExistsException, \
    NonterminalDoesNotExistsException


class InvalidRuleTest(TestCase):
    def test_undefinedRule(self):
        class R(Rule): pass
        with self.assertRaises(RuleNotDefinedException):
            Grammar(terminals=[],
                    nonterminals=[],
                    rules=[R])

    def test_termNotInGrammar(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class C(Nonterminal): pass
        class R1(Rule): rule=([A, B], [0])
        with self.assertRaises(TerminalDoesNotExistsException):
            Grammar(terminals=[],
                    nonterminals=[A, B, C],
                    rules=[R1])
        class R2(Rule): rule=([0, B], [C])
        with self.assertRaises(TerminalDoesNotExistsException):
            Grammar(terminals=[],
                    nonterminals=[A, B, C],
                    rules=[R2])

    def test_nontermNotInGrammar(self):
        class A(Nonterminal): pass
        class B(Nonterminal): pass
        class C(Nonterminal): pass
        class R1(Rule): rule=([A, B], [C])
        with self.assertRaises(NonterminalDoesNotExistsException):
            Grammar(terminals=[],
                    nonterminals=[A, B],
                    rules=[R1])
        class R2(Rule): rule=([C, B], [B])
        with self.assertRaises(NonterminalDoesNotExistsException):
            Grammar(terminals=[],
                    nonterminals=[A, B],
                    rules=[R2])


if __name__ == '__main__':
    main()
