#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 16:08
:Licence GNUv3
Part of grammpy

"""

from inspect import isclass

from grammpy.exceptions import RuleException, UselessEpsilonException, RuleSyntaxException, \
    TerminalDoesNotExistsException, \
    NonterminalDoesNotExistsException
from grammpy import EPS
from grammpy import Nonterminal
from .BaseRule import BaseRule


class ValidationRule(BaseRule):
    @staticmethod
    def _controlSide(cls, side, grammar):
        if not isinstance(side, list):
            raise RuleSyntaxException(cls, 'One side of rule is not enclose by list', side)
        if len(side) == 0:
            raise RuleSyntaxException(cls, 'One side of rule is not define', side)
        if EPS in side and len(side) > 1:
            raise UselessEpsilonException(cls)
        for symb in side:
            if isclass(symb) and issubclass(symb, Nonterminal):
                if not grammar.have_nonterm(symb):
                    raise NonterminalDoesNotExistsException(cls, symb, grammar)
            elif symb is EPS:
                continue
            elif not grammar.have_term(symb):
                raise TerminalDoesNotExistsException(cls, symb, grammar)

    @classmethod
    def validate(cls, grammar):
        r = cls.rules
        if not isinstance(r, list):
            raise RuleSyntaxException(cls, 'Rules property is not enclose in list')
        for rule in r:
            if not isinstance(rule, tuple):
                raise RuleSyntaxException(cls, 'One of the rules is not enclose in tuple', rule)
            if len(rule) != 2:
                raise RuleSyntaxException(cls, 'One of the rules does not have define left and right part', rule)
            l = rule[0]
            r = rule[1]
            ValidationRule._controlSide(cls, l, grammar)
            ValidationRule._controlSide(cls, r, grammar)
            if l == [EPS] and r == [EPS]:
                raise UselessEpsilonException(cls)

    @classmethod
    def is_valid(cls, grammar):
        try:
            cls.validate(grammar)
            return True
        except RuleException:
            return False
