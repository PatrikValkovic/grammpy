#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 20:33
:Licence GNUv3
Part of grammpy

"""
from copy import copy
from typing import TYPE_CHECKING

from ... import EPSILON

if TYPE_CHECKING:  # pragma: no cover
    from ... import Grammar


def remove_nongenerating_nonterminals(grammar, inplace=False):
    # type: (Grammar, bool) -> Grammar
    """
    Remove nongenerating symbols from the grammar.
    Nongenerating symbols are symbols, that don't generate sequence of terminals.
    For example never ending recursion.
    :param grammar: Grammar where to remove nongenerating symbols.
    :param inplace: True if transformation should be performed in place. False by default.
    :return: Grammar without nongenerating symbols.
    """
    # copy if required
    if inplace is False:
        grammar = copy(grammar)
    # create working sets
    generates = grammar.terminals.copy()
    generates.add(EPSILON)
    rules = grammar.rules.copy()
    # iterate until the set doesn't change
    while True:
        # create set for the next iteration
        additional = generates.copy()
        # iterate over unprocessed rules
        for rule in rules.copy():
            rightPart = rule.right
            allIn = True
            # check if all symbols on the right part of rule are in generates set
            for symbol in rightPart:
                if symbol not in generates:
                    allIn = False
                    break
            # Symbol is missing so rule is not process
            if not allIn:
                continue
            # Rule is process - remove it from processing rules and make symbol as generating
            additional.add(rule.fromSymbol)
            rules.remove(rule)
            # end of rules iterations
        # ff current and previous iterations are same, than end iterations
        if additional == generates:
            break
        # swap sets from previous and current iterations
        generates = additional
    # remove nonterms that are not generating
    nongenerating = grammar.nonterminals.difference(generates)
    grammar.nonterminals.remove(*nongenerating)
    # return the grammar
    return grammar
