#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 22.08.2017 20:51
:Licence MIT
Part of grammpy-transforms

"""
from inspect import isclass
from unittest import main, TestCase
from grammpy import *
from grammpy.transforms import ContextFree


class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass
class Rules(Rule):
    rules=[
        ([S], [A]),
        ([S], [B]),
        ([A], [C]),
        ([A], [0, A]),
        ([A], [1, S]),
        ([B], [D]),
        ([B], [2, B]),
        ([B], [3, S]),
        ([C], [1, C]),
        ([C], [0]),
        ([D], [3, D]),
        ([D], [2])]


"""
 -------------------------------
 |  S  |  A  |  B  |  C  |  D  |
--------------------------------
S| []  | [1] | [2] |[1,3]|[2,6]|
--------------------------------
A|     | []  |     | [3] |     |
--------------------------------
B|     |     | []  |     | [6] |
--------------------------------
C|     |     |     | []  |     |
--------------------------------
D|     |     |     |     | []  |
--------------------------------

S->A  S->B  A->C  A->0A  A->1S  B->D  B->2B  B->3S  C->1C  C->0  D->3D  D->2
----  ----  ----                ----                         

S->A->0A
S->A->1S
S->A->C->1C
S->A->C->0
S->B->2B
S->B->3S
S->B->D->3D
S->B->D->2
A->C->1C
A->C->0
B->D->3D
B->D->2
"""


class SimpleTest(TestCase):
    def test_simpleTest(self):
        g = Grammar(terminals=[0, 1, 2, 3],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        com = ContextFree.remove_unit_rules(g)
        # Removed
        class RuleStoA(Rule): rule=([S], [A])
        self.assertNotIn(RuleStoA, com.rules)
        class RuleStoB(Rule): rule=([S], [B])
        self.assertNotIn(RuleStoB, com.rules)
        class RuleAtoC(Rule): rule=([A], [C])
        self.assertNotIn(RuleAtoC, com.rules)
        class RuleBtoD(Rule): rule=([B], [D])
        self.assertNotIn(RuleBtoD, com.rules)
        # Old rules
        class RuleNewAto0A(Rule): rule = ([A], [0, A])
        self.assertIn(RuleNewAto0A, com.rules)
        class RuleNewAto1S(Rule): rule = ([A], [1, S])
        self.assertIn(RuleNewAto1S, com.rules)
        class RuleNewBto2B(Rule): rule = ([B], [2, B])
        self.assertIn(RuleNewBto2B, com.rules)
        class RuleNewBto3S(Rule): rule = ([B], [3, S])
        self.assertIn(RuleNewBto3S, com.rules)
        class RuleNewCto1C(Rule): rule = ([C], [1, C])
        self.assertIn(RuleNewCto1C, com.rules)
        class RuleNewCto0(Rule): rule = ([C], [0])
        self.assertIn(RuleNewCto0, com.rules)
        class RuleNewDto3D(Rule): rule = ([D], [3, D])
        self.assertIn(RuleNewDto3D, com.rules)
        class RuleNewDto2(Rule): rule = ([D], [2])
        self.assertIn(RuleNewDto2, com.rules)
        # New rules
        class RuleNewSto0A(Rule): rule = ([S], [0, A])
        self.assertIn(RuleNewSto0A, com.rules)
        fromSto0A = list(filter(lambda x: hash(x) == hash(RuleNewSto0A), com.rules))[0]
        self.assertTrue(isclass(fromSto0A))
        self.assertTrue(issubclass(fromSto0A, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto0A.by_rules), 1)
        self.assertEqual(fromSto0A.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto0A.end_rule.rule, ([A], [0, A]))
        class RuleNewSto1S(Rule): rule = ([S], [1, S])
        self.assertIn(RuleNewSto1S, com.rules)
        fromSto1S = list(filter(lambda x: hash(x) == hash(RuleNewSto1S), com.rules))[0]
        self.assertTrue(isclass(fromSto1S))
        self.assertTrue(issubclass(fromSto1S, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1S.by_rules), 1)
        self.assertEqual(fromSto1S.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1S.end_rule.rule, ([A], [1, S]))
        class RuleNewSto1C(Rule): rule = ([S], [1, C])
        self.assertIn(RuleNewSto1C, com.rules)
        fromSto1C = list(filter(lambda x: hash(x) == hash(RuleNewSto1C), com.rules))[0]
        self.assertTrue(isclass(fromSto1C))
        self.assertTrue(issubclass(fromSto1C, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1C.by_rules), 2)
        self.assertEqual(fromSto1C.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1C.by_rules[1].rule, ([A], [C]))
        self.assertEqual(fromSto1C.end_rule.rule, ([C], [1, C]))
        class RuleNewSto0(Rule): rule = ([S], [0])
        self.assertIn(RuleNewSto0, com.rules)
        fromSto0 = list(filter(lambda x: hash(x) == hash(RuleNewSto0), com.rules))[0]
        self.assertTrue(isclass(fromSto0))
        self.assertTrue(issubclass(fromSto0, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto0.by_rules), 2)
        self.assertEqual(fromSto0.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto0.by_rules[1].rule, ([A], [C]))
        self.assertEqual(fromSto0.end_rule.rule, ([C], [0]))
        class RuleNewSto2B(Rule): rule = ([S], [2, B])
        self.assertIn(RuleNewSto2B, com.rules)
        fromSto2B = list(filter(lambda x: hash(x) == hash(RuleNewSto2B), com.rules))[0]
        self.assertTrue(isclass(fromSto2B))
        self.assertTrue(issubclass(fromSto2B, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto2B.by_rules), 1)
        self.assertEqual(fromSto2B.by_rules[0].rule, ([S], [B]))
        self.assertEqual(fromSto2B.end_rule.rule, ([B], [2, B]))
        class RuleNewSto3S(Rule): rule = ([S], [3, S])
        self.assertIn(RuleNewSto3S, com.rules)
        fromSto3S = list(filter(lambda x: hash(x) == hash(RuleNewSto3S), com.rules))[0]
        self.assertTrue(isclass(fromSto3S))
        self.assertTrue(issubclass(fromSto3S, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto3S.by_rules), 1)
        self.assertEqual(fromSto3S.by_rules[0].rule, ([S], [B]))
        self.assertEqual(fromSto3S.end_rule.rule, ([B], [3, S]))
        class RuleNewSto3D(Rule): rule = ([S], [3, D])
        self.assertIn(RuleNewSto3D, com.rules)
        fromSto3D = list(filter(lambda x: hash(x) == hash(RuleNewSto3D), com.rules))[0]
        self.assertTrue(isclass(fromSto3D))
        self.assertTrue(issubclass(fromSto3D, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto3D.by_rules), 2)
        self.assertEqual(fromSto3D.by_rules[0].rule, ([S], [B]))
        self.assertEqual(fromSto3D.by_rules[1].rule, ([B], [D]))
        self.assertEqual(fromSto3D.end_rule.rule, ([D], [3, D]))
        class RuleNewSto2(Rule): rule = ([S], [2])
        self.assertIn(RuleNewSto2, com.rules)
        fromSto2 = list(filter(lambda x: hash(x) == hash(RuleNewSto2), com.rules))[0]
        self.assertTrue(isclass(fromSto2))
        self.assertTrue(issubclass(fromSto2, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto2.by_rules), 2)
        self.assertEqual(fromSto2.by_rules[0].rule, ([S], [B]))
        self.assertEqual(fromSto2.by_rules[1].rule, ([B], [D]))
        self.assertEqual(fromSto2.end_rule.rule, ([D], [2]))
        class RuleNewAto1C(Rule): rule = ([A], [1, C])
        self.assertIn(RuleNewAto1C, com.rules)
        fromAto1C = list(filter(lambda x: hash(x) == hash(RuleNewAto1C), com.rules))[0]
        self.assertTrue(isclass(fromAto1C))
        self.assertTrue(issubclass(fromAto1C, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto1C.by_rules), 1)
        self.assertEqual(fromAto1C.by_rules[0].rule, ([A], [C]))
        self.assertEqual(fromAto1C.end_rule.rule, ([C], [1, C]))
        class RuleNewAto0(Rule): rule = ([A], [0])
        self.assertIn(RuleNewAto0, com.rules)
        fromAto0 = list(filter(lambda x: hash(x) == hash(RuleNewAto0), com.rules))[0]
        self.assertTrue(isclass(fromAto0))
        self.assertTrue(issubclass(fromAto0, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto0.by_rules), 1)
        self.assertEqual(fromAto0.by_rules[0].rule, ([A], [C]))
        self.assertEqual(fromAto0.end_rule.rule, ([C], [0]))
        class RuleNewBto3D(Rule): rule = ([B], [3, D])
        self.assertIn(RuleNewBto3D, com.rules)
        fromBto3D = list(filter(lambda x: hash(x) == hash(RuleNewBto3D), com.rules))[0]
        self.assertTrue(isclass(fromBto3D))
        self.assertTrue(issubclass(fromBto3D, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto3D.by_rules), 1)
        self.assertEqual(fromBto3D.by_rules[0].rule, ([B], [D]))
        self.assertEqual(fromBto3D.end_rule.rule, ([D], [3, D]))
        class RuleNewBto2(Rule): rule = ([B], [2])
        self.assertIn(RuleNewBto2, com.rules)
        fromBto2 = list(filter(lambda x: hash(x) == hash(RuleNewBto2), com.rules))[0]
        self.assertTrue(isclass(fromBto2))
        self.assertTrue(issubclass(fromBto2, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto2.by_rules), 1)
        self.assertEqual(fromBto2.by_rules[0].rule, ([B], [D]))
        self.assertEqual(fromBto2.end_rule.rule, ([D], [2]))

    def test_simpleTestShouldNotChange(self):
        g = Grammar(terminals=[0,1,2,3],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        ContextFree.remove_unit_rules(g)
        # Removed
        class RuleStoA(Rule): rule = ([S], [A])
        self.assertIn(RuleStoA, g.rules)
        class RuleStoB(Rule): rule = ([S], [B])
        self.assertIn(RuleStoB, g.rules)
        class RuleAtoC(Rule): rule = ([A], [C])
        self.assertIn(RuleAtoC, g.rules)
        class RuleBtoD(Rule): rule = ([B], [D])
        self.assertIn(RuleBtoD, g.rules)
        # Old rules
        class RuleNewAto0A(Rule): rule = ([A], [0, A])
        self.assertIn(RuleNewAto0A, g.rules)
        class RuleNewAto1S(Rule): rule = ([A], [1, S])
        self.assertIn(RuleNewAto1S, g.rules)
        class RuleNewBto2B(Rule): rule = ([B], [2, B])
        self.assertIn(RuleNewBto2B, g.rules)
        class RuleNewBto3S(Rule): rule = ([B], [3, S])
        self.assertIn(RuleNewBto3S, g.rules)
        class RuleNewCto1C(Rule): rule = ([C], [1, C])
        self.assertIn(RuleNewCto1C, g.rules)
        class RuleNewCto0(Rule): rule = ([C], [0])
        self.assertIn(RuleNewCto0, g.rules)
        class RuleNewDto3D(Rule): rule = ([D], [3, D])
        self.assertIn(RuleNewDto3D, g.rules)
        class RuleNewDto2(Rule): rule = ([D], [2])
        self.assertIn(RuleNewDto2, g.rules)
        # New rules
        class RuleNewSto0A(Rule): rule = ([S], [0, A])
        self.assertNotIn(RuleNewSto0A, g.rules)
        class RuleNewSto1S(Rule): rule = ([S], [1, S])
        self.assertNotIn(RuleNewSto1S, g.rules)
        class RuleNewSto1C(Rule): rule = ([S], [1, C])
        self.assertNotIn(RuleNewSto1C, g.rules)
        class RuleNewSto0(Rule): rule = ([S], [0])
        self.assertNotIn(RuleNewSto0, g.rules)
        class RuleNewSto2B(Rule): rule = ([S], [2, B])
        self.assertNotIn(RuleNewSto2B, g.rules)
        class RuleNewSto3S(Rule): rule = ([S], [3, S])
        self.assertNotIn(RuleNewSto3S, g.rules)
        class RuleNewSto3D(Rule): rule = ([S], [3, D])
        self.assertNotIn(RuleNewSto3D, g.rules)
        class RuleNewSto2(Rule): rule = ([S], [2])
        self.assertNotIn(RuleNewSto2, g.rules)
        class RuleNewAto1C(Rule): rule = ([A], [1, C])
        self.assertNotIn(RuleNewAto1C, g.rules)
        class RuleNewAto0(Rule): rule = ([A], [0])
        self.assertNotIn(RuleNewAto0, g.rules)
        class RuleNewBto3D(Rule): rule = ([B], [3, D])
        self.assertNotIn(RuleNewBto3D, g.rules)
        class RuleNewBto2(Rule): rule = ([B], [2])
        self.assertNotIn(RuleNewBto2, g.rules)

    def test_simpleTestShouldChange(self):
        g = Grammar(terminals=[0,1,2,3],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        ContextFree.remove_unit_rules(g, True)
        # Removed
        class RuleStoA(Rule): rule = ([S], [A])
        self.assertNotIn(RuleStoA, g.rules)
        class RuleStoB(Rule): rule = ([S], [B])
        self.assertNotIn(RuleStoB, g.rules)
        class RuleAtoC(Rule): rule = ([A], [C])
        self.assertNotIn(RuleAtoC, g.rules)
        class RuleBtoD(Rule): rule = ([B], [D])
        self.assertNotIn(RuleBtoD, g.rules)
        # Old rules
        class RuleNewAto0A(Rule): rule = ([A], [0, A])
        self.assertIn(RuleNewAto0A, g.rules)
        class RuleNewAto1S(Rule): rule = ([A], [1, S])
        self.assertIn(RuleNewAto1S, g.rules)
        class RuleNewBto2B(Rule): rule = ([B], [2, B])
        self.assertIn(RuleNewBto2B, g.rules)
        class RuleNewBto3S(Rule): rule = ([B], [3, S])
        self.assertIn(RuleNewBto3S, g.rules)
        class RuleNewCto1C(Rule): rule = ([C], [1, C])
        self.assertIn(RuleNewCto1C, g.rules)
        class RuleNewCto0(Rule): rule = ([C], [0])
        self.assertIn(RuleNewCto0, g.rules)
        class RuleNewDto3D(Rule): rule = ([D], [3, D])
        self.assertIn(RuleNewDto3D, g.rules)
        class RuleNewDto2(Rule): rule = ([D], [2])
        self.assertIn(RuleNewDto2, g.rules)
        # New rules
        class RuleNewSto0A(Rule): rule = ([S], [0, A])
        self.assertIn(RuleNewSto0A, g.rules)
        fromSto0A = list(filter(lambda x: hash(x) == hash(RuleNewSto0A), g.rules))[0]
        self.assertTrue(isclass(fromSto0A))
        self.assertTrue(issubclass(fromSto0A, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto0A.by_rules), 1)
        self.assertEqual(fromSto0A.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto0A.end_rule.rule, ([A], [0, A]))

        class RuleNewSto1S(Rule): rule = ([S], [1, S])
        self.assertIn(RuleNewSto1S, g.rules)
        fromSto1S = list(filter(lambda x: hash(x) == hash(RuleNewSto1S), g.rules))[0]
        self.assertTrue(isclass(fromSto1S))
        self.assertTrue(issubclass(fromSto1S, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1S.by_rules), 1)
        self.assertEqual(fromSto1S.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1S.end_rule.rule, ([A], [1, S]))
        class RuleNewSto1C(Rule): rule = ([S], [1, C])
        self.assertIn(RuleNewSto1C, g.rules)
        fromSto1C = list(filter(lambda x: hash(x) == hash(RuleNewSto1C), g.rules))[0]
        self.assertTrue(isclass(fromSto1C))
        self.assertTrue(issubclass(fromSto1C, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto1C.by_rules), 2)
        self.assertEqual(fromSto1C.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto1C.by_rules[1].rule, ([A], [C]))
        self.assertEqual(fromSto1C.end_rule.rule, ([C], [1, C]))
        class RuleNewSto0(Rule): rule = ([S], [0])
        self.assertIn(RuleNewSto0, g.rules)
        fromSto0 = list(filter(lambda x: hash(x) == hash(RuleNewSto0), g.rules))[0]
        self.assertTrue(isclass(fromSto0))
        self.assertTrue(issubclass(fromSto0, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto0.by_rules), 2)
        self.assertEqual(fromSto0.by_rules[0].rule, ([S], [A]))
        self.assertEqual(fromSto0.by_rules[1].rule, ([A], [C]))
        self.assertEqual(fromSto0.end_rule.rule, ([C], [0]))
        class RuleNewSto2B(Rule): rule = ([S], [2, B])
        self.assertIn(RuleNewSto2B, g.rules)
        fromSto2B = list(filter(lambda x: hash(x) == hash(RuleNewSto2B), g.rules))[0]
        self.assertTrue(isclass(fromSto2B))
        self.assertTrue(issubclass(fromSto2B, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto2B.by_rules), 1)
        self.assertEqual(fromSto2B.by_rules[0].rule, ([S], [B]))
        self.assertEqual(fromSto2B.end_rule.rule, ([B], [2, B]))
        class RuleNewSto3S(Rule): rule = ([S], [3, S])
        self.assertIn(RuleNewSto3S, g.rules)
        fromSto3S = list(filter(lambda x: hash(x) == hash(RuleNewSto3S), g.rules))[0]
        self.assertTrue(isclass(fromSto3S))
        self.assertTrue(issubclass(fromSto3S, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto3S.by_rules), 1)
        self.assertEqual(fromSto3S.by_rules[0].rule, ([S], [B]))
        self.assertEqual(fromSto3S.end_rule.rule, ([B], [3, S]))
        class RuleNewSto3D(Rule): rule = ([S], [3, D])
        self.assertIn(RuleNewSto3D, g.rules)
        fromSto3D = list(filter(lambda x: hash(x) == hash(RuleNewSto3D), g.rules))[0]
        self.assertTrue(isclass(fromSto3D))
        self.assertTrue(issubclass(fromSto3D, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto3D.by_rules), 2)
        self.assertEqual(fromSto3D.by_rules[0].rule, ([S], [B]))
        self.assertEqual(fromSto3D.by_rules[1].rule, ([B], [D]))
        self.assertEqual(fromSto3D.end_rule.rule, ([D], [3, D]))
        class RuleNewSto2(Rule): rule = ([S], [2])
        self.assertIn(RuleNewSto2, g.rules)
        fromSto2 = list(filter(lambda x: hash(x) == hash(RuleNewSto2), g.rules))[0]
        self.assertTrue(isclass(fromSto2))
        self.assertTrue(issubclass(fromSto2, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromSto2.by_rules), 2)
        self.assertEqual(fromSto2.by_rules[0].rule, ([S], [B]))
        self.assertEqual(fromSto2.by_rules[1].rule, ([B], [D]))
        self.assertEqual(fromSto2.end_rule.rule, ([D], [2]))
        class RuleNewAto1C(Rule): rule = ([A], [1, C])
        self.assertIn(RuleNewAto1C, g.rules)
        fromAto1C = list(filter(lambda x: hash(x) == hash(RuleNewAto1C), g.rules))[0]
        self.assertTrue(isclass(fromAto1C))
        self.assertTrue(issubclass(fromAto1C, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto1C.by_rules), 1)
        self.assertEqual(fromAto1C.by_rules[0].rule, ([A], [C]))
        self.assertEqual(fromAto1C.end_rule.rule, ([C], [1, C]))
        class RuleNewAto0(Rule): rule = ([A], [0])
        self.assertIn(RuleNewAto0, g.rules)
        fromAto0 = list(filter(lambda x: hash(x) == hash(RuleNewAto0), g.rules))[0]
        self.assertTrue(isclass(fromAto0))
        self.assertTrue(issubclass(fromAto0, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromAto0.by_rules), 1)
        self.assertEqual(fromAto0.by_rules[0].rule, ([A], [C]))
        self.assertEqual(fromAto0.end_rule.rule, ([C], [0]))
        class RuleNewBto3D(Rule): rule = ([B], [3, D])
        self.assertIn(RuleNewBto3D, g.rules)
        fromBto3D = list(filter(lambda x: hash(x) == hash(RuleNewBto3D), g.rules))[0]
        self.assertTrue(isclass(fromBto3D))
        self.assertTrue(issubclass(fromBto3D, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto3D.by_rules), 1)
        self.assertEqual(fromBto3D.by_rules[0].rule, ([B], [D]))
        self.assertEqual(fromBto3D.end_rule.rule, ([D], [3, D]))
        class RuleNewBto2(Rule): rule = ([B], [2])
        self.assertIn(RuleNewBto2, g.rules)
        fromBto2 = list(filter(lambda x: hash(x) == hash(RuleNewBto2), g.rules))[0]
        self.assertTrue(isclass(fromBto2))
        self.assertTrue(issubclass(fromBto2, ContextFree.ReducedUnitRule))
        self.assertEqual(len(fromBto2.by_rules), 1)
        self.assertEqual(fromBto2.by_rules[0].rule, ([B], [D]))
        self.assertEqual(fromBto2.end_rule.rule, ([D], [2]))


if __name__ == '__main__':
    main()
