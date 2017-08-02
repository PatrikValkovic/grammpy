#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .Rule import Rule
from .exceptions import RuleException, UselessEpsilonException, RuleSyntaxException, TerminalDoesNotExistsException, \
    NonterminalDoesNotExistsException
from .Constants import EPS
from .Nonterminal import Nonterminal
from . import Grammar


class IsMethodsRuleExtension(Rule):
    @classmethod
    def is_regular(cls):
        raise NotImplementedError()

    @classmethod
    def is_contextfree(cls):
        raise NotImplementedError()

    @classmethod
    def is_context(cls):
        raise NotImplementedError()

    @classmethod
    def is_unrestricted(cls):
        raise NotImplementedError()

    @staticmethod
    def _controlSide(cls, side, grammar: Grammar):
        if not isinstance(side, list):
            raise RuleSyntaxException(cls, 'One side of rule is not enclose by list', side)
        if len(side) == 0:
            raise RuleSyntaxException(cls, 'One side of rule is not define', side)
        if EPS in side and len(side) > 1:
            raise UselessEpsilonException(cls)
        for symb in side:
            if issubclass(symb, Nonterminal):
                if not grammar.have_nonterm(symb):
                    raise NonterminalDoesNotExistsException(cls, symb, grammar)
            elif symb is EPS:
                continue
            elif not grammar.have_term(symb):
                raise TerminalDoesNotExistsException(cls, symb, grammar)
            else:
                raise RuleSyntaxException(cls, 'Could not specify symbol type', symb)

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
            IsMethodsRuleExtension._controlSide(cls, l, grammar)
            IsMethodsRuleExtension._controlSide(cls, r, grammar)

    @classmethod
    def is_valid(cls, grammar):
        try:
            cls.validate(grammar)
            return True
        except RuleException:
            return False
