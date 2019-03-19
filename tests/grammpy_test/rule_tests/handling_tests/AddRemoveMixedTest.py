#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 21:53
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal, Rule


class N(Nonterminal): pass
class A(Rule): rule=([N], [0])
class B(Rule): rule=([N], [1])
class C(Rule): rule=([N], [2])

class AddRemoveMixedTest(TestCase):
    def test_add_remove_add_one(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        self.assertEqual(len(gr.rules), 0)
        self.assertEqual(gr.rules.size(), 0)
        self.assertNotIn(A, gr.rules)
        gr.rules.add(A)
        self.assertEqual(len(gr.rules), 1)
        self.assertEqual(gr.rules.size(), 1)
        self.assertIn(A, gr.rules)
        gr.rules.remove(A)
        self.assertEqual(len(gr.rules), 0)
        self.assertEqual(gr.rules.size(), 0)
        self.assertNotIn(A, gr.rules)

    def test_addTwoRemoveOneAndAddThird(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B)
        self.assertEqual(len(gr.rules), 2)
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertNotIn(C, gr.rules)
        gr.rules.remove(B)
        self.assertEqual(len(gr.rules), 1)
        self.assertIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertNotIn(C, gr.rules)
        gr.rules.add(C)
        self.assertEqual(len(gr.rules), 2)
        self.assertIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_addThreeRemoveTwoInArray(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(len(gr.rules), 3)
        self.assertEqual(gr.rules.size(), 3)
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)
        gr.rules.remove(*[A, B])
        self.assertEqual(len(gr.rules), 1)
        self.assertEqual(gr.rules.size(), 1)
        self.assertNotIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertIn(C, gr.rules)

    def test_addThreeRemoveTwoAsParameters(self):
        gr = Grammar(terminals=[0, 1, 2],
                     nonterminals=[N])
        gr.rules.add(A, B, C)
        self.assertEqual(len(gr.rules), 3)
        self.assertEqual(gr.rules.size(), 3)
        self.assertIn(A, gr.rules)
        self.assertIn(B, gr.rules)
        self.assertIn(C, gr.rules)
        gr.rules.remove(A, B)
        self.assertEqual(len(gr.rules), 1)
        self.assertEqual(gr.rules.size(), 1)
        self.assertNotIn(A, gr.rules)
        self.assertNotIn(B, gr.rules)
        self.assertIn(C, gr.rules)


if __name__ == '__main__':
    main()
