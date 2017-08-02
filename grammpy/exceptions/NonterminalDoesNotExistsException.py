#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .RuleSyntaxException import RuleSyntaxException


class NonterminalDoesNotExistsException(RuleSyntaxException):
    def __init__(self, rule, nonterminal, grammar):
        super().__init__(rule, 'Nonterminal does not exists in current grammar')
        self.nonterminal = nonterminal
        self.grammar = grammar
