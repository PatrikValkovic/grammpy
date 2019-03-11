#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.03.2019 17:56
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar, Nonterminal
from grammpy.exceptions import NotNonterminalException


class A(Nonterminal): pass
class B(Nonterminal): pass
class C(Nonterminal): pass
class D(Nonterminal): pass


class DiscardTest(TestCase):
    def test_removeOne(self):
        gr = Grammar()
        gr.nonterminals.add(*[A, B, C])
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        gr.nonterminals.discard(A)
        self.assertEqual(gr.nonterminals.size(), 2)
        self.assertEqual(len(gr.nonterminals), 2)
        self.assertNotIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)
        self.assertNotIn(D, gr.nonterminals)

    def test_removeTwo(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        gr.nonterminals.discard(A)
        gr.nonterminals.discard(B)
        self.assertEqual(gr.nonterminals.size(), 1)
        self.assertEqual(len(gr.nonterminals), 1)
        self.assertNotIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)
        self.assertNotIn(D, gr.nonterminals)


    def test_removeTwoInArray(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        gr.nonterminals.discard(A, B)
        self.assertEqual(gr.nonterminals.size(), 1)
        self.assertEqual(len(gr.nonterminals), 1)
        self.assertNotIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)
        self.assertNotIn(D, gr.nonterminals)

    def test_removeTwoInParameters(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        gr.nonterminals.discard(*[A, B])
        self.assertEqual(gr.nonterminals.size(), 1)
        self.assertEqual(len(gr.nonterminals), 1)
        self.assertNotIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)
        self.assertNotIn(D, gr.nonterminals)

    def test_removeAll(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        gr.nonterminals.clear()
        self.assertEqual(gr.nonterminals.size(), 0)
        self.assertEqual(len(gr.nonterminals), 0)
        self.assertNotIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertNotIn(C, gr.nonterminals)

    def test_removeEmptyGrammar(self):
        gr = Grammar()
        self.assertEqual(gr.nonterminals.size(), 0)
        self.assertEqual(len(gr.nonterminals), 0)
        gr.nonterminals.clear()
        self.assertEqual(gr.nonterminals.size(), 0)
        self.assertEqual(len(gr.nonterminals), 0)

    def test_removeSameElementMoreTimesInArray(self):
        gr = Grammar()
        gr.nonterminals.add(*[A, B, C])
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        gr.nonterminals.discard(*[B, B])
        self.assertEqual(gr.nonterminals.size(), 2)
        self.assertEqual(len(gr.nonterminals), 2)
        self.assertIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)

    def test_removeSameElementMoreTimesAsParameters(self):
        gr = Grammar()
        gr.nonterminals.add(*[A, B, C])
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        gr.nonterminals.discard(B, B)
        self.assertEqual(gr.nonterminals.size(), 2)
        self.assertEqual(len(gr.nonterminals), 2)
        self.assertIn(A, gr.nonterminals)
        self.assertNotIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)

    def test_removeSameElementMoreTimesSequentally(self):
        gr = Grammar()
        gr.nonterminals.add(*[A, B, C])
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        gr.nonterminals.discard(A)
        gr.nonterminals.discard(A)
        self.assertEqual(gr.nonterminals.size(), 2)
        self.assertEqual(len(gr.nonterminals), 2)
        self.assertNotIn(A, gr.nonterminals)
        self.assertIn(B, gr.nonterminals)
        self.assertIn(C, gr.nonterminals)

    def test_removeElementNotThere(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        gr.nonterminals.discard(D)

    def test_removeOneOfTheElementNotThere(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        self.assertEqual(gr.nonterminals.size(), 3)
        self.assertEqual(len(gr.nonterminals), 3)
        gr.nonterminals.discard(B, D)

    def test_removeInvalid(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.discard(0)

    def test_removeInvalidOnEmpty(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.discard(0)

    def test_removeInvalidAsOneOfThem(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.discard(B, 0)

    def test_removeInvalidMoreTimes(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.discard(1, 0)

    def test_removeInvalidMoreTimesBetweenValid(self):
        gr = Grammar()
        gr.nonterminals.add(A, B, C)
        with self.assertRaises(NotNonterminalException):
            gr.nonterminals.discard(A, 1, B, 0)


if __name__ == '__main__':
    main()
