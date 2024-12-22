#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 19.03.2019 15:39
:Licence MIT
Part of grammpy

"""
from grammpy import *
from grammpy.transforms import ContextFree, InverseContextFree, InverseCommon
from grammpy.parsers import cyk


# Terminals
class PlusOperator(Terminal): pass
class MinusOperator(Terminal): pass
class MultipleOperator(Terminal): pass
class DivideOperator(Terminal): pass
class LeftBracket(Terminal): pass
class RightBracket(Terminal): pass


# Nonterminals
class Common(Nonterminal):
    def __init__(self):
        super().__init__()
        self._attribute = None
    @property
    def attribute(self):
        if self._attribute is None:
            self.to_rule.compute()
        return self._attribute
    @attribute.setter
    def attribute(self, value):
        self._attribute = value


class Number(Common): pass
class MultipleDivide(Common): pass
class PlusMinus(Common): pass


# Rules
class NumberDirect(Rule):
    rules = [([Number], [0]),
             ([Number], [1]),
             ([Number], [2]),
             ([Number], [3]),
             ([Number], [4]),
             ([Number], [5]),
             ([Number], [6]),
             ([Number], [7]),
             ([Number], [8]),
             ([Number], [9])]
    def compute(self):
        self._from_symbols[0].attribute = self._to_symbols[0].s

class NumberCompute(Rule):
    rules = [([Number], [Number, 0]),
             ([Number], [Number, 1]),
             ([Number], [Number, 2]),
             ([Number], [Number, 3]),
             ([Number], [Number, 4]),
             ([Number], [Number, 5]),
             ([Number], [Number, 6]),
             ([Number], [Number, 7]),
             ([Number], [Number, 8]),
             ([Number], [Number, 9])]
    def compute(self):
        self._from_symbols[0].attribute = self._to_symbols[0].attribute * 10 + self._to_symbols[1].s

class MultipleApplied(Rule):
    fromSymbol = MultipleDivide
    right = [MultipleDivide, MultipleOperator, Number]
    def compute(self):
        self._from_symbols[0].attribute = self._to_symbols[0].attribute * self._to_symbols[2].attribute

class DivideApplied(Rule):
    fromSymbol = MultipleDivide
    right = [MultipleDivide, DivideOperator, Number]
    def compute(self):
        self._from_symbols[0].attribute = self._to_symbols[0].attribute / self._to_symbols[2].attribute

class NoDivideMultiple(Rule):
    fromSymbol = MultipleDivide
    toSymbol = Number
    def compute(self):
        self._from_symbols[0].attribute = self._to_symbols[0].attribute

class PlusApplied(Rule):
    fromSymbol = PlusMinus
    right = [PlusMinus, PlusOperator, MultipleDivide]
    def compute(self):
        self._from_symbols[0].attribute = self._to_symbols[0].attribute + self._to_symbols[2].attribute

class MinusApplied(Rule):
    fromSymbol = PlusMinus
    right = [PlusMinus, MinusOperator, MultipleDivide]
    def compute(self):
        self._from_symbols[0].attribute = self._to_symbols[0].attribute - self._to_symbols[2].attribute

class NoPlusMinus(Rule):
    fromSymbol = PlusMinus
    toSymbol = MultipleDivide
    def compute(self):
        self._from_symbols[0].attribute = self._to_symbols[0].attribute

class BracketsApplied(Rule):
    fromSymbol = Number
    right = [LeftBracket, PlusMinus, RightBracket]
    def compute(self):
        self._from_symbols[0].attribute = self._to_symbols[1].attribute


g = Grammar(terminals=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                       PlusOperator, MinusOperator, MultipleOperator, DivideOperator,
                       LeftBracket, RightBracket],
            nonterminals=[Number, MultipleDivide, PlusMinus],
            rules=[NumberDirect, NumberCompute,
                   DivideApplied, MultipleApplied, NoDivideMultiple,
                   MinusApplied, PlusApplied, NoPlusMinus,
                   BracketsApplied],
            start_symbol=PlusMinus)

if __name__ == '__main__':
    g = ContextFree.prepare_for_cyk(g, inplace=True)

    root = cyk(g, [1, 0, PlusOperator,
                   LeftBracket, 5, MultipleOperator, 2, PlusOperator, 4, RightBracket,
                   DivideOperator, 2, MultipleOperator, 4])

    root = InverseContextFree.reverse_cyk_transforms(root)
    root = InverseCommon.splitted_rules(root)

    print(root.attribute)
