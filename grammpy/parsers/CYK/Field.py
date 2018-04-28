#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 18:47
:Licence GNUv3
Part of pyparsers

"""
from collections import namedtuple

from grammpy import *

"""

    f[2][1] = I

     x ->
  y  A B C D
  |  E F G
  V  H I
     J
"""


class Point(namedtuple('Point', ['x', 'y'])):
    """
    Represent point in 2D space
    """
    pass


class Field:
    """
    Represent structure on which CYK operates
    """

    def __init__(self, size):
        """
        Create structure with specific size
        :param size:
        """
        self._field = [[[] for _ in range(k, 0, -1)] for k in range(size, 0, -1)]

    def fill(self, term_dict, terms):
        """
        Fill first row of the structure witch nonterminal directly rewritable to terminal
        :param term_dict: Dictionary of rules directly rewritable to terminal.
        Key is hash of terminal, value is list of rules with key terminal at the right side.
        :param terms: Input sequence of terminal
        """
        for i in range(len(terms)):
            t = terms[i]
            self._field[0][i] += term_dict[hash(t)]

    def rules(self, x, y):
        """
        Get rules at specific position in the structure
        :param x: X coordinate
        :param y: Y coordinate
        :return: List of rules
        """
        return [r for r in self._field[y][x]]

    def positions(self, x, y):
        """
        Get all positions, that can be combined to get word parsed at specified position
        :param x: X coordinate
        :param y: Y coordinate
        :return: List of tuples with two Point instances
        """
        return [(Point(x, v), Point(x + 1 + v, y - 1 - v)) for v in range(y)]

    def put(self, x, y, v):
        """
        Set possible rules at specific position
        :param x: X coordinate
        :param y: Y coordinate
        :param v: Value to set
        """
        self._field[y][x] = v
