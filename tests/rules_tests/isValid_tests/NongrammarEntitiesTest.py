#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 18:01
:Licence GNUv3
Part of grammpy

"""

from unittest import main, TestCase

from grammpy import Rule, Nonterminal as _N
from grammpy.exceptions import TerminalDoesNotExistsException, NonterminalDoesNotExistsException
from rules_tests.grammar import *


class Invalid(_N):
    pass


class NongrammarEntitiesTest(TestCase):
    def test_invalidTerminal(self):
        class tmp(Rule):
            rules = [([NFifth], [5, NFirst])]
        with self.assertRaises(TerminalDoesNotExistsException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_invalidTerminalFrom(self):
        class tmp(Rule):
            rules = [(['asdf', NFifth], [2, NFirst])]
        with self.assertRaises(TerminalDoesNotExistsException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_invalidTerminalMultiple(self):
        class tmp(Rule):
            rules = [([TSecond, 'b', TThird], ['c', 2]),
                     ([NFifth], [5, NFirst])]
        with self.assertRaises(TerminalDoesNotExistsException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_invalidTerminalFromMultiple(self):
        class tmp(Rule):
            rules = [([TSecond, 'b', TThird], ['c', 2]),
                     (['asdf', NFifth], [2, NFirst])]
        with self.assertRaises(TerminalDoesNotExistsException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_invalidNonterminal(self):
        class tmp(Rule):
            rules = [([NFifth], [2, Invalid])]
        with self.assertRaises(NonterminalDoesNotExistsException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_invalidNonterminalFrom(self):
        class tmp(Rule):
            rules = [(['a', Invalid], [2, NFirst])]
        with self.assertRaises(NonterminalDoesNotExistsException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_invalidNonterminalMultiple(self):
        class tmp(Rule):
            rules = [([TSecond, 'b', TThird], ['c', 2]),
                     ([NFifth], [2, Invalid])]
        with self.assertRaises(NonterminalDoesNotExistsException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))

    def test_invalidNonterminalFromMultiple(self):
        class tmp(Rule):
            rules = [([TSecond, 'b', TThird], ['c', 2]),
                     (['a', Invalid], [2, NFirst])]
        with self.assertRaises(NonterminalDoesNotExistsException):
            tmp.validate(grammar)
        self.assertFalse(tmp.is_valid(grammar))


if __name__ == '__main__':
    main()
