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


class TerminalAddRemoveMixedTest(TestCase):
    def test_add_remove_add_one(self):
        gr = Grammar()
        self.assertEqual(len(gr.terminals), 0)
        self.assertNotIn(0, gr.terminals)
        gr.terminals.add(0)
        self.assertEqual(len(gr.terminals), 1)
        self.assertIn(0, gr.terminals)
        gr.terminals.remove(0)
        self.assertEqual(len(gr.terminals), 0)
        self.assertNotIn(0, gr.terminals)

    def test_addTwoRemoveOneAndAddThird(self):
        gr = Grammar()
        gr.terminals.add(0, 'asdf')
        self.assertEqual(len(gr.terminals), 2)
        self.assertIn(0, gr.terminals)
        self.assertIn('asdf', gr.terminals)
        self.assertNotIn(TempClass, gr.terminals)
        gr.terminals.remove('asdf')
        self.assertEqual(len(gr.terminals), 1)
        self.assertIn(0, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)
        self.assertNotIn(TempClass, gr.terminals)
        gr.terminals.add(TempClass)
        self.assertEqual(len(gr.terminals), 2)
        self.assertIn(0, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)

    def test_addThreeRemoveTwoInArray(self):
        gr = Grammar()
        gr.terminals.add(0, 'asdf', TempClass)
        self.assertEqual(len(gr.terminals), 3)
        self.assertEqual(gr.terminals.size(), 3)
        self.assertIn(0, gr.terminals)
        self.assertIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)
        gr.terminals.remove(*[0, 'asdf'])
        self.assertEqual(len(gr.terminals), 1)
        self.assertEqual(gr.terminals.size(), 1)
        self.assertNotIn(0, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)
        self.assertIn(TempClass, gr.terminals)


if __name__ == '__main__':
    main()
