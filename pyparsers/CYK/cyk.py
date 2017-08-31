#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 14:47
:Licence GNUv3
Part of pyparsers

"""

from typing import Iterable
from grammpy import *
from .Field import Field

def _create_mapping(grammar: Grammar) -> tuple:
    termmap = dict()
    rulemap = dict()
    for r in grammar.rules():
        if len(r.right) == 1:
            # rule to terminal
            if r.toSymbol not in termmap:
                termmap[r.toSymbol] = []
            termmap[r.toSymbol].append(r)
        else:
            # rule with nonterms
            key = hash(tuple(r.right))
            if key not in rulemap:
                rulemap[key] = []
            rulemap[key].append(r)
    return (termmap, rulemap)


def cyk(grammar: Grammar, input: Iterable) -> Nonterminal:
    i = list(input)
    f = Field(grammar, len(i))
    (termmap, rulemap) = _create_mapping(grammar)
    raise NotImplementedError()