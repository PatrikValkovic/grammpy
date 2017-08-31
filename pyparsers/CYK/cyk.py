#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 14:47
:Licence GNUv3
Part of pyparsers

"""

from typing import Iterable

import itertools
from grammpy import *
from .Field import Field


def _create_mapping(grammar: Grammar) -> tuple:
    termmap = dict()
    rulemap = dict()
    for r in grammar.rules():
        if len(r.right) == 1:
            # rule to terminal
            if r.toSymbol not in termmap:
                termmap[r.toSymbol] = set()
            termmap[r.toSymbol].add(r)
        else:
            # rule with nonterms
            key = hash(tuple(r.right))
            if key not in rulemap:
                rulemap[key] = set()
            rulemap[key].add(r)
    return (termmap, rulemap)

def _all_combinations(first, second):
    for f in first:
        for s in second:
            yield (f, s)

def cyk(grammar: Grammar, input: Iterable) -> Nonterminal:
    i = list(input)
    f = Field(grammar, len(i))
    # creating mapping for speedup rules searching
    (termmap, rulemap) = _create_mapping(grammar)
    # fill first line with rules directly rewritable to terminal
    f.fill(termmap, i)
    # fill rest of field
    for y in range(1, len(i)):
        for x in range(len(i) - y):
            positions = f.positions(x, y)
            pairs = [(f.nonterms(pos[0].x, pos[0].y),
                      f.nonterms(pos[1].x, pos[1].y))
                     for pos in positions]
            r = set()
            for pair in pairs:
                for (first, second) in _all_combinations(pair[0], pair[1]):
                    h = hash((first, second))
                    if h in rulemap: r |= rulemap[h]
            f.put(x, y, list(r))
    raise NotImplementedError()
