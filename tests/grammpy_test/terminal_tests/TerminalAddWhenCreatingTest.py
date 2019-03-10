#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.03.2019 22:00
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main

from grammpy import Grammar


class TerminalAddWhenCreatingTest(TestCase):
    def test_addOneInArray(self):
        gr = Grammar(terminals=['A'])
        self.assertIn('A', gr.terminals)

    def test_addTwoInArray(self):
        gr = Grammar(terminals=['A', 0])
        self.assertIn(0, gr.terminals)
        self.assertIn('A', gr.terminals)

    def test_addOneSeparate(self):
        gr = Grammar(terminals='A')
        self.assertIn('A', gr.terminals)

    def test_addThreeInString(self):
        gr = Grammar(terminals='ABC')
        self.assertIn('A', gr.terminals)
        self.assertIn('B', gr.terminals)
        self.assertIn('C', gr.terminals)
        self.assertNotIn('D', gr.terminals)

    def test_addThreeInTuple(self):
        gr = Grammar(terminals=('A', 'B', 'C'))
        self.assertIn('A', gr.terminals)
        self.assertIn('B', gr.terminals)
        self.assertIn('C', gr.terminals)
        self.assertNotIn('D', gr.terminals)

    def test_addThreeOneDelete(self):
        gr = Grammar(terminals=('A', 'B', 'C'))
        self.assertIn('A', gr.terminals)
        self.assertIn('B', gr.terminals)
        self.assertIn('C', gr.terminals)
        self.assertNotIn('D', gr.terminals)
        gr.terminals.remove('B')
        self.assertIn('A', gr.terminals)
        self.assertNotIn('B', gr.terminals)
        self.assertIn('C', gr.terminals)
        self.assertNotIn('D', gr.terminals)


if __name__ == '__main__':
    main()