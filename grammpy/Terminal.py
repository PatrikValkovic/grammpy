#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""


class Terminal:

    def __init__(self, symbol, grammar):
        self.__symbol = symbol
        self.__grammar = grammar

    def __hash__(self):
        return hash((self.__symbol, id(self.__grammar)))

    def __eq__(self, other):
        return isinstance(other, Terminal) and hash(self) == hash(other)

    def symbol(self):
        return self.__symbol
