#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase
from grammpy import Grammar


class TempClass:
    pass


class TerminalAddingTest(TestCase):
    def test_haveTermEmpty(self):
        gr = Grammar()
        self.assertFalse(gr.have_term(TempClass))
        self.assertFalse(gr.have_term(1))
        self.assertFalse(gr.have_term('asdf'))

    def test_haveTermClass(self):
        gr = Grammar()
        gr.add_term(TempClass)
        self.assertTrue(gr.have_term(TempClass))

    def test_haveTermArray(self):
        gr = Grammar()
        gr.add_term([TempClass, 0, 'asdf'])
        self.assertTrue(gr.have_term([0, 'asdf']))

    def test_dontHaveTermArray(self):
        gr = Grammar()
        gr.add_term([TempClass, 0, 'asdf'])
        self.assertFalse(gr.have_term([TempClass, 'a']))

    def test_haveTermTuple(self):
        gr = Grammar()
        gr.add_term([TempClass, 0, 'asdf'])
        self.assertTrue(gr.have_term((0, 'asdf')))

    def test_dontHaveTermTuple(self):
        gr = Grammar()
        gr.add_term([TempClass, 0, 'asdf'])
        self.assertFalse(gr.have_term((TempClass, 'a')))
