#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 18:47
:Licence GNUv3
Part of pyparsers

"""

from grammpy import *

"""
    A B C D
    A B C
    A B
    A
"""


class Field:
    def __init__(self, grammar: Grammar, size):
        self._field = [[None for _ in range(k, 0, -1)] for k in range(size, 0, -1)]
        self._termmap = dict()
        self._rulemap = dict()
        for r in grammar.rules():
            if len(r.right) == 1:
                # rule to terminal
                if r.toSymbol not in self._termmap:
                    self._termmap[r.toSymbol] = []
                self._termmap[r.toSymbol].append(r)
            else:
                # rule with nonterms
                key = hash(tuple(r.right))
                if key not in self._rulemap:
                    self._rulemap[key] = []
                self._rulemap[key].append(r)
