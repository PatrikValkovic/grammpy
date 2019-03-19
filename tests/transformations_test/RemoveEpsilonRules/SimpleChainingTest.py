#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.08.2017 15:48
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
        ([S], [A, B, C]),
        ([A], [0, A]),
        ([A], [EPS]),
        ([B], [A]),
        ([B], [1, 1]),
        ([B], [EPS]),
        ([C], [EPS])]


"""
S->ABC  A->0A   A->eps  B->A    B->11   B->eps  C->eps
ToEpsilon: S,A,B,C
S->ABC  A->0A   A->eps  B->A    B->11   B->eps  C->eps  S->BC   S->AC   S->AB   
                ------                  ------  ------  +++++   +++++   +++++

A->0    S->B    S->C    S->A    S->eps
++++    ++++    ++++    ++++    ++++++
"""


class SimpleChainingTest(TestCase):
    def test_simpleChainingTest(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B, C],
                    rules=[Rules],
                    start_symbol=S)
        com = ContextFree.remove_rules_with_epsilon(g)
        self.assertEqual(len(com.rules), 12)
        class RuleNewStoBC(Rule): rule=([S], [B, C])
        class RuleNewStoAC(Rule): rule=([S], [A, C])
        class RuleNewStoAB(Rule): rule=([S], [A, B])
        class RuleNewAto0(Rule): rule=([A], [0])
        class RuleNewStoB(Rule): rule=([S], [B])
        class RuleNewStoC(Rule): rule=([S], [C])
        class RuleNewStoA(Rule): rule=([S], [A])
        class RuleNewStoEPS(Rule): rule=([S], [EPS])
        self.assertIn(RuleNewStoBC, com.rules)
        self.assertIn(RuleNewStoAC, com.rules)
        self.assertIn(RuleNewStoAB, com.rules)
        self.assertIn(RuleNewAto0, com.rules)
        self.assertIn(RuleNewStoB, com.rules)
        self.assertIn(RuleNewStoC, com.rules)
        self.assertIn(RuleNewStoA, com.rules)
        self.assertIn(RuleNewStoEPS, com.rules)
        fromStoBC = list(filter(lambda x: hash(x) == hash(RuleNewStoBC), com.rules))[0]
        self.assertTrue(isclass(fromStoBC))
        self.assertTrue(issubclass(fromStoBC, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoBC.from_rule.rule, ([S], [A, B, C]))
        self.assertEqual(fromStoBC.replace_index, 0)
        fromStoAC = list(filter(lambda x: hash(x) == hash(RuleNewStoAC), com.rules))[0]
        self.assertTrue(isclass(fromStoAC))
        self.assertTrue(issubclass(fromStoAC, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoAC.from_rule.rule, ([S], [A, B, C]))
        self.assertEqual(fromStoAC.replace_index, 1)
        fromStoAB = list(filter(lambda x: hash(x) == hash(RuleNewStoAB), com.rules))[0]
        self.assertTrue(isclass(fromStoAB))
        self.assertTrue(issubclass(fromStoAB, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoAB.from_rule.rule, ([S], [A, B, C]))
        self.assertEqual(fromStoAB.replace_index, 2)
        fromAto0 = list(filter(lambda x: hash(x) == hash(RuleNewAto0), com.rules))[0]
        self.assertTrue(isclass(fromAto0))
        self.assertTrue(issubclass(fromAto0, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromAto0.from_rule.rule, ([A], [0, A]))
        self.assertEqual(fromAto0.replace_index, 1)
        fromStoA = list(filter(lambda x: hash(x) == hash(RuleNewStoA), com.rules))[0]
        self.assertTrue(isclass(fromStoA))
        self.assertTrue(issubclass(fromStoA, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoA.from_rule.rule, ([S], [A, C]))
        self.assertEqual(fromStoA.replace_index, 1)
        fromStoB = list(filter(lambda x: hash(x) == hash(RuleNewStoB), com.rules))[0]
        self.assertTrue(isclass(fromStoB))
        self.assertTrue(issubclass(fromStoB, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoB.from_rule.rule, ([S], [B, C]))
        self.assertEqual(fromStoB.replace_index, 1)
        fromStoC = list(filter(lambda x: hash(x) == hash(RuleNewStoC), com.rules))[0]
        self.assertTrue(isclass(fromStoC))
        self.assertTrue(issubclass(fromStoC, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoC.from_rule.rule, ([S], [B, C]))
        self.assertEqual(fromStoC.replace_index, 0)
        fromStoEPS = list(filter(lambda x: hash(x) == hash(RuleNewStoEPS), com.rules))[0]
        self.assertTrue(isclass(fromStoEPS))
        self.assertTrue(issubclass(fromStoEPS, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoEPS.from_rule.rule, ([S], [C]))
        self.assertEqual(fromStoEPS.replace_index, 0)
        class RuleOldAtoEps(Rule): rule=([A], [EPS])
        class RuleOldBtoEps(Rule): rule=([B], [EPS])
        class RuleOldCtoEps(Rule): rule=([C], [EPS])
        self.assertNotIn(RuleOldAtoEps, com.rules)
        self.assertNotIn(RuleOldBtoEps, com.rules)
        self.assertNotIn(RuleOldCtoEps, com.rules)

    def test_simpleChainingTestShouldNotChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B, C],
                    rules=[Rules],
                    start_symbol=S)
        ContextFree.remove_rules_with_epsilon(g)
        self.assertEqual(len(g.rules), 7)
        class RuleNewStoBC(Rule): rule=([S], [B, C])
        class RuleNewStoAC(Rule): rule=([S], [A, C])
        class RuleNewStoAB(Rule): rule=([S], [A, B])
        class RuleNewAto0(Rule): rule=([A], [0])
        class RuleNewStoB(Rule): rule=([S], [B])
        class RuleNewStoC(Rule): rule=([S], [C])
        class RuleNewStoA(Rule): rule=([S], [A])
        class RuleNewStoEPS(Rule): rule=([S], [EPS])
        self.assertNotIn(RuleNewStoBC, g.rules)
        self.assertNotIn(RuleNewStoAC, g.rules)
        self.assertNotIn(RuleNewStoAB, g.rules)
        self.assertNotIn(RuleNewAto0, g.rules)
        self.assertNotIn(RuleNewStoB, g.rules)
        self.assertNotIn(RuleNewStoC, g.rules)
        self.assertNotIn(RuleNewStoA, g.rules)
        self.assertNotIn(RuleNewStoEPS, g.rules)
        class RuleOldAtoEps(Rule): rule=([A], [EPS])
        class RuleOldBtoEps(Rule): rule=([B], [EPS])
        class RuleOldCtoEps(Rule): rule=([C], [EPS])
        self.assertIn(RuleOldAtoEps, g.rules)
        self.assertIn(RuleOldBtoEps, g.rules)
        self.assertIn(RuleOldCtoEps, g.rules)

    def test_simpleChainingTestShouldChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B, C],
                    rules=[Rules],
                    start_symbol=S)
        ContextFree.remove_rules_with_epsilon(g, True)
        class RuleNewStoBC(Rule): rule=([S], [B, C])
        class RuleNewStoAC(Rule): rule=([S], [A, C])
        class RuleNewStoAB(Rule): rule=([S], [A, B])
        class RuleNewAto0(Rule): rule=([A], [0])
        class RuleNewStoB(Rule): rule=([S], [B])
        class RuleNewStoC(Rule): rule=([S], [C])
        class RuleNewStoA(Rule): rule=([S], [A])
        class RuleNewStoEPS(Rule): rule=([S], [EPS])
        self.assertIn(RuleNewStoBC, g.rules)
        self.assertIn(RuleNewStoAC, g.rules)
        self.assertIn(RuleNewStoAB, g.rules)
        self.assertIn(RuleNewAto0, g.rules)
        self.assertIn(RuleNewStoB, g.rules)
        self.assertIn(RuleNewStoC, g.rules)
        self.assertIn(RuleNewStoA, g.rules)
        self.assertIn(RuleNewStoEPS, g.rules)
        fromStoBC = list(filter(lambda x: hash(x) == hash(RuleNewStoBC), g.rules))[0]
        self.assertTrue(isclass(fromStoBC))
        self.assertTrue(issubclass(fromStoBC, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoBC.from_rule.rule, ([S], [A, B, C]))
        self.assertEqual(fromStoBC.replace_index, 0)
        fromStoAC = list(filter(lambda x: hash(x) == hash(RuleNewStoAC), g.rules))[0]
        self.assertTrue(isclass(fromStoAC))
        self.assertTrue(issubclass(fromStoAC, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoAC.from_rule.rule, ([S], [A, B, C]))
        self.assertEqual(fromStoAC.replace_index, 1)
        fromStoAB = list(filter(lambda x: hash(x) == hash(RuleNewStoAB), g.rules))[0]
        self.assertTrue(isclass(fromStoAB))
        self.assertTrue(issubclass(fromStoAB, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoAB.from_rule.rule, ([S], [A, B, C]))
        self.assertEqual(fromStoAB.replace_index, 2)
        fromAto0 = list(filter(lambda x: hash(x) == hash(RuleNewAto0), g.rules))[0]
        self.assertTrue(isclass(fromAto0))
        self.assertTrue(issubclass(fromAto0, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromAto0.from_rule.rule, ([A], [0, A]))
        self.assertEqual(fromAto0.replace_index, 1)
        fromStoA = list(filter(lambda x: hash(x) == hash(RuleNewStoA), g.rules))[0]
        self.assertTrue(isclass(fromStoA))
        self.assertTrue(issubclass(fromStoA, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoA.from_rule.rule, ([S], [A, C]))
        self.assertEqual(fromStoA.replace_index, 1)
        fromStoB = list(filter(lambda x: hash(x) == hash(RuleNewStoB), g.rules))[0]
        self.assertTrue(isclass(fromStoB))
        self.assertTrue(issubclass(fromStoB, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoB.from_rule.rule, ([S], [B, C]))
        self.assertEqual(fromStoB.replace_index, 1)
        fromStoC = list(filter(lambda x: hash(x) == hash(RuleNewStoC), g.rules))[0]
        self.assertTrue(isclass(fromStoC))
        self.assertTrue(issubclass(fromStoC, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoC.from_rule.rule, ([S], [B, C]))
        self.assertEqual(fromStoC.replace_index, 0)
        fromStoEPS = list(filter(lambda x: hash(x) == hash(RuleNewStoEPS), g.rules))[0]
        self.assertTrue(isclass(fromStoEPS))
        self.assertTrue(issubclass(fromStoEPS, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoEPS.from_rule.rule, ([S], [C]))
        self.assertEqual(fromStoEPS.replace_index, 0)
        class RuleOldAtoEps(Rule): rule=([A], [EPS])
        class RuleOldBtoEps(Rule): rule=([B], [EPS])
        class RuleOldCtoEps(Rule): rule=([C], [EPS])
        self.assertNotIn(RuleOldAtoEps, g.rules)
        self.assertNotIn(RuleOldBtoEps, g.rules)
        self.assertNotIn(RuleOldCtoEps, g.rules)


if __name__ == '__main__':
    main()
