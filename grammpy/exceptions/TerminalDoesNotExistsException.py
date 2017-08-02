#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .RuleSyntaxException import RuleSyntaxException


class TerminalDoesNotExistsException(RuleSyntaxException):
    def __init__(self, rule, terminal, grammar):
        super().__init__(rule, 'Terminal does not exists in current grammar')
        self.terminal = terminal
        self.grammar = grammar
