#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase, main
from grammpy.RawGrammar import RawGrammar as Grammar
from grammpy import Nonterminal
from grammpy.exceptions import NotNonterminalException


class TempClass(Nonterminal):
    pass


class NonterminalsInvalidTest(TestCase):
    def test_invalidAddNumber(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.add_nonterm(0)

    def test_invalidAddString(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.add_nonterm("string")

    def test_invalidAddAfterCorrectAdd(self):
        gr = Grammar()
        gr.add_nonterm(TempClass)
        with self.assertRaises(NotNonterminalException):
            gr.add_nonterm("asdf")

    def test_invalidAddInArray(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.add_nonterm([TempClass, "asdf"])

    def test_invalidHaveNumber(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.have_nonterm(0)

    def test_invalidHaveString(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.have_nonterm("string")

    def test_invalidHaveAfterCorrectAdd(self):
        gr = Grammar()
        gr.add_nonterm(TempClass)
        with self.assertRaises(NotNonterminalException):
            gr.have_nonterm("asdf")

    def test_invalidHaveInArray(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.have_nonterm([TempClass, "asdf"])


if __name__ == '__main__':
    main()
