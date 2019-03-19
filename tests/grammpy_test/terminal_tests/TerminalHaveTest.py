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


class TerminalHaveTest(TestCase):
    def test_haveTermEmpty(self):
        gr = Grammar()
        self.assertNotIn(TempClass, gr.terminals)
        self.assertNotIn(1, gr.terminals)
        self.assertNotIn('asdf', gr.terminals)

    def test_haveTermClass(self):
        gr = Grammar()
        gr.terminals.add(TempClass)
        self.assertIn(TempClass, gr.terminals)

    def test_addMultiple(self):
        gr = Grammar()
        gr.terminals.add(*[TempClass, 0, 'asdf'])
        self.assertIn(TempClass, gr.terminals)
        self.assertIn(0, gr.terminals)
        self.assertIn('asdf', gr.terminals)


if __name__ == '__main__':
    main()
