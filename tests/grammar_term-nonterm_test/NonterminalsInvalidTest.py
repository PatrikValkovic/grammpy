#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase, main

from grammpy import Nonterminal
from grammpy.Grammars.RawGrammar import RawGrammar as Grammar
from grammpy.Terminal import Terminal
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

    def test_invalidRemoveNumber(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.remove_nonterm(0)

    def test_invalidRemoveString(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.remove_nonterm("string")

    def test_invalidRemoveAfterCorrectAdd(self):
        gr = Grammar()
        gr.add_nonterm(TempClass)
        with self.assertRaises(NotNonterminalException):
            gr.remove_nonterm("asdf")

    def test_invalidRemoveInArray(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.remove_nonterm([TempClass, "asdf"])

    def test_invalidGetNumber(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.get_nonterm(0)

    def test_invalidGetString(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.get_nonterm("string")

    def test_invalidGetAfterCorrectAdd(self):
        gr = Grammar()
        gr.add_nonterm(TempClass)
        with self.assertRaises(NotNonterminalException):
            gr.get_nonterm("asdf")

    def test_invalidGetInArray(self):
        gr = Grammar()
        with self.assertRaises(NotNonterminalException):
            gr.get_nonterm([TempClass, "asdf"])

    def test_rawTermMethod(self):
        gr = Grammar()
        gr.add_term([TempClass, 'a', 0])
        self.assertEqual(gr.term(['a'])[0].s,'a')
        self.assertIsInstance(gr.term([0])[0],Terminal)
        self.assertIsNone(gr.term(['asdf'])[0])



if __name__ == '__main__':
    main()
