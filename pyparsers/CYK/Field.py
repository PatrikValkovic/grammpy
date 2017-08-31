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


class Field:
    def __init__(self, grammar: Grammar, size):
        self._field = [[[] for _ in range(k, 0, -1)] for k in range(size, 0, -1)]

    def nonterms(self, x, y):
        return [r.rule for r in self._field[y][x]]
