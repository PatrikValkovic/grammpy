#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.03.2019 22:00
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import Grammar


class TempClass:
    pass


class TerminalAddingTest(TestCase):

    def test_haveTermEmpty(self):
        gr = Grammar()
        self.assertNotIn(TempClass, gr.terminals)
        self.assertNotIn(1, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)

    def test_correctAddOne(self):
        gr = Grammar()
        self.assertEqual(gr.terminals.size(), 0)
        self.assertEqual(len(gr.terminals), 0)
        self.assertNotIn(0, gr.terminals)
        gr.terminals.add(0)
        self.assertEqual(gr.terminals.size(), 1)
        self.assertEqual(len(gr.terminals), 1)
        self.assertIn(0, gr.terminals)

    def test_correctAddTwo(self):
        gr = Grammar()
        self.assertEqual(gr.terminals.size(), 0)
        self.assertEqual(len(gr.terminals), 0)
        self.assertNotIn(0, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)
        gr.terminals.add(0)
        self.assertEqual(gr.terminals.size(), 1)
        self.assertEqual(len(gr.terminals), 1)
        self.assertIn(0, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)
        gr.terminals.add('asdf')
        self.assertEqual(gr.terminals.size(), 2)
        self.assertEqual(len(gr.terminals), 2)
        self.assertIn(0, gr.terminals)
        self.assertIn('asdf', gr.terminals)

    def test_addInArray(self):
        gr = Grammar()
        gr.terminals.add(0, 'asdf', TempClass)
        self.assertEqual(gr.terminals.size(), 3)
        self.assertEqual(len(gr.terminals), 3)
        self.assertIn(0, gr.terminals)
        self.assertIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)

    def test_oneSeparateTwoTuple(self):
        gr = Grammar()
        gr.terminals.add(0)
        self.assertEqual(gr.terminals.size(), 1)
        self.assertEqual(len(gr.terminals), 1)
        self.assertIn(0, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)
        self.assertNotIn(TempClass, gr.terminals)
        gr.terminals.add(*('asdf', TempClass))
        self.assertEqual(gr.terminals.size(), 3)
        self.assertEqual(len(gr.terminals), 3)
        self.assertIn(0, gr.terminals)
        self.assertIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)


    def test_equalGetTermAndTermMethods(self):
        gr = Grammar()
        ins = TempClass()
        gr.terminals.add(ins)
        self.assertEqual(gr.terminals.size(), 1)
        self.assertEqual(len(gr.terminals), 1)
        self.assertIn(ins, gr.terminals)


if __name__ == '__main__':
    main()
