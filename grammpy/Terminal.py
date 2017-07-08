#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""


class Terminal:
    '''
    Represent Terminal in former grammar
    '''

    def __init__(self, symbol, grammar):
        '''
        Create new terminal, where symbol is provided terminal passed into grammar
        :param symbol: Symbol representing terminal
        :param grammar: The grammar to which the terminal belongs
        '''
        self.__symbol = symbol
        self.__grammar = grammar

    def __hash__(self):
        '''
        Return hash based on symbol and instance of grammar
        :return: Hash value
        '''
        return hash((self.__symbol, id(self.__grammar)))

    def __eq__(self, other):
        '''
        Compare two terminals based on hash values
        :param other: Terminal to compare
        :type other: Terminal
        :return:
        :rtype bool
        '''
        return isinstance(other, Terminal) and hash(self) == hash(other)

    def symbol(self):
        '''
        Get symbol for the terminal.
        :return: Symbol that represent current terminal
        '''
        return self.__symbol