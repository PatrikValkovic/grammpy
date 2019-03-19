#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 22.08.2017 21:14
:Licence MIT
Part of grammpy

"""
from inspect import isclass
from unittest import main, TestCase
from grammpy import *
from grammpy.transforms import ContextFree


class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class Rules(Rule):
    rules = [
        ([S], [0, B, 0]),
        ([S], [A]),
        ([A], [0, A]),
        ([A], [B]),
        ([B], [1, B]),
        ([B], [A, B]),
        ([B], [C]),
        ([B], [EPS]),
        ([C], [1, A]),
        ([C], [1])]


"""
 ---------------------------------
 |   S   |   A   |   B   |   C   |
----------------------------------
S|  []   |  [2]  | [2,4] |[2,4,7]|
----------------------------------
A|       |  []   |  [4]  | [4,7] |
----------------------------------
B|       |       |  []   |  [7]  |
----------------------------------
C|       |       |       |  []   |
----------------------------------

S->0B0  S->A  A->0A  A->B  B->1B  B->AB  B->C  B->EPS  C->1A  C->1
        ----         ----                ----              
        
S->A->0A
S->A->B->1B
S->A->B->AB
S->A->B->eps
S->A->B->C->1A
S->A->B->C->1
A->B->1B
A->B->AB
A->B->eps
A->B->C->1A
A->B->C->1    
B->C->1A
B->C->1    
"""


class SimpleTest(TestCase):
    def test_simpleTest(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B, C],
                    rules=[Rules],
                    start_symbol=S)
        com = ContextFree.remove_unit_rules(g)
        # Removed
        class RuleStoA(Rule): rule=([S], [A])
        self.assertNotIn(RuleStoA, com.rules)
        class RuleAtoB(Rule): rule=([A], [B])
        self.assertNotIn(RuleAtoB, com.rules)
        class RuleBtoC(Rule): rule=([B], [C])
        self.assertNotIn(RuleBtoC, com.rules)
        # Old rules
        class RuleNewSto0B0(Rule): rule = ([S], [0, B, 0])
        self.assertIn(RuleNewSto0B0, com.rules)
        class RuleNewAto0A(Rule): rule = ([A], [0, A])
        self.assertIn(RuleNewAto0A, com.rules)
        class RuleNewBto1B(Rule): rule = ([B], [1, B])
        self.assertIn(RuleNewBto1B, com.rules)
        class RuleNewBtoAB(Rule): rule = ([B], [A, B])
        self.assertIn(RuleNewBtoAB, com.rules)
        class RuleNewBtoEPS(Rule): rule = ([B], [EPS])
        self.assertIn(RuleNewBtoEPS, com.rules)
        class RuleNewCto1A(Rule): rule = ([C], [1, A])
        self.assertIn(RuleNewCto1A, com.rules)
        class RuleNewCto1(Rule): rule = ([C], [1])
        self.assertIn(RuleNewCto1, com.rules)
        # New rules
        class RuleNewSto0A(Rule): rule = ([S], [0, A])
        self.assertIn(RuleNewSto0A, com.rules)
        fromSto0A = list(filter(lambda x: hash(x) == hash(RuleNewSto0A), com.rules))[0]
        self.assertTrue(isclass(fromSto0A))
        self.assertTrue(issubclass(fromSto0A, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto0A.by_rules), 1)
        self.assertEqual(fromSto0A.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto0A.end_rule.rule, ([A], [0, A]))
        class RuleNewSto1B(Rule): rule = ([S], [1, B])
        self.assertIn(RuleNewSto1B, com.rules)
        fromSto1B = list(filter(lambda x: hash(x) == hash(RuleNewSto1B), com.rules))[0]
        self.assertTrue(isclass(fromSto1B))
        self.assertTrue(issubclass(fromSto1B, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1B.by_rules), 2)
        self.assertEqual(fromSto1B.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1B.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromSto1B.end_rule.rule, ([B], [1, B]))
        class RuleNewStoAB(Rule): rule = ([S], [A, B])
        self.assertIn(RuleNewStoAB, com.rules)
        fromStoAB = list(filter(lambda x: hash(x) == hash(RuleNewStoAB), com.rules))[0]
        self.assertTrue(isclass(fromStoAB))
        self.assertTrue(issubclass(fromStoAB, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromStoAB.by_rules), 2)
        self.assertEqual(fromStoAB.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromStoAB.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromStoAB.end_rule.rule, ([B], [A, B]))
        class RuleNewStoEPS(Rule): rule = ([S], [EPS])
        self.assertIn(RuleNewStoEPS, com.rules)
        fromStoEPS = list(filter(lambda x: hash(x) == hash(RuleNewStoEPS), com.rules))[0]
        self.assertTrue(isclass(fromStoEPS))
        self.assertTrue(issubclass(fromStoEPS, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromStoEPS.by_rules), 2)
        self.assertEqual(fromStoEPS.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromStoEPS.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromStoEPS.end_rule.rule, ([B], [EPS]))
        class RuleNewSto1A(Rule): rule = ([S], [1, A])
        self.assertIn(RuleNewSto1A, com.rules)
        fromSto1A = list(filter(lambda x: hash(x) == hash(RuleNewSto1A), com.rules))[0]
        self.assertTrue(isclass(fromSto1A))
        self.assertTrue(issubclass(fromSto1A, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1A.by_rules), 3)
        self.assertEqual(fromSto1A.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1A.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromSto1A.by_rules[2].rule, ([B], [C]))
        self.assertEqual(fromSto1A.end_rule.rule, ([C], [1, A]))
        class RuleNewSto1(Rule): rule = ([S], [1])
        self.assertIn(RuleNewSto1, com.rules)
        fromSto1 = list(filter(lambda x: hash(x) == hash(RuleNewSto1), com.rules))[0]
        self.assertTrue(isclass(fromSto1))
        self.assertTrue(issubclass(fromSto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1.by_rules), 3)
        self.assertEqual(fromSto1.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromSto1.by_rules[2].rule, ([B], [C]))
        self.assertEqual(fromSto1.end_rule.rule, ([C], [1]))
        class RuleNewAto1B(Rule): rule = ([A], [1, B])
        self.assertIn(RuleNewAto1B, com.rules)
        fromAto1B = list(filter(lambda x: hash(x) == hash(RuleNewAto1B), com.rules))[0]
        self.assertTrue(isclass(fromAto1B))
        self.assertTrue(issubclass(fromAto1B, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto1B.by_rules), 1)
        self.assertEqual(fromAto1B.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAto1B.end_rule.rule, ([B], [1, B]))
        class RuleNewAtoAB(Rule): rule = ([A], [A, B])
        self.assertIn(RuleNewAtoAB, com.rules)
        fromAtoAB = list(filter(lambda x: hash(x) == hash(RuleNewAtoAB), com.rules))[0]
        self.assertTrue(isclass(fromAtoAB))
        self.assertTrue(issubclass(fromAtoAB, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAtoAB.by_rules), 1)
        self.assertEqual(fromAtoAB.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAtoAB.end_rule.rule, ([B], [A, B]))
        class RuleNewAtoEPS(Rule): rule = ([A], [EPS])
        self.assertIn(RuleNewAtoEPS, com.rules)
        fromAtoEPS = list(filter(lambda x: hash(x) == hash(RuleNewAtoEPS), com.rules))[0]
        self.assertTrue(isclass(fromAtoEPS))
        self.assertTrue(issubclass(fromAtoEPS, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAtoEPS.by_rules), 1)
        self.assertEqual(fromAtoEPS.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAtoEPS.end_rule.rule, ([B], [EPS]))
        class RuleNewAto1A(Rule): rule = ([A], [1, A])
        self.assertIn(RuleNewAto1A, com.rules)
        fromAto1A = list(filter(lambda x: hash(x) == hash(RuleNewAto1A), com.rules))[0]
        self.assertTrue(isclass(fromAto1A))
        self.assertTrue(issubclass(fromAto1A, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto1A.by_rules), 2)
        self.assertEqual(fromAto1A.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAto1A.by_rules[1].rule, ([B], [C]))
        self.assertEqual(fromAto1A.end_rule.rule, ([C], [1, A]))
        class RuleNewAto1(Rule): rule = ([A], [1])
        self.assertIn(RuleNewAto1, com.rules)
        fromAto1 = list(filter(lambda x: hash(x) == hash(RuleNewAto1), com.rules))[0]
        self.assertTrue(isclass(fromAto1))
        self.assertTrue(issubclass(fromAto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto1.by_rules), 2)
        self.assertEqual(fromAto1.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAto1.by_rules[1].rule, ([B], [C]))
        self.assertEqual(fromAto1.end_rule.rule, ([C], [1]))
        class RuleNewBto1A(Rule): rule = ([B], [1, A])
        self.assertIn(RuleNewBto1A, com.rules)
        fromBto1A = list(filter(lambda x: hash(x) == hash(RuleNewBto1A), com.rules))[0]
        self.assertTrue(isclass(fromBto1A))
        self.assertTrue(issubclass(fromBto1A, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto1A.by_rules), 1)
        self.assertEqual(fromBto1A.by_rules[0].rule, ([B], [C]))
        self.assertEqual(fromBto1A.end_rule.rule, ([C], [1, A]))
        class RuleNewBto1(Rule): rule = ([B], [1])
        self.assertIn(RuleNewBto1, com.rules)
        fromBto1 = list(filter(lambda x: hash(x) == hash(RuleNewBto1), com.rules))[0]
        self.assertTrue(isclass(fromBto1))
        self.assertTrue(issubclass(fromBto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto1.by_rules), 1)
        self.assertEqual(fromBto1.by_rules[0].rule, ([B], [C]))
        self.assertEqual(fromBto1.end_rule.rule, ([C], [1]))

    def test_simpleTestShouldNotChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B, C],
                    rules=[Rules],
                    start_symbol=S)
        ContextFree.remove_unit_rules(g)
        # Removed
        class RuleStoA(Rule): rule=([S], [A])
        self.assertIn(RuleStoA, g.rules)
        class RuleAtoB(Rule): rule=([A], [B])
        self.assertIn(RuleAtoB, g.rules)
        class RuleBtoC(Rule): rule=([B], [C])
        self.assertIn(RuleBtoC, g.rules)
        # Old rules
        class RuleNewSto0B0(Rule): rule = ([S], [0, B, 0])
        self.assertIn(RuleNewSto0B0, g.rules)
        class RuleNewAto0A(Rule): rule = ([A], [0, A])
        self.assertIn(RuleNewAto0A, g.rules)
        class RuleNewBto1B(Rule): rule = ([B], [1, B])
        self.assertIn(RuleNewBto1B, g.rules)
        class RuleNewBtoAB(Rule): rule = ([B], [A, B])
        self.assertIn(RuleNewBtoAB, g.rules)
        class RuleNewBtoEPS(Rule): rule = ([B], [EPS])
        self.assertIn(RuleNewBtoEPS, g.rules)
        class RuleNewCto1A(Rule): rule = ([C], [1, A])
        self.assertIn(RuleNewCto1A, g.rules)
        class RuleNewCto1(Rule): rule = ([C], [1])
        self.assertIn(RuleNewCto1, g.rules)
        # New rules
        class RuleNewSto0A(Rule): rule = ([S], [0, A])
        self.assertNotIn(RuleNewSto0A, g.rules)
        class RuleNewSto1B(Rule): rule = ([S], [1, B])
        self.assertNotIn(RuleNewSto1B, g.rules)
        class RuleNewStoAB(Rule): rule = ([S], [A, B])
        self.assertNotIn(RuleNewStoAB, g.rules)
        class RuleNewStoEPS(Rule): rule = ([S], [EPS])
        self.assertNotIn(RuleNewStoEPS, g.rules)
        class RuleNewSto1A(Rule): rule = ([S], [1, A])
        self.assertNotIn(RuleNewSto1A, g.rules)
        class RuleNewSto1(Rule): rule = ([S], [1])
        self.assertNotIn(RuleNewSto1, g.rules)
        class RuleNewAto1B(Rule): rule = ([A], [1, B])
        self.assertNotIn(RuleNewAto1B, g.rules)
        class RuleNewAtoAB(Rule): rule = ([A], [A, B])
        self.assertNotIn(RuleNewAtoAB, g.rules)
        class RuleNewAtoEPS(Rule): rule = ([A], [EPS])
        self.assertNotIn(RuleNewAtoEPS, g.rules)
        class RuleNewAto1A(Rule): rule = ([A], [1, A])
        self.assertNotIn(RuleNewAto1A, g.rules)
        class RuleNewAto1(Rule): rule = ([A], [1])
        self.assertNotIn(RuleNewAto1, g.rules)
        class RuleNewBto1A(Rule): rule = ([B], [1, A])
        self.assertNotIn(RuleNewBto1A, g.rules)
        class RuleNewBto1(Rule): rule = ([B], [1])
        self.assertNotIn(RuleNewBto1, g.rules)

    def test_simpleTestShouldChange(self):
        g = Grammar(terminals=[0, 1],
                    nonterminals=[S, A, B, C],
                    rules=[Rules],
                    start_symbol=S)
        ContextFree.remove_unit_rules(g, True)

        # Removed
        class RuleStoA(Rule): rule = ([S], [A])
        self.assertNotIn(RuleStoA, g.rules)
        class RuleAtoB(Rule): rule = ([A], [B])
        self.assertNotIn(RuleAtoB, g.rules)
        class RuleBtoC(Rule): rule = ([B], [C])
        self.assertNotIn(RuleBtoC, g.rules)
        # Old rules
        class RuleNewSto0B0(Rule): rule = ([S], [0, B, 0])
        self.assertIn(RuleNewSto0B0, g.rules)
        class RuleNewAto0A(Rule): rule = ([A], [0, A])
        self.assertIn(RuleNewAto0A, g.rules)
        class RuleNewBto1B(Rule): rule = ([B], [1, B])
        self.assertIn(RuleNewBto1B, g.rules)
        class RuleNewBtoAB(Rule): rule = ([B], [A, B])
        self.assertIn(RuleNewBtoAB, g.rules)
        class RuleNewBtoEPS(Rule): rule = ([B], [EPS])
        self.assertIn(RuleNewBtoEPS, g.rules)
        class RuleNewCto1A(Rule): rule = ([C], [1, A])
        self.assertIn(RuleNewCto1A, g.rules)
        class RuleNewCto1(Rule): rule = ([C], [1])
        self.assertIn(RuleNewCto1, g.rules)
        # New rules
        class RuleNewSto0A(Rule): rule = ([S], [0, A])
        self.assertIn(RuleNewSto0A, g.rules)
        fromSto0A = list(filter(lambda x: hash(x) == hash(RuleNewSto0A), g.rules))[0]
        self.assertTrue(isclass(fromSto0A))
        self.assertTrue(issubclass(fromSto0A, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto0A.by_rules), 1)
        self.assertEqual(fromSto0A.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto0A.end_rule.rule, ([A], [0, A]))
        class RuleNewSto1B(Rule): rule = ([S], [1, B])
        self.assertIn(RuleNewSto1B, g.rules)
        fromSto1B = list(filter(lambda x: hash(x) == hash(RuleNewSto1B), g.rules))[0]
        self.assertTrue(isclass(fromSto1B))
        self.assertTrue(issubclass(fromSto1B, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1B.by_rules), 2)
        self.assertEqual(fromSto1B.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1B.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromSto1B.end_rule.rule, ([B], [1, B]))
        class RuleNewStoAB(Rule): rule = ([S], [A, B])
        self.assertIn(RuleNewStoAB, g.rules)
        fromStoAB = list(filter(lambda x: hash(x) == hash(RuleNewStoAB), g.rules))[0]
        self.assertTrue(isclass(fromStoAB))
        self.assertTrue(issubclass(fromStoAB, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromStoAB.by_rules), 2)
        self.assertEqual(fromStoAB.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromStoAB.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromStoAB.end_rule.rule, ([B], [A, B]))
        class RuleNewStoEPS(Rule): rule = ([S], [EPS])
        self.assertIn(RuleNewStoEPS, g.rules)
        fromStoEPS = list(filter(lambda x: hash(x) == hash(RuleNewStoEPS), g.rules))[0]
        self.assertTrue(isclass(fromStoEPS))
        self.assertTrue(issubclass(fromStoEPS, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromStoEPS.by_rules), 2)
        self.assertEqual(fromStoEPS.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromStoEPS.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromStoEPS.end_rule.rule, ([B], [EPS]))
        class RuleNewSto1A(Rule): rule = ([S], [1, A])
        self.assertIn(RuleNewSto1A, g.rules)
        fromSto1A = list(filter(lambda x: hash(x) == hash(RuleNewSto1A), g.rules))[0]
        self.assertTrue(isclass(fromSto1A))
        self.assertTrue(issubclass(fromSto1A, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1A.by_rules), 3)
        self.assertEqual(fromSto1A.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1A.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromSto1A.by_rules[2].rule, ([B], [C]))
        self.assertEqual(fromSto1A.end_rule.rule, ([C], [1, A]))
        class RuleNewSto1(Rule): rule = ([S], [1])
        self.assertIn(RuleNewSto1, g.rules)
        fromSto1 = list(filter(lambda x: hash(x) == hash(RuleNewSto1), g.rules))[0]
        self.assertTrue(isclass(fromSto1))
        self.assertTrue(issubclass(fromSto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1.by_rules), 3)
        self.assertEqual(fromSto1.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromSto1.by_rules[2].rule, ([B], [C]))
        self.assertEqual(fromSto1.end_rule.rule, ([C], [1]))
        class RuleNewAto1B(Rule): rule = ([A], [1, B])
        self.assertIn(RuleNewAto1B, g.rules)
        fromAto1B = list(filter(lambda x: hash(x) == hash(RuleNewAto1B), g.rules))[0]
        self.assertTrue(isclass(fromAto1B))
        self.assertTrue(issubclass(fromAto1B, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto1B.by_rules), 1)
        self.assertEqual(fromAto1B.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAto1B.end_rule.rule, ([B], [1, B]))
        class RuleNewAtoAB(Rule): rule = ([A], [A, B])
        self.assertIn(RuleNewAtoAB, g.rules)
        fromAtoAB = list(filter(lambda x: hash(x) == hash(RuleNewAtoAB), g.rules))[0]
        self.assertTrue(isclass(fromAtoAB))
        self.assertTrue(issubclass(fromAtoAB, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAtoAB.by_rules), 1)
        self.assertEqual(fromAtoAB.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAtoAB.end_rule.rule, ([B], [A, B]))
        class RuleNewAtoEPS(Rule): rule = ([A], [EPS])
        self.assertIn(RuleNewAtoEPS, g.rules)
        fromAtoEPS = list(filter(lambda x: hash(x) == hash(RuleNewAtoEPS), g.rules))[0]
        self.assertTrue(isclass(fromAtoEPS))
        self.assertTrue(issubclass(fromAtoEPS, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAtoEPS.by_rules), 1)
        self.assertEqual(fromAtoEPS.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAtoEPS.end_rule.rule, ([B], [EPS]))
        class RuleNewAto1A(Rule): rule = ([A], [1, A])
        self.assertIn(RuleNewAto1A, g.rules)
        fromAto1A = list(filter(lambda x: hash(x) == hash(RuleNewAto1A), g.rules))[0]
        self.assertTrue(isclass(fromAto1A))
        self.assertTrue(issubclass(fromAto1A, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto1A.by_rules), 2)
        self.assertEqual(fromAto1A.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAto1A.by_rules[1].rule, ([B], [C]))
        self.assertEqual(fromAto1A.end_rule.rule, ([C], [1, A]))
        class RuleNewAto1(Rule): rule = ([A], [1])
        self.assertIn(RuleNewAto1, g.rules)
        fromAto1 = list(filter(lambda x: hash(x) == hash(RuleNewAto1), g.rules))[0]
        self.assertTrue(isclass(fromAto1))
        self.assertTrue(issubclass(fromAto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto1.by_rules), 2)
        self.assertEqual(fromAto1.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAto1.by_rules[1].rule, ([B], [C]))
        self.assertEqual(fromAto1.end_rule.rule, ([C], [1]))
        class RuleNewBto1A(Rule): rule = ([B], [1, A])
        self.assertIn(RuleNewBto1A, g.rules)
        fromBto1A = list(filter(lambda x: hash(x) == hash(RuleNewBto1A), g.rules))[0]
        self.assertTrue(isclass(fromBto1A))
        self.assertTrue(issubclass(fromBto1A, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto1A.by_rules), 1)
        self.assertEqual(fromBto1A.by_rules[0].rule, ([B], [C]))
        self.assertEqual(fromBto1A.end_rule.rule, ([C], [1, A]))
        class RuleNewBto1(Rule): rule = ([B], [1])
        self.assertIn(RuleNewBto1, g.rules)
        fromBto1 = list(filter(lambda x: hash(x) == hash(RuleNewBto1), g.rules))[0]
        self.assertTrue(isclass(fromBto1))
        self.assertTrue(issubclass(fromBto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto1.by_rules), 1)
        self.assertEqual(fromBto1.by_rules[0].rule, ([B], [C]))
        self.assertEqual(fromBto1.end_rule.rule, ([C], [1]))


if __name__ == '__main__':
    main()
