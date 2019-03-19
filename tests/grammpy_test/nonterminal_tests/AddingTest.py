#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 15:37
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal
from grammpy.exceptions import NotNonterminalException


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass


class AddingTest(TestCase):

    def test_haveEmpty(self):
        gr = Grammar()
        self.assertNotIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertNotIn(C, gr.nonterminals)

    def test_correctAddOne(self):
        gr = Grammar()
        self.assertEqual(gr.nonterminals.size(), 0)
        self.assertEqual(len(gr.nonterminals), 0)
        self.assertNotIn(A, gr.nonterminals)
        gr.nonterminals.add(A)
        self.assertEqual(gr.nonterminals.size(), 1)
        self.assertEqual(len(gr.nonterminals), 1)
        self.assertIn(A, gr.nonterminals)

    def test_correctAddTwo(self):
        gr = Grammar()
        self.assertEqual(gr.nonterminals.size(), 0)
        self.assertEqual(len(gr.nonterminals), 0)
        self.assertNotIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        gr.nonterminals.add(A)
        self.assertEqual(gr.nonterminals.size(), 1)
        self.assertEqual(len(gr.nonterminals), 1)
        self.assertIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        gr.nonterminals.add(B)
        self.assertEqual(gr.nonterminals.size(), 2)
        self.assertEqual(len(gr.nonterminals), 2)
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)

    def test_addThreeAsParameters(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)

    def test_addThreeAsArray(self):
        gr = Grammar()
        gr.nonterminals.add(*[A, B, C])
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)

    def test_oneSeparateTwoTuple(self):
        gr = Grammar()
        gr.nonterminals.add(A)
        self.assertEqual(gr.nonterminals.size(), 1)
        self.assertEqual(len(gr.nonterminals), 1)
        self.assertIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertNotIn(C, gr.nonterminals)
        gr.nonterminals.add(*(B, C))
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)

    def test_addSameTwiceInParameters(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, A, C)
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)

    def test_addSameTwiceInSequence(self):
        gr = Grammar()
        gr.nonterminals.add(A, C)
        self.assertEqual(gr.nonterminals.size(), 2)
        self.assertEqual(len(gr.nonterminals), 2)
        self.assertIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)
        gr.nonterminals.add(A, B)
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        self.assertIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)

    def test_addNonterminal(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.add(0)

    def test_addNonterminalAfterTerminal(self):
        gr = Grammar()
        gr.nonterminals.add(A)
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.add(0)

    def test_addNonterminalAndTerminalInArray(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.add([A, 0])

    def test_addNonterminalAndTerminalInParameters(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.add(A, 0)

    def test_addNonterminalAndTerminalInArrayAfterValid(self):
        gr = Grammar()
        gr.nonterminals.add(A)
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.add(*[B, 0])

    def test_addNonterminalAndTerminalAsParametersAfterValid(self):
        gr = Grammar()
        gr.nonterminals.add(A)
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.add(B, 0)


if __name__ == '__main__':
    main()
