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

def _all_combinations(tpl):
    for f in tpl[0]:
        for s in tpl[1]:
            yield (f, s)

class _place_item:
    def __init__(self, r, t1, t2):
        self.to_rule = [t1, t2]
        self.rule = r

    def __hash__(self):
        return hash(self.rule)

    @property
    def fromSymbol(self):
        return self.rule.fromSymbol



def cyk(grammar: Grammar, input: Iterable) -> Nonterminal:
    i = list(input)
    l = len(i)
    f = Field(grammar, l)
    # creating mapping for speedup rules searching
    (termmap, rulemap) = _create_mapping(grammar)
    # fill first line with rules directly rewritable to terminal
    f.fill(termmap, i)
    # fill rest of field
    for y in range(1, l):
        for x in range(l - y):
            positions = f.positions(x, y)
            pairs_of_rules = [(f.rules(pos[0].x, pos[0].y),
                      f.rules(pos[1].x, pos[1].y))
                     for pos in positions]
            rules = set()
            for pair_of_rule in pairs_of_rules:
                for (first_rule, second_rule) in _all_combinations(pair_of_rule):
                    h = hash((first_rule.fromSymbol, second_rule.fromSymbol))
                    if h in rulemap:
                        for r in rulemap[h]: # list of rules
                            rules.add(_place_item(r, first_rule, second_rule))
            f.put(x, y, list(rules))
    # Check if is start symol on the bottom of field
    if grammar.start_get() not in [r.fromSymbol for r in f.rules(0,l-1)]:
        raise NotImplementedError() # TODO exception
    # Find init symbol and rule
    start = grammar.start_get()()  # type: Nonterminal
    start_rule = [r for r in f.rules(0, l-1) if grammar.start_is(r.fromSymbol)][0]
    # Prepare buffer for proccess
    to_process = list()
    to_process.append({'n': start, 'r': start_rule})
    # Prepare tree
    while len(to_process) > 0:
        working = to_process.pop()
        rule_class = working['r']
        working_nonterm = working['n']  # type: Nonterminal
        # it middle rule - not rewritable to nonterminal
        if isinstance(rule_class, _place_item):
            created_rule = rule_class.rule() # type: Rule
            working_nonterm._set_to_rule(created_rule)
            created_rule._from_symbols.append(working_nonterm)
            for side in rule_class.to_rule:
                symbol = side.fromSymbol() # type: Nonterminal
                symbol._set_from_rule(created_rule)
                created_rule._to_symbols.append(symbol)
                to_process.append({'n': symbol, 'r': side})
        # it is rule rewritable to nonterminal
        else:
            created_rule = rule_class() # type: Rule
            working_nonterm._set_to_rule(created_rule)
            t = grammar.term(rule_class.toSymbol)
            created_rule._to_symbols = [t]
            t._set_from_rule(created_rule)
    return start
