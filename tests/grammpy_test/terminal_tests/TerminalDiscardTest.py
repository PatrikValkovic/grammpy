#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.03.2019 22:44
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main

from grammpy import Grammar


class TempClass:
    pass


class TerminalDiscardTest(TestCase):
    def test_removeOne(self):
        gr = Grammar()
        gr.terminals.add(*[0, 'asdf', TempClass])
        self.assertEqual(gr.terminals.size(), 3)
        self.assertEqual(len(gr.terminals), 3)
        gr.terminals.discard(0)
        self.assertEqual(gr.terminals.size(), 2)
        self.assertEqual(len(gr.terminals), 2)
        self.assertNotIn(0, gr.terminals)
        self.assertIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)

    def test_removeClass(self):
        gr = Grammar()
        gr.terminals.add(*[0, 'asdf', TempClass])
        self.assertEqual(gr.terminals.size(), 3)
        self.assertEqual(len(gr.terminals), 3)
        gr.terminals.discard(TempClass)
        self.assertEqual(gr.terminals.size(), 2)
        self.assertEqual(len(gr.terminals), 2)
        self.assertIn(0, gr.terminals)
        self.assertIn('asdf', gr.terminals)
        self.assertNotIn(TempClass, gr.terminals)

    def test_removeTwo(self):
        gr = Grammar()
        gr.terminals.add(*[0, 'asdf', TempClass])
        self.assertEqual(gr.terminals.size(), 3)
        self.assertEqual(len(gr.terminals), 3)
        gr.terminals.discard(0)
        gr.terminals.discard('asdf')
        self.assertEqual(gr.terminals.size(), 1)
        self.assertEqual(len(gr.terminals), 1)
        self.assertNotIn(0, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)

    def test_removeTwoInArray(self):
        gr = Grammar()
        gr.terminals.add(*[0, 'asdf', TempClass])
        self.assertEqual(gr.terminals.size(), 3)
        self.assertEqual(len(gr.terminals), 3)
        gr.terminals.discard(*[0, 'asdf'])
        self.assertEqual(gr.terminals.size(), 1)
        self.assertEqual(len(gr.terminals), 1)
        self.assertNotIn(0, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)

    def test_removeTwoInParameters(self):
        gr = Grammar()
        gr.terminals.add(*[0, 'asdf', TempClass])
        self.assertEqual(gr.terminals.size(), 3)
        self.assertEqual(len(gr.terminals), 3)
        gr.terminals.discard(0, 'asdf')
        self.assertEqual(gr.terminals.size(), 1)
        self.assertEqual(len(gr.terminals), 1)
        self.assertNotIn(0, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)

    def test_removeAllWithoutParam(self):
        gr = Grammar()
        gr.terminals.add(0, 'asdf', TempClass)
        self.assertEqual(gr.terminals.size(), 3)
        self.assertEqual(len(gr.terminals), 3)
        gr.terminals.clear()
        self.assertEqual(gr.terminals.size(), 0)
        self.assertEqual(len(gr.terminals), 0)
        self.assertNotIn(0, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)
        self.assertNotIn(TempClass, gr.terminals)

    def test_removeEmptyGrammar(self):
        gr = Grammar()
        self.assertEqual(gr.terminals.size(), 0)
        self.assertEqual(len(gr.terminals), 0)
        gr.terminals.clear()
        self.assertEqual(gr.terminals.size(), 0)
        self.assertEqual(len(gr.terminals), 0)

    def test_removeSameElementMoreTimesInArray(self):
        gr = Grammar()
        gr.terminals.add(*[0, 'asdf', TempClass])
        self.assertEqual(gr.terminals.size(), 3)
        self.assertEqual(len(gr.terminals), 3)
        gr.terminals.discard(*[0, 0])
        self.assertEqual(gr.terminals.size(), 2)
        self.assertEqual(len(gr.terminals), 2)
        self.assertNotIn(0, gr.terminals)
        self.assertIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)

    def test_removeSameElementMoreTimesAsParameters(self):
        gr = Grammar()
        gr.terminals.add(*[0, 'asdf', TempClass])
        self.assertEqual(gr.terminals.size(), 3)
        self.assertEqual(len(gr.terminals), 3)
        gr.terminals.discard(0, 0)
        self.assertEqual(gr.terminals.size(), 2)
        self.assertEqual(len(gr.terminals), 2)
        self.assertNotIn(0, gr.terminals)
        self.assertIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)

    def test_removeSameElementMoreTimesSequentally(self):
        gr = Grammar()
        gr.terminals.add(*[0, 'asdf', TempClass])
        self.assertEqual(gr.terminals.size(), 3)
        self.assertEqual(len(gr.terminals), 3)
        gr.terminals.discard(0)
        gr.terminals.discard(0)
        self.assertEqual(gr.terminals.size(), 2)
        self.assertEqual(len(gr.terminals), 2)
        self.assertNotIn(0, gr.terminals)
        self.assertIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)


if __name__ == '__main__':
    main()
