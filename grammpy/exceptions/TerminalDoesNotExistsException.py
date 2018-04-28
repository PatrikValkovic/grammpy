#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 18:15
:Licence GNUv3
Part of grammpy

"""

from .RuleSyntaxException import RuleSyntaxException


class TerminalDoesNotExistsException(RuleSyntaxException):
    """
    Grammar does not exists in grammar provided
    """
    def __init__(self, rule, terminal, grammar):
        super().__init__(rule, 'Terminal does not exists in current grammar')
        self.terminal = terminal
        self.grammar = grammar
