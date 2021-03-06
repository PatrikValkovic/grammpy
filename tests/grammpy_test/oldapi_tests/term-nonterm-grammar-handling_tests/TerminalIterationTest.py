#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 12:28
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main

from grammpy.old_api import Grammar


class TempClass:
    pass


class TerminalIterationTest(TestCase):
    def test_oneTerminalTerms(self):
        gr = Grammar()
        gr.add_term('a')
        for i in gr.terms():
            self.assertEqual(i.s, 'a')

    def test_oneTerminalGetTerm(self):
        gr = Grammar()
        gr.add_term('a')
        for i in gr.get_term():
            self.assertEqual(i.s, 'a')

    def test_ThreeTerminalTerms(self):
        gr = Grammar()
        gr.add_term([0, 'a', TempClass])
        s = set(term.s for term in gr.terms())
        for i in [0, 'a', TempClass]:
            self.assertTrue(i in s)

    def test_ThreeTerminalGetTerm(self):
        gr = Grammar()
        gr.add_term([0, 'a', TempClass])
        s = set(term.s for term in gr.get_term())
        for i in [0, 'a', TempClass]:
            self.assertIn(i, s)


if __name__ == '__main__':
    main()
