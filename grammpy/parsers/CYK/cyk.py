#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 14:47
:Licence GNUv3
Part of grammpy

"""

from typing import Iterable, TYPE_CHECKING, Generator, Any, Dict, Set, Type

from .Field import Field
from .PlaceItem import PlaceItem
from ... import *
from ...exceptions import NotParsedException, StartSymbolNotSetException

if TYPE_CHECKING:  # pragma: no cover
    from ... import Grammar


def _create_mapping(grammar):
    # type: (Grammar) -> (Dict[int, Set[Type[Rule]]], Dict[int, Set[Type[Rule]]])
    """
    Create mapping between symbols and rules rewritable to these symbols.
    :param grammar: Grammar to use.
    :return: Tuple of two dictionaries.
    First dictionary maps rule to terminal hash.
    Second dictionary maps rule to nonterminals hash.
    """
    termmap = dict()
    rulemap = dict()
    for r in grammar.rules:
        if len(r.right) == 1:
            # rule to terminal
            h = hash(r.toSymbol)
            if h not in termmap:
                termmap[h] = set()
            termmap[h].add(r)
        else:
            # rule to two nonterms
            key = hash(tuple(r.right))
            if key not in rulemap:
                rulemap[key] = set()
            rulemap[key].add(r)
    return (termmap, rulemap)

def _all_combinations(tpl):
    # type: ((Iterable, Iterable)) -> Generator[tuple]
    """
    Return all combinations of iterables passed as a parameter.
    :param tpl: Tuple of two iterable.
    :return: Generator of tuples.
    """
    for f in tpl[0]:
        for s in tpl[1]:
            yield (f, s)


def cyk(grammar, parse_sequence):
    # type: (Grammar, Iterable[Any]) -> Nonterminal
    """
    Perform CYK algorithm.
    :param grammar: Grammar to use in Chomsky Normal Form.
    :param parse_sequence: Input sequence to parse.
    :return: Instance of root Nonterminal in parsed tree.
    """
    # check start symbol
    if grammar.start is None:
        raise StartSymbolNotSetException()
    # create variables
    parse_sequence = list(parse_sequence)
    input_length = len(parse_sequence)
    index = input_length - 1
    f = Field(input_length)
    # creating mapping for speedup rules searching
    (termmap, rulemap) = _create_mapping(grammar)
    # fill first line with rules directly rewritable to terminal
    f.fill(termmap, parse_sequence)
    # fill rest of fields
    for y in range(1, input_length):
        for x in range(input_length - y):
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
                            rules.add(PlaceItem(r, first_rule, second_rule))
            f.put(x, y, list(rules))
    # Check if is start symol on the bottom of field
    if grammar.start not in [r.fromSymbol for r in f.rules(0, input_length - 1)]:
        raise NotParsedException()
    # Find init symbol and rule
    start = grammar.start()  # type: Nonterminal
    start_rule = [r for r in f.rules(0, input_length - 1) if grammar.start == r.fromSymbol][0]
    # Prepare buffer for proccess
    to_process = list()
    to_process.append({'n': start, 'r': start_rule})
    # Prepare tree
    while len(to_process) > 0:
        working = to_process.pop()
        rule_class = working['r']
        working_nonterm = working['n']  # type: Nonterminal
        # its middle rule - not rewritable to nonterminal
        if isinstance(rule_class, PlaceItem):
            created_rule = rule_class.rule()  # type: Rule
            working_nonterm._set_to_rule(created_rule)
            created_rule._from_symbols.append(working_nonterm)
            for side in rule_class.to_rule:
                symbol = side.fromSymbol()  # type: Nonterminal
                symbol._set_from_rule(created_rule)
                created_rule._to_symbols.append(symbol)
                to_process.append({'n': symbol, 'r': side})
        # it is rule rewritable to nonterminal
        else:
            created_rule = rule_class()  # type: Rule
            working_nonterm._set_to_rule(created_rule)
            created_rule._from_symbols.append(working_nonterm)
            t = Terminal(parse_sequence[index])
            index -= 1
            created_rule._to_symbols.append(t)
            t._set_from_rule(created_rule)
    return start
