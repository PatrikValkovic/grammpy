#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.08.2017 16:01
:Licence MIT
Part of grammpy

"""
from inspect import isclass
from unittest import TestCase, main
from grammpy import *
from grammpy.transforms import ContextFree


class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class Rules(Rule):
    rules = [
        ([S], [1, B]),
        ([A], [1, B]),
        ([A], [EPS]),
        ([B], [EPS]),
        ([B], [1, C]),
        ([C], [1, 1])]


"""
S->1B   A->1B   A->eps  B->eps  B->1C   C->11
ToEpsilon: A,B
S->1B   A->1B   A->eps  B->eps  B->1C   C->11   S->1    A->1
                ------  ------                  ++++    ++++
"""


class SimpleTest(TestCase):
    def test_simpleTest(self):
        g = Grammar(terminals=[1],
                    nonterminals=[S, A, B, C],
                    rules=[Rules])
        com = ContextFree.remove_rules_with_epsilon(g)
        self.assertEqual(com.rules.size(), 6)
        class RuleNewS(Rule): rule=([S], [1])
        class RuleNewA(Rule): rule=([A], [1])
        self.assertIn(RuleNewS, com.rules)
        self.assertIn(RuleNewA, com.rules)
        fromS = list(filter(lambda x: hash(x) == hash(RuleNewS), com.rules))[0]
        self.assertEqual(fromS.fromSymbol, S)
        self.assertEqual(fromS.toSymbol, 1)
        self.assertTrue(isclass(fromS))
        self.assertTrue(issubclass(fromS, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromS.from_rule.rule, ([S], [1, B]))
        self.assertEqual(fromS.replace_index, 1)
        fromA = list(filter(lambda x: hash(x) == hash(RuleNewA), com.rules))[0]
        self.assertEqual(fromA.fromSymbol, A)
        self.assertEqual(fromA.toSymbol, 1)
        self.assertTrue(isclass(fromA))
        self.assertTrue(issubclass(fromA, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromA.from_rule.rule, ([A], [1, B]))
        self.assertEqual(fromA.replace_index, 1)
        class OldA(Rule): rule=([A], [EPS])
        class OldB(Rule): rule=([B], [EPS])
        self.assertNotIn(OldA, com.rules)
        self.assertNotIn(OldB, com.rules)

    def test_simpleTestShouldNotChange(self):
        g = Grammar(terminals=[1],
                    nonterminals=[S, A, B, C],
                    rules=[Rules])
        ContextFree.remove_rules_with_epsilon(g)
        self.assertEqual(g.rules.size(), 6)
        class RuleNewS(Rule): rule=([S], [1])
        class RuleNewA(Rule): rule=([A], [1])
        self.assertNotIn(RuleNewS, g.rules)
        self.assertNotIn(RuleNewA, g.rules)
        class OldA(Rule): rule=([A], [EPS])
        class OldB(Rule): rule=([B], [EPS])
        self.assertIn(OldA, g.rules)
        self.assertIn(OldB, g.rules)

    def test_simpleTestShouldChange(self):
        g = Grammar(terminals=[1],
                    nonterminals=[S, A, B, C],
                    rules=[Rules],
                    start_symbol=S)
        ContextFree.remove_rules_with_epsilon(g, True)
        self.assertEqual(g.rules.size(), 6)
        class RuleNewS(Rule): rule = ([S], [1])
        class RuleNewA(Rule): rule = ([A], [1])
        self.assertIn(RuleNewS, g.rules)
        self.assertIn(RuleNewA, g.rules)
        fromS = list(filter(lambda x: hash(x) == hash(RuleNewS), g.rules))[0]
        self.assertEqual(fromS.fromSymbol, S)
        self.assertEqual(fromS.toSymbol, 1)
        self.assertTrue(isclass(fromS))
        self.assertTrue(issubclass(fromS, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromS.from_rule.rule, ([S], [1, B]))
        self.assertEqual(fromS.replace_index, 1)
        fromA = list(filter(lambda x: hash(x) == hash(RuleNewA), g.rules))[0]
        self.assertEqual(fromA.fromSymbol, A)
        self.assertEqual(fromA.toSymbol, 1)
        self.assertTrue(isclass(fromA))
        self.assertTrue(issubclass(fromA, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromA.from_rule.rule, ([A], [1, B]))
        self.assertEqual(fromA.replace_index, 1)
        class OldA(Rule): rule = ([A], [EPS])
        class OldB(Rule): rule = ([B], [EPS])
        self.assertNotIn(OldA, g.rules)
        self.assertNotIn(OldB, g.rules)


if __name__ == '__main__':
    main()
