#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 18:15
:Licence GNUv3
Part of grammpy

"""

from .RuleSyntaxException import RuleSyntaxException


class NonterminalDoesNotExistsException(RuleSyntaxException):
    """
    Nonterminal does not exists in provided grammar
    """
    def __init__(self, rule, nonterminal, grammar):
        super().__init__(rule, 'Nonterminal does not exists in current grammar')
        self.nonterminal = nonterminal
        self.grammar = grammar
