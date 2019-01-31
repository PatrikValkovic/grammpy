#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.07.2017 19:45
:Licence GNUv3
Part of grammpy

"""
from typing import Any

from .support._RuleConnectable import _RuleConnectable


class Terminal(_RuleConnectable):
    '''
    Represent Terminal in formal grammar.
    '''

    def __init__(self, symbol):
        # type: (Any) -> Terminal
        '''
        Create new terminal.
        :param symbol: Symbol representing terminal.
        :param grammar: The grammar to which the terminal belongs
        TODO remove reference to grammar.
        '''
        super().__init__()
        self.__symbol = symbol

    def __hash__(self):
        # type: () -> int
        '''
        Return hash based on symbol (symbol's hash).
        :return: Hash value of the terminal.
        '''
        return hash(self.__symbol)

    def __eq__(self, other):
        # type: (Any) -> bool
        '''
        Compare two terminals based on hash values.
        :param other: Terminal to compare.
        :return: True if objects are equal, false otherwise.
        '''
        return hash(self) == hash(other)

    def symbol(self):
        # type: () -> Any
        '''
        Get symbol for the terminal.
        :return: Symbol that represent current terminal.
        '''
        return self.__symbol

    @property
    def s(self):
        # type: () -> Any
        """
        Shortcut for symbol method.
        :return: Symbol that represent current terminal.
        """
        return self.symbol()
