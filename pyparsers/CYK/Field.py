#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 18:47
:Licence GNUv3
Part of pyparsers

"""

from grammpy import *

"""

    f[2][1] = I

     x ->
  y  A B C D
  |  E F G
  V  H I
     J
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Field:
    def __init__(self, grammar: Grammar, size):
        self._field = [[[] for _ in range(k, 0, -1)] for k in range(size, 0, -1)]

    def fill(self, term_dict, terms):
        for i in range(len(terms)):
            t = terms[i]
            self._field[0][i] += term_dict[t]

    def nonterms(self, x, y):
        return [r.fromSymbol for r in self._field[y][x]]

    def positions(self, x, y):
        return [(Point(x, v), Point(x+1+v, y-1-v)) for v in range(y)]

    def put(self, x, y, v):
        self._field[y][x] = v