#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.08.2017 15:55
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
class D(Nonterminal): pass
class Rules(Rule):
    rules = [
        ([S], [A, 0, A]),
        ([S], [0]),
        ([A], [B, C]),
        ([A], [2]),
        ([A], [C, C, C]), # multiple here
        ([B], [1, C]),
        ([B], [3, D]),
        ([B], [EPS]),
        ([C], [A, A, 3]),
        ([C], [EPS]),
        ([D], [A, A, B]),
        ([D], [A, A, 3])]


"""
S->A0A  S->0    A->BC   A->2    A->CCC  B->1C   B->3D   B->eps  C->AA3  C->eps  D->AAB  D->AA3
ToEpsilon: A, B, C, D
S->A0A  S->0    A->BC   A->2    A->CCC  B->1C   B->3D   B->eps  C->AA3  C->eps  D->AAB  D->AA3
                                                        ------          ------
                                                        
S->0A           A->C            A->CC   B->1    B->3            C->A3           D->AB   D->A3
S->A0           A->B                                                            D->AA 

                                                                C->3            D->B    D->3
                                                                                D->A
"""


class MultipleUsageTest(TestCase):
    def test_multipleUsage(self):
        g = Grammar(terminals=[0, 1, 2, 3],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        com = ContextFree.remove_rules_with_epsilon(g)
        self.assertEqual(len(com.rules), 25)
        self.assertEqual(com.rules.size(), 25)
        class RuleNewSto0A(Rule): rule = ([S], [0, A])
        self.assertIn(RuleNewSto0A, com.rules)
        fromSto0A = list(filter(lambda x: hash(x) == hash(RuleNewSto0A), com.rules))[0]
        self.assertTrue(isclass(fromSto0A))
        self.assertTrue(issubclass(fromSto0A, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromSto0A.from_rule.rule, ([S], [A, 0, A]))
        self.assertEqual(fromSto0A.replace_index, 0)
        class RuleNewStoA0(Rule): rule = ([S], [A, 0])
        self.assertIn(RuleNewStoA0, com.rules)
        fromStoA0 = list(filter(lambda x: hash(x) == hash(RuleNewStoA0), com.rules))[0]
        self.assertTrue(isclass(fromStoA0))
        self.assertTrue(issubclass(fromStoA0, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoA0.from_rule.rule, ([S], [A, 0, A]))
        self.assertEqual(fromStoA0.replace_index, 2)
        class RuleNewAtoB(Rule): rule = ([A], [B])
        self.assertIn(RuleNewAtoB, com.rules)
        fromAtoB = list(filter(lambda x: hash(x) == hash(RuleNewAtoB), com.rules))[0]
        self.assertTrue(isclass(fromAtoB))
        self.assertTrue(issubclass(fromAtoB, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromAtoB.from_rule.rule, ([A], [B, C]))
        self.assertEqual(fromAtoB.replace_index, 1)
        class RuleNewAtoC(Rule): rule = ([A], [C])
        self.assertIn(RuleNewAtoC, com.rules)
        fromAtoC = list(filter(lambda x: hash(x) == hash(RuleNewAtoC), com.rules))[0]
        self.assertTrue(isclass(fromAtoC))
        self.assertTrue(issubclass(fromAtoC, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromAtoC.from_rule.rule, ([A], [B, C]))
        self.assertEqual(fromAtoC.replace_index, 0)
        class RuleNewAtoCC(Rule): rule = ([A], [C, C])
        self.assertIn(RuleNewAtoCC, com.rules)
        fromAtoCC = list(filter(lambda x: hash(x) == hash(RuleNewAtoCC), com.rules))[0]
        self.assertTrue(isclass(fromAtoCC))
        self.assertTrue(issubclass(fromAtoCC, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromAtoCC.from_rule.rule, ([A], [C, C, C]))
        self.assertEqual(fromAtoCC.replace_index, 0)
        class RuleNewBto1(Rule): rule = ([B], [1])
        self.assertIn(RuleNewBto1, com.rules)
        fromBto1 = list(filter(lambda x: hash(x) == hash(RuleNewBto1), com.rules))[0]
        self.assertTrue(isclass(fromBto1))
        self.assertTrue(issubclass(fromBto1, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromBto1.from_rule.rule, ([B], [1, C]))
        self.assertEqual(fromBto1.replace_index, 1)
        class RuleNewBto3(Rule): rule = ([B], [3])
        self.assertIn(RuleNewBto3, com.rules)
        fromBto3 = list(filter(lambda x: hash(x) == hash(RuleNewBto3), com.rules))[0]
        self.assertTrue(isclass(fromBto3))
        self.assertTrue(issubclass(fromBto3, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromBto3.from_rule.rule, ([B], [3, D]))
        self.assertEqual(fromBto3.replace_index, 1)
        class RuleNewCtoA3(Rule): rule = ([C], [A, 3])
        self.assertIn(RuleNewCtoA3, com.rules)
        fromCtoA3 = list(filter(lambda x: hash(x) == hash(RuleNewCtoA3), com.rules))[0]
        self.assertTrue(isclass(fromCtoA3))
        self.assertTrue(issubclass(fromCtoA3, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromCtoA3.from_rule.rule, ([C], [A, A, 3]))
        self.assertEqual(fromCtoA3.replace_index, 0)
        class RuleNewDtoAB(Rule): rule = ([D], [A, B])
        self.assertIn(RuleNewDtoAB, com.rules)
        fromDtoAB = list(filter(lambda x: hash(x) == hash(RuleNewDtoAB), com.rules))[0]
        self.assertTrue(isclass(fromDtoAB))
        self.assertTrue(issubclass(fromDtoAB, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDtoAB.from_rule.rule, ([D], [A, A, B]))
        self.assertEqual(fromDtoAB.replace_index, 0)
        class RuleNewDtoAA(Rule): rule = ([D], [A, A])
        self.assertIn(RuleNewDtoAA, com.rules)
        fromDtoAA = list(filter(lambda x: hash(x) == hash(RuleNewDtoAA), com.rules))[0]
        self.assertTrue(isclass(fromDtoAA))
        self.assertTrue(issubclass(fromDtoAA, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDtoAA.from_rule.rule, ([D], [A, A, B]))
        self.assertEqual(fromDtoAA.replace_index, 2)
        class RuleNewDtoA3(Rule): rule = ([D], [A, 3])
        self.assertIn(RuleNewDtoA3, com.rules)
        fromDtoA3 = list(filter(lambda x: hash(x) == hash(RuleNewDtoA3), com.rules))[0]
        self.assertTrue(isclass(fromDtoA3))
        self.assertTrue(issubclass(fromDtoA3, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDtoA3.from_rule.rule, ([D], [A, A, 3]))
        self.assertEqual(fromDtoA3.replace_index, 0)
        class RuleNewCto3(Rule): rule = ([C], [3])
        self.assertIn(RuleNewCto3, com.rules)
        fromCto3 = list(filter(lambda x: hash(x) == hash(RuleNewCto3), com.rules))[0]
        self.assertTrue(isclass(fromCto3))
        self.assertTrue(issubclass(fromCto3, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromCto3.from_rule.rule, ([C], [A, 3]))
        self.assertEqual(fromCto3.replace_index, 0)
        class RuleNewDtoA(Rule): rule = ([D], [A])
        self.assertIn(RuleNewDtoA, com.rules)
        fromDtoA = list(filter(lambda x: hash(x) == hash(RuleNewDtoA), com.rules))[0]
        self.assertTrue(isclass(fromDtoA))
        self.assertTrue(issubclass(fromDtoA, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDtoA.from_rule.rule, ([D], [A, B]))
        self.assertEqual(fromDtoA.replace_index, 1)
        class RuleNewDtoB(Rule): rule = ([D], [B])
        self.assertIn(RuleNewDtoB, com.rules)
        fromDtoB = list(filter(lambda x: hash(x) == hash(RuleNewDtoB), com.rules))[0]
        self.assertTrue(isclass(fromDtoB))
        self.assertTrue(issubclass(fromDtoB, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDtoB.from_rule.rule, ([D], [A, B]))
        self.assertEqual(fromDtoB.replace_index, 0)
        class RuleNewDto3(Rule): rule = ([D], [3])
        self.assertIn(RuleNewDto3, com.rules)
        fromDto3 = list(filter(lambda x: hash(x) == hash(RuleNewDto3), com.rules))[0]
        self.assertTrue(isclass(fromDto3))
        self.assertTrue(issubclass(fromDto3, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDto3.from_rule.rule, ([D], [A, 3]))
        self.assertEqual(fromDto3.replace_index, 0)
        class BtoEps(Rule): rule=([B], [EPS])
        class CtoEps(Rule): rule=([B], [EPS])
        self.assertNotIn(BtoEps, com.rules)
        self.assertNotIn(CtoEps, com.rules)

    def test_multipleUsageShouldNotChange(self):
        g = Grammar(terminals=[0, 1, 2, 3],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        ContextFree.remove_rules_with_epsilon(g)
        self.assertEqual(len(g.rules), 12)
        self.assertEqual(g.rules.size(), 12)
        class RuleNewAto0A(Rule): rule = ([A], [0, A])
        class RuleNewAtoA0(Rule): rule = ([A], [A, 0])
        class RuleNewAtoB(Rule): rule = ([A], [B])
        class RuleNewAtoC(Rule): rule = ([A], [C])
        class RuleNewAtoCC(Rule): rule = ([A], [C, C])
        class RuleNewAto1(Rule): rule = ([A], [1])
        class RuleNewBto3(Rule): rule = ([B], [3])
        class RuleNewCtoA3(Rule): rule = ([C], [A, 3])
        class RuleNewDtoAB(Rule): rule = ([D], [A, B])
        class RuleNewDtoAA(Rule): rule = ([D], [A, A])
        class RuleNewDtoA3(Rule): rule = ([D], [A, 3])
        class RuleNewCto3(Rule): rule = ([C], [3])
        class RuleNewDtoA(Rule): rule = ([D], [A])
        class RuleNewDtoB(Rule): rule = ([D], [B])
        class RuleNewDto3(Rule): rule = ([D], [3])
        self.assertNotIn(RuleNewAto0A, g.rules)
        self.assertNotIn(RuleNewAtoA0, g.rules)
        self.assertNotIn(RuleNewAtoB, g.rules)
        self.assertNotIn(RuleNewAtoC, g.rules)
        self.assertNotIn(RuleNewAtoCC, g.rules)
        self.assertNotIn(RuleNewAto1, g.rules)
        self.assertNotIn(RuleNewBto3, g.rules)
        self.assertNotIn(RuleNewCtoA3, g.rules)
        self.assertNotIn(RuleNewDtoAB, g.rules)
        self.assertNotIn(RuleNewDtoAA, g.rules)
        self.assertNotIn(RuleNewDtoA3, g.rules)
        self.assertNotIn(RuleNewCto3, g.rules)
        self.assertNotIn(RuleNewDtoA, g.rules)
        self.assertNotIn(RuleNewDtoB, g.rules)
        self.assertNotIn(RuleNewDto3, g.rules)
        class BtoEps(Rule): rule=([B], [EPS])
        class CtoEps(Rule): rule=([B], [EPS])
        self.assertIn(BtoEps, g.rules)
        self.assertIn(CtoEps, g.rules)

    def test_multipleUsageShouldChange(self):
        g = Grammar(terminals=[0, 1, 2, 3],
                    nonterminals=[S, A, B, C, D],
                    rules=[Rules],
                    start_symbol=S)
        ContextFree.remove_rules_with_epsilon(g, True)
        self.assertEqual(len(g.rules), 25)
        self.assertEqual(g.rules.size(), 25)
        class RuleNewSto0A(Rule): rule = ([S], [0, A])
        self.assertIn(RuleNewSto0A, g.rules)
        fromSto0A = list(filter(lambda x: hash(x) == hash(RuleNewSto0A), g.rules))[0]
        self.assertTrue(isclass(fromSto0A))
        self.assertTrue(issubclass(fromSto0A, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromSto0A.from_rule.rule, ([S], [A, 0, A]))
        self.assertEqual(fromSto0A.replace_index, 0)
        class RuleNewStoA0(Rule): rule = ([S], [A, 0])
        self.assertIn(RuleNewStoA0, g.rules)
        fromStoA0 = list(filter(lambda x: hash(x) == hash(RuleNewStoA0), g.rules))[0]
        self.assertTrue(isclass(fromStoA0))
        self.assertTrue(issubclass(fromStoA0, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromStoA0.from_rule.rule, ([S], [A, 0, A]))
        self.assertEqual(fromStoA0.replace_index, 2)
        class RuleNewAtoB(Rule): rule = ([A], [B])
        self.assertIn(RuleNewAtoB, g.rules)
        fromAtoB = list(filter(lambda x: hash(x) == hash(RuleNewAtoB), g.rules))[0]
        self.assertTrue(isclass(fromAtoB))
        self.assertTrue(issubclass(fromAtoB, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromAtoB.from_rule.rule, ([A], [B, C]))
        self.assertEqual(fromAtoB.replace_index, 1)
        class RuleNewAtoC(Rule): rule = ([A], [C])
        self.assertIn(RuleNewAtoC, g.rules)
        fromAtoC = list(filter(lambda x: hash(x) == hash(RuleNewAtoC), g.rules))[0]
        self.assertTrue(isclass(fromAtoC))
        self.assertTrue(issubclass(fromAtoC, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromAtoC.from_rule.rule, ([A], [B, C]))
        self.assertEqual(fromAtoC.replace_index, 0)
        class RuleNewAtoCC(Rule): rule = ([A], [C, C])
        self.assertIn(RuleNewAtoCC, g.rules)
        fromAtoCC = list(filter(lambda x: hash(x) == hash(RuleNewAtoCC), g.rules))[0]
        self.assertTrue(isclass(fromAtoCC))
        self.assertTrue(issubclass(fromAtoCC, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromAtoCC.from_rule.rule, ([A], [C, C, C]))
        self.assertEqual(fromAtoCC.replace_index, 0)
        class RuleNewBto1(Rule): rule = ([B], [1])
        self.assertIn(RuleNewBto1, g.rules)
        fromBto1 = list(filter(lambda x: hash(x) == hash(RuleNewBto1), g.rules))[0]
        self.assertTrue(isclass(fromBto1))
        self.assertTrue(issubclass(fromBto1, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromBto1.from_rule.rule, ([B], [1, C]))
        self.assertEqual(fromBto1.replace_index, 1)
        class RuleNewBto3(Rule): rule = ([B], [3])
        self.assertIn(RuleNewBto3, g.rules)
        fromBto3 = list(filter(lambda x: hash(x) == hash(RuleNewBto3), g.rules))[0]
        self.assertTrue(isclass(fromBto3))
        self.assertTrue(issubclass(fromBto3, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromBto3.from_rule.rule, ([B], [3, D]))
        self.assertEqual(fromBto3.replace_index, 1)
        class RuleNewCtoA3(Rule): rule = ([C], [A, 3])
        self.assertIn(RuleNewCtoA3, g.rules)
        fromCtoA3 = list(filter(lambda x: hash(x) == hash(RuleNewCtoA3), g.rules))[0]
        self.assertTrue(isclass(fromCtoA3))
        self.assertTrue(issubclass(fromCtoA3, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromCtoA3.from_rule.rule, ([C], [A, A, 3]))
        self.assertEqual(fromCtoA3.replace_index, 0)
        class RuleNewDtoAB(Rule): rule = ([D], [A, B])
        self.assertIn(RuleNewDtoAB, g.rules)
        fromDtoAB = list(filter(lambda x: hash(x) == hash(RuleNewDtoAB), g.rules))[0]
        self.assertTrue(isclass(fromDtoAB))
        self.assertTrue(issubclass(fromDtoAB, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDtoAB.from_rule.rule, ([D], [A, A, B]))
        self.assertEqual(fromDtoAB.replace_index, 0)
        class RuleNewDtoAA(Rule): rule = ([D], [A, A])
        self.assertIn(RuleNewDtoAA, g.rules)
        fromDtoAA = list(filter(lambda x: hash(x) == hash(RuleNewDtoAA), g.rules))[0]
        self.assertTrue(isclass(fromDtoAA))
        self.assertTrue(issubclass(fromDtoAA, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDtoAA.from_rule.rule, ([D], [A, A, B]))
        self.assertEqual(fromDtoAA.replace_index, 2)
        class RuleNewDtoA3(Rule): rule = ([D], [A, 3])
        self.assertIn(RuleNewDtoA3, g.rules)
        fromDtoA3 = list(filter(lambda x: hash(x) == hash(RuleNewDtoA3), g.rules))[0]
        self.assertTrue(isclass(fromDtoA3))
        self.assertTrue(issubclass(fromDtoA3, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDtoA3.from_rule.rule, ([D], [A, A, 3]))
        self.assertEqual(fromDtoA3.replace_index, 0)
        class RuleNewCto3(Rule): rule = ([C], [3])
        self.assertIn(RuleNewCto3, g.rules)
        fromCto3 = list(filter(lambda x: hash(x) == hash(RuleNewCto3), g.rules))[0]
        self.assertTrue(isclass(fromCto3))
        self.assertTrue(issubclass(fromCto3, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromCto3.from_rule.rule, ([C], [A, 3]))
        self.assertEqual(fromCto3.replace_index, 0)
        class RuleNewDtoA(Rule): rule = ([D], [A])
        self.assertIn(RuleNewDtoA, g.rules)
        fromDtoA = list(filter(lambda x: hash(x) == hash(RuleNewDtoA), g.rules))[0]
        self.assertTrue(isclass(fromDtoA))
        self.assertTrue(issubclass(fromDtoA, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDtoA.from_rule.rule, ([D], [A, B]))
        self.assertEqual(fromDtoA.replace_index, 1)
        class RuleNewDtoB(Rule): rule = ([D], [B])
        self.assertIn(RuleNewDtoB, g.rules)
        fromDtoB = list(filter(lambda x: hash(x) == hash(RuleNewDtoB), g.rules))[0]
        self.assertTrue(isclass(fromDtoB))
        self.assertTrue(issubclass(fromDtoB, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDtoB.from_rule.rule, ([D], [A, B]))
        self.assertEqual(fromDtoB.replace_index, 0)
        class RuleNewDto3(Rule): rule = ([D], [3])
        self.assertIn(RuleNewDto3, g.rules)
        fromDto3 = list(filter(lambda x: hash(x) == hash(RuleNewDto3), g.rules))[0]
        self.assertTrue(isclass(fromDto3))
        self.assertTrue(issubclass(fromDto3, ContextFree.EpsilonRemovedRule))
        self.assertEqual(fromDto3.from_rule.rule, ([D], [A, 3]))
        self.assertEqual(fromDto3.replace_index, 0)
        class BtoEps(Rule): rule=([B], [EPS])
        class CtoEps(Rule): rule=([B], [EPS])
        self.assertNotIn(BtoEps, g.rules)
        self.assertNotIn(CtoEps, g.rules)


if __name__ == '__main__':
    main()
