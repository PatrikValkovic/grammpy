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


class TerminalIterationTest(TestCase):
    def test_oneTerminalTerms(self):
        gr = Grammar()
        gr.terminals.add('a')
        for t in gr.terminals:
            self.assertEqual(t, 'a')

    def test_ThreeTerminalTerms(self):
        gr = Grammar()
        gr.terminals.add(0, 'a', TempClass)
        s = list(term for term in gr.terminals)
        for i in [0, 'a', TempClass]:
            self.assertIn(i, s)


if __name__ == '__main__':
    main()
