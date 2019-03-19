#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 22.08.2017 21:28
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
        ([S], [A]),
        ([A], [B]),
        ([B], [C]),
        ([C], [A]),
        ([A], [0]),
        ([B], [1]),
        ([C], [2])]


"""
 ---------------------------------
 |   S   |   A   |   B   |   C   |
----------------------------------
S|  []   |  [1]  | [1,2] |[1,2,3]|
----------------------------------
A|       |  []   |  [2]  | [2,3] |
----------------------------------
B|       | [3,4] |  []   |  [3]  |
----------------------------------
C|       |  [4]  | [4,2] |  []   |
----------------------------------

S->A  A->B  B->C  C->A  A->0  B->1  C->2
----  ----  ----  ----

S->A->0
S->A->B->1
S->A->B->C->2
A->B->1
A->B->C->2
B->C->2
B->C->A->0
C->A->0
C->A->B->1
"""


class SimpleTest(TestCase):
    def test_simpleTest(self):
        g = Grammar(terminals=[0, 1, 2],
                    nonterminals=[S, A, B, C],
                    rules=[Rules],
                    start_symbol=S)
        com = ContextFree.remove_unit_rules(g)
        # Removed
        class RuleStoA(Rule): rule = ([S], [A])
        self.assertNotIn(RuleStoA, com.rules)
        class RuleAtoB(Rule): rule = ([A], [B])
        self.assertNotIn(RuleAtoB, com.rules)
        class RuleBtoC(Rule): rule = ([B], [C])
        self.assertNotIn(RuleBtoC, com.rules)
        class RuleCtoA(Rule): rule = ([C], [A])
        self.assertNotIn(RuleCtoA, com.rules)
        # Old rules
        class RuleNewAto0(Rule): rule = ([A], [0])
        self.assertIn(RuleNewAto0, com.rules)
        class RuleNewBto1(Rule): rule = ([B], [1])
        self.assertIn(RuleNewBto1, com.rules)
        class RuleNewCto2(Rule): rule = ([C], [2])
        self.assertIn(RuleNewCto2, com.rules)
        # New rules
        class RuleNewSto0(Rule): rule = ([S], [0])
        self.assertIn(RuleNewSto0, com.rules)
        fromSto0 = list(filter(lambda x: hash(x) == hash(RuleNewSto0), com.rules))[0]
        self.assertTrue(isclass(fromSto0))
        self.assertTrue(issubclass(fromSto0, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto0.by_rules), 1)
        self.assertEqual(fromSto0.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto0.end_rule.rule, ([A], [0]))
        class RuleNewSto1(Rule): rule = ([S], [1])
        self.assertIn(RuleNewSto1, com.rules)
        fromSto1 = list(filter(lambda x: hash(x) == hash(RuleNewSto1), com.rules))[0]
        self.assertTrue(isclass(fromSto1))
        self.assertTrue(issubclass(fromSto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1.by_rules), 2)
        self.assertEqual(fromSto1.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromSto1.end_rule.rule, ([B], [1]))
        class RuleNewSto2(Rule): rule = ([S], [2])
        self.assertIn(RuleNewSto2, com.rules)
        fromSto2 = list(filter(lambda x: hash(x) == hash(RuleNewSto2), com.rules))[0]
        self.assertTrue(isclass(fromSto2))
        self.assertTrue(issubclass(fromSto2, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto2.by_rules), 3)
        self.assertEqual(fromSto2.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto2.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromSto2.by_rules[2].rule, ([B], [C]))
        self.assertEqual(fromSto2.end_rule.rule, ([C], [2]))
        class RuleNewAto1(Rule): rule = ([A], [1])
        self.assertIn(RuleNewAto1, com.rules)
        fromAto1 = list(filter(lambda x: hash(x) == hash(RuleNewAto1), com.rules))[0]
        self.assertTrue(isclass(fromAto1))
        self.assertTrue(issubclass(fromAto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto1.by_rules), 1)
        self.assertEqual(fromAto1.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAto1.end_rule.rule, ([B], [1]))
        class RuleNewAto2(Rule): rule = ([A], [2])
        self.assertIn(RuleNewAto2, com.rules)
        fromAto2 = list(filter(lambda x: hash(x) == hash(RuleNewAto2), com.rules))[0]
        self.assertTrue(isclass(fromAto2))
        self.assertTrue(issubclass(fromAto2, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto2.by_rules), 2)
        self.assertEqual(fromAto2.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAto2.by_rules[1].rule, ([B], [C]))
        self.assertEqual(fromAto2.end_rule.rule, ([C], [2]))
        class RuleNewBto2(Rule): rule = ([B], [2])
        self.assertIn(RuleNewBto2, com.rules)
        fromBto2 = list(filter(lambda x: hash(x) == hash(RuleNewBto2), com.rules))[0]
        self.assertTrue(isclass(fromBto2))
        self.assertTrue(issubclass(fromBto2, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto2.by_rules), 1)
        self.assertEqual(fromBto2.by_rules[0].rule, ([B], [C]))
        self.assertEqual(fromBto2.end_rule.rule, ([C], [2]))
        class RuleNewBto0(Rule): rule = ([B], [0])
        self.assertIn(RuleNewBto0, com.rules)
        fromBto0 = list(filter(lambda x: hash(x) == hash(RuleNewBto0), com.rules))[0]
        self.assertTrue(isclass(fromBto0))
        self.assertTrue(issubclass(fromBto0, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto0.by_rules), 2)
        self.assertEqual(fromBto0.by_rules[0].rule, ([B], [C]))
        self.assertEqual(fromBto0.by_rules[1].rule, ([C], [A]))
        self.assertEqual(fromBto0.end_rule.rule, ([A], [0]))
        class RuleNewCto0(Rule): rule = ([C], [0])
        self.assertIn(RuleNewCto0, com.rules)
        fromCto0 = list(filter(lambda x: hash(x) == hash(RuleNewCto0), com.rules))[0]
        self.assertTrue(isclass(fromCto0))
        self.assertTrue(issubclass(fromCto0, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromCto0.by_rules), 1)
        self.assertEqual(fromCto0.by_rules[0].rule, ([C], [A]))
        self.assertEqual(fromCto0.end_rule.rule, ([A], [0]))
        class RuleNewCto1(Rule): rule = ([C], [1])
        self.assertIn(RuleNewCto1, com.rules)
        fromCto1 = list(filter(lambda x: hash(x) == hash(RuleNewCto1), com.rules))[0]
        self.assertTrue(isclass(fromCto1))
        self.assertTrue(issubclass(fromCto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromCto1.by_rules), 2)
        self.assertEqual(fromCto1.by_rules[0].rule, ([C], [A]))
        self.assertEqual(fromCto1.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromCto1.end_rule.rule, ([B], [1]))

    def test_simpleTestShouldNotChange(self):
        g = Grammar(terminals=[0, 1, 2],
                    nonterminals=[S, A, B, C],
                    rules=[Rules],
                    start_symbol=S)
        ContextFree.remove_unit_rules(g)
        # Removed
        class RuleStoA(Rule): rule = ([S], [A])
        self.assertIn(RuleStoA, g.rules)
        class RuleAtoB(Rule): rule = ([A], [B])
        self.assertIn(RuleAtoB, g.rules)
        class RuleBtoC(Rule): rule = ([B], [C])
        self.assertIn(RuleBtoC, g.rules)
        class RuleCtoA(Rule): rule = ([C], [A])
        self.assertIn(RuleCtoA, g.rules)
        # Old rules
        class RuleNewAto0(Rule): rule = ([A], [0])
        self.assertIn(RuleNewAto0, g.rules)
        class RuleNewBto1(Rule): rule = ([B], [1])
        self.assertIn(RuleNewBto1, g.rules)
        class RuleNewCto2(Rule): rule = ([C], [2])
        self.assertIn(RuleNewCto2, g.rules)
        # New rules
        class RuleNewSto0(Rule): rule = ([S], [0])
        self.assertNotIn(RuleNewSto0, g.rules)
        class RuleNewSto1(Rule): rule = ([S], [1])
        self.assertNotIn(RuleNewSto1, g.rules)
        class RuleNewSto2(Rule): rule = ([S], [2])
        self.assertNotIn(RuleNewSto2, g.rules)
        class RuleNewAto1(Rule): rule = ([A], [1])
        self.assertNotIn(RuleNewAto1, g.rules)
        class RuleNewAto2(Rule): rule = ([A], [2])
        self.assertNotIn(RuleNewAto2, g.rules)
        class RuleNewBto2(Rule): rule = ([B], [2])
        self.assertNotIn(RuleNewBto2, g.rules)
        class RuleNewBto0(Rule): rule = ([B], [0])
        self.assertNotIn(RuleNewBto0, g.rules)
        class RuleNewCto0(Rule): rule = ([C], [0])
        self.assertNotIn(RuleNewCto0, g.rules)
        class RuleNewCto1(Rule): rule = ([C], [1])
        self.assertNotIn(RuleNewCto1, g.rules)

    def test_simpleTestShouldChange(self):
        g = Grammar(terminals=[0, 1, 2],
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
        class RuleCtoA(Rule): rule = ([C], [A])
        self.assertNotIn(RuleCtoA, g.rules)
        # Old rules
        class RuleNewAto0(Rule): rule = ([A], [0])
        self.assertIn(RuleNewAto0, g.rules)
        class RuleNewBto1(Rule): rule = ([B], [1])
        self.assertIn(RuleNewBto1, g.rules)
        class RuleNewCto2(Rule): rule = ([C], [2])
        self.assertIn(RuleNewCto2, g.rules)
        # New rules
        class RuleNewSto0(Rule): rule = ([S], [0])
        self.assertIn(RuleNewSto0, g.rules)
        fromSto0 = list(filter(lambda x: hash(x) == hash(RuleNewSto0), g.rules))[0]
        self.assertTrue(isclass(fromSto0))
        self.assertTrue(issubclass(fromSto0, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto0.by_rules), 1)
        self.assertEqual(fromSto0.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto0.end_rule.rule, ([A], [0]))
        class RuleNewSto1(Rule): rule = ([S], [1])
        self.assertIn(RuleNewSto1, g.rules)
        fromSto1 = list(filter(lambda x: hash(x) == hash(RuleNewSto1), g.rules))[0]
        self.assertTrue(isclass(fromSto1))
        self.assertTrue(issubclass(fromSto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1.by_rules), 2)
        self.assertEqual(fromSto1.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromSto1.end_rule.rule, ([B], [1]))
        class RuleNewSto2(Rule): rule = ([S], [2])
        self.assertIn(RuleNewSto2, g.rules)
        fromSto2 = list(filter(lambda x: hash(x) == hash(RuleNewSto2), g.rules))[0]
        self.assertTrue(isclass(fromSto2))
        self.assertTrue(issubclass(fromSto2, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto2.by_rules), 3)
        self.assertEqual(fromSto2.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto2.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromSto2.by_rules[2].rule, ([B], [C]))
        self.assertEqual(fromSto2.end_rule.rule, ([C], [2]))
        class RuleNewAto1(Rule): rule = ([A], [1])
        self.assertIn(RuleNewAto1, g.rules)
        fromAto1 = list(filter(lambda x: hash(x) == hash(RuleNewAto1), g.rules))[0]
        self.assertTrue(isclass(fromAto1))
        self.assertTrue(issubclass(fromAto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto1.by_rules), 1)
        self.assertEqual(fromAto1.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAto1.end_rule.rule, ([B], [1]))
        class RuleNewAto2(Rule): rule = ([A], [2])
        self.assertIn(RuleNewAto2, g.rules)
        fromAto2 = list(filter(lambda x: hash(x) == hash(RuleNewAto2), g.rules))[0]
        self.assertTrue(isclass(fromAto2))
        self.assertTrue(issubclass(fromAto2, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto2.by_rules), 2)
        self.assertEqual(fromAto2.by_rules[0].rule, ([A], [B]))
        self.assertEqual(fromAto2.by_rules[1].rule, ([B], [C]))
        self.assertEqual(fromAto2.end_rule.rule, ([C], [2]))
        class RuleNewBto2(Rule): rule = ([B], [2])
        self.assertIn(RuleNewBto2, g.rules)
        fromBto2 = list(filter(lambda x: hash(x) == hash(RuleNewBto2), g.rules))[0]
        self.assertTrue(isclass(fromBto2))
        self.assertTrue(issubclass(fromBto2, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto2.by_rules), 1)
        self.assertEqual(fromBto2.by_rules[0].rule, ([B], [C]))
        self.assertEqual(fromBto2.end_rule.rule, ([C], [2]))
        class RuleNewBto0(Rule): rule = ([B], [0])
        self.assertIn(RuleNewBto0, g.rules)
        fromBto0 = list(filter(lambda x: hash(x) == hash(RuleNewBto0), g.rules))[0]
        self.assertTrue(isclass(fromBto0))
        self.assertTrue(issubclass(fromBto0, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto0.by_rules), 2)
        self.assertEqual(fromBto0.by_rules[0].rule, ([B], [C]))
        self.assertEqual(fromBto0.by_rules[1].rule, ([C], [A]))
        self.assertEqual(fromBto0.end_rule.rule, ([A], [0]))
        class RuleNewCto0(Rule): rule = ([C], [0])
        self.assertIn(RuleNewCto0, g.rules)
        fromCto0 = list(filter(lambda x: hash(x) == hash(RuleNewCto0), g.rules))[0]
        self.assertTrue(isclass(fromCto0))
        self.assertTrue(issubclass(fromCto0, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromCto0.by_rules), 1)
        self.assertEqual(fromCto0.by_rules[0].rule, ([C], [A]))
        self.assertEqual(fromCto0.end_rule.rule, ([A], [0]))
        class RuleNewCto1(Rule): rule = ([C], [1])
        self.assertIn(RuleNewCto1, g.rules)
        fromCto1 = list(filter(lambda x: hash(x) == hash(RuleNewCto1), g.rules))[0]
        self.assertTrue(isclass(fromCto1))
        self.assertTrue(issubclass(fromCto1, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromCto1.by_rules), 2)
        self.assertEqual(fromCto1.by_rules[0].rule, ([C], [A]))
        self.assertEqual(fromCto1.by_rules[1].rule, ([A], [B]))
        self.assertEqual(fromCto1.end_rule.rule, ([B], [1]))
        

if __name__ == '__main__':
    main()
