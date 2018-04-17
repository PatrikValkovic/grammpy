#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 17.08.2017 13:58
:Licence GNUv3
Part of grammpy-transforms

"""



from unittest import main, TestCase

from grammpy import *
from grammpy.transforms import *


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass
class E(Nonterminal): pass
class F(Nonterminal): pass
class RuleAto0B(Rule): rule = ([A], [0, B])
class RuleBto1C(Rule): rule = ([B], [1, C])
class RuleCto01(Rule): rule = ([C], [0, 1])
class RuleDto0E(Rule): rule = ([D], [0, E])
class RuleEto1F(Rule): rule = ([E], [1, F])
class RuleFto0D(Rule): rule = ([F], [0, D])




class RecursiveSeparateTest(TestCase):
    def test_recursiveSeparateTest(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C, D, E, F],
                    rules=[RuleAto0B, RuleBto1C, RuleCto01,
                           RuleDto0E, RuleEto1F, RuleFto0D],
                    start_symbol=A)
        com = ContextFree.remove_unreachable_symbols(g)
        self.assertTrue(com.have_term([0, 1]))
        self.assertTrue(com.have_nonterm([A, B, C]))
        self.assertFalse(com.have_nonterm(D))
        self.assertFalse(com.have_nonterm(E))
        self.assertFalse(com.have_nonterm(F))

    def test_recursiveSeparateTestShouldNotChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C, D, E, F],
                    rules=[RuleAto0B, RuleBto1C, RuleCto01,
                           RuleDto0E, RuleEto1F, RuleFto0D],
                    start_symbol=A)
        ContextFree.remove_unreachable_symbols(g)
        self.assertTrue(g.have_term([0, 1]))
        self.assertTrue(g.have_nonterm([A, B, C, D, E, F]))

    def test_recursiveSeparateTestShouldChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[A, B, C, D, E, F],
                    rules=[RuleAto0B, RuleBto1C, RuleCto01,
                           RuleDto0E, RuleEto1F, RuleFto0D],
                    start_symbol=A)
        ContextFree.remove_unreachable_symbols(g, transform_grammar=True)
        self.assertTrue(g.have_term([0, 1]))
        self.assertTrue(g.have_nonterm([A, B, C]))
        self.assertFalse(g.have_nonterm(D))
        self.assertFalse(g.have_nonterm(E))
        self.assertFalse(g.have_nonterm(F))


if __name__ == '__main__':
    main()
