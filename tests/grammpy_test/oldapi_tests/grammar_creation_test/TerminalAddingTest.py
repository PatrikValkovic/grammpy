#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 22:00
:Licence MIT
Part of grammpy

"""

from unittest import TestCase, main

from grammpy.old_api import Grammar


class TerminalAddingTest(TestCase):
    def test_shouldAddOneTerminal(self):
        g = Grammar(terminals=['asdf'])
        self.assertTrue(g.have_term('asdf'))
        self.assertFalse(g.have_term('a'))

    def test_shouldAddMoreTerminals(self):
        g = Grammar(terminals=[0, 1, 2])
        self.assertTrue(g.have_term([0, 1, 2]))
        self.assertFalse(g.have_term('a'))
        self.assertFalse(g.have_term('asdf'))
        self.assertFalse(g.have_term(3))


if __name__ == '__main__':
    main()
