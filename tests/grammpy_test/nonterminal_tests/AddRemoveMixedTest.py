#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 17:43
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass


class AddRemoveMixedTest(TestCase):
    def test_add_remove_add_one(self):
        gr = Grammar()
        self.assertEqual(len(gr.nonterminals), 0)
        self.assertEqual(gr.nonterminals.size(), 0)
        self.assertNotIn(A, gr.nonterminals)
        gr.nonterminals.add(A)
        self.assertEqual(len(gr.nonterminals), 1)
        self.assertEqual(gr.nonterminals.size(), 1)
        self.assertIn(A, gr.nonterminals)
        gr.nonterminals.remove(A)
        self.assertEqual(len(gr.nonterminals), 0)
        self.assertEqual(gr.nonterminals.size(), 0)
        self.assertNotIn(A, gr.nonterminals)

    def test_addTwoRemoveOneAndAddThird(self):
        gr = Grammar()
        gr.nonterminals.add(A, B)
        self.assertEqual(len(gr.nonterminals), 2)
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertNotIn(C, gr.nonterminals)
        gr.nonterminals.remove(B)
        self.assertEqual(len(gr.nonterminals), 1)
        self.assertIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertNotIn(C, gr.nonterminals)
        gr.nonterminals.add(C)
        self.assertEqual(len(gr.nonterminals), 2)
        self.assertIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)

    def test_addThreeRemoveTwoInArray(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        self.assertEqual(len(gr.nonterminals), 3)
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)
        gr.nonterminals.remove(*[A, B])
        self.assertEqual(len(gr.nonterminals), 1)
        self.assertEqual(gr.nonterminals.size(), 1)
        self.assertNotIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)

    def test_addThreeRemoveTwoAsParameters(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        self.assertEqual(len(gr.nonterminals), 3)
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)
        gr.nonterminals.remove(A, B)
        self.assertEqual(len(gr.nonterminals), 1)
        self.assertEqual(gr.nonterminals.size(), 1)
        self.assertNotIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)


if __name__ == '__main__':
    main()