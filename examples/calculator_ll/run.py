#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 19.03.2019 15:39
:Licence MIT
Part of grammpy

"""
import os
import pickle
from grammpy import *
from grammpy.transforms import ContextFree
from grammpy.parsers import ll, create_ll_parsing_table


# Terminals
class PlusOperator(Terminal): pass
class MinusOperator(Terminal): pass
class MultipleOperator(Terminal): pass
class DivideOperator(Terminal): pass
class LeftBracket(Terminal): pass
class RightBracket(Terminal): pass

class NumberTerminal(Terminal):
    def __init__(self, s):
        super().__init__(s)

    def __hash__(self):
        return hash(NumberTerminal)


# Nonterminals
class Common(Nonterminal):
    def __init__(self):
        self._value = None

    @property
    def value(self):
        if self._value is None:
            self.to_rule.compute()
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

class E(Common): pass
class Ecap(Common): pass
class T(Common): pass
class Tcap(Common): pass
class F(Common): pass


# Rules
class RuleE(Rule):
    rule = ([E], [T, Ecap])

    def compute(self):
        left = self.to_symbols[0].value
        result = self.to_symbols[1].to_rule.compute(left)
        self.from_symbols[0].value = result


class RuleEcapPlus(Rule):
    rule = ([Ecap], [PlusOperator, T, Ecap])

    def compute(self, left_side):
        me = self.to_symbols[1].value
        tmp = left_side + me
        result = self.to_symbols[2].to_rule.compute(tmp)
        self.from_symbols[0].value = result
        return result


class RuleEcapMinus(Rule):
    rule = ([Ecap], [MinusOperator, T, Ecap])

    def compute(self, left_side):
        me = self.to_symbols[1].value
        tmp = left_side - me
        result = self.to_symbols[2].to_rule.compute(tmp)
        self.from_symbols[0].value = result
        return result


class RuleEcapEps(Rule):
    rule = ([Ecap], [EPSILON])

    def compute(self, left_side):
        self.from_symbols[0].value = left_side
        return left_side


class RuleT(Rule):
    rule = ([T], [F, Tcap])

    def compute(self):
        left = self.to_symbols[0].value
        result = self.to_symbols[1].to_rule.compute(left)
        self.from_symbols[0].value = result


class RuleTcapTimes(Rule):
    rule = ([Tcap], [MultipleOperator, F, Tcap])

    def compute(self, left_side):
        me = self.to_symbols[1].value
        tmp = left_side * me
        result = self.to_symbols[2].to_rule.compute(tmp)
        self.from_symbols[0].value = result
        return result


class RuleTcapDivide(Rule):
    rule = ([Tcap], [DivideOperator, F, Tcap])

    def compute(self, left_side):
        me = self.to_symbols[1].value
        tmp = left_side / me
        result = self.to_symbols[2].to_rule.compute(tmp)
        self.from_symbols[0].value = result
        return result


class RuleTcapEps(Rule):
    rule = ([Tcap], [EPSILON])

    def compute(self, left_side):
        self.from_symbols[0].value = left_side
        return left_side


class RuleNum(Rule):
    rule = ([F], [NumberTerminal])

    def compute(self):
        self.from_symbols[0].value = self.to_symbols[0].s


class RuleBrackets(Rule):
    rule = ([F], [LeftBracket, E, RightBracket])

    def compute(self):
        self.from_symbols[0].value = self.to_symbols[1].value


g = Grammar(terminals=[NumberTerminal, PlusOperator, MinusOperator, MultipleOperator, DivideOperator, LeftBracket,
                       RightBracket],
            nonterminals=[E, Ecap, T, Tcap, F],
            rules=[RuleE, RuleEcapPlus, RuleEcapMinus, RuleEcapEps, RuleT, RuleTcapTimes, RuleTcapDivide, RuleTcapEps,
                   RuleNum, RuleBrackets],
            start_symbol=E)

if __name__ == '__main__':
    if not os.path.exists('cache.pckl'):
        first_table = ContextFree.create_first_table(g, 1)
        follow_table = ContextFree.create_follow_table(g, first_table, 1)
        parsing_table = create_ll_parsing_table(g, first_table, follow_table, 1)
        with open('cache.pckl', 'wb') as f:
            pickle.dump(parsing_table, f)
    else:
        with open('cache.pckl', 'rb') as f:
            parsing_table = pickle.load(f)

    root = ll(g.start, [
        NumberTerminal(10),
        PlusOperator,
        LeftBracket,
        NumberTerminal(5),
        MultipleOperator,
        NumberTerminal(2),
        MinusOperator,
        NumberTerminal(4),
        RightBracket,
        DivideOperator,
        NumberTerminal(2),
        MultipleOperator,
        NumberTerminal(4)
    ], parsing_table, 1)

    print(root.value)
