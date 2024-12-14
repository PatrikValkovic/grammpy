#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 17.08.207 13:29
:Licence MIT
Part of grammpy

"""
from copy import copy
from typing import TYPE_CHECKING

from ...exceptions import StartSymbolNotSetException

if TYPE_CHECKING:  # pragma: no cover
    from ... import Grammar


def remove_unreachable_symbols(grammar, inplace=False):
    # type: (Grammar, bool) -> Grammar
    """
    Remove unreachable symbols from the grammar.
    :param grammar: Grammar where to remove symbols.
    :param inplace: True if transformation should be performed in place. False by default.
    :return: Grammar without unreachable symbols.
    """
    # copy if required
    if inplace is False:
        grammar = copy(grammar)
    # check if start symbol is set
    if grammar.start is None:
        raise StartSymbolNotSetException()
    # create process sets
    reachable = {grammar.start}
    rules = grammar.rules.copy()
    # begin iterations
    while True:
        # create sets for current iteration
        active = reachable.copy()
        # loop the working rules
        for rule in rules.copy():
            # lf left part of rule already in reachable symbols
            if rule.fromSymbol in reachable:
                # set symbols on the right as reachable
                for symbol in rule.right:
                    active.add(symbol)
                # remove rule from the next iteration
                rules.remove(rule)
            # end of rules loop
        # if current and previous iterations are same, we are done
        if active == reachable:
            break
        # otherwise swap the sets
        reachable = active
    # remove the symbols
    nonterminals_to_remove = grammar.nonterminals.difference(reachable)
    terminals_to_remove = grammar.terminals.difference(reachable)
    grammar.nonterminals.remove(*nonterminals_to_remove)
    grammar.terminals.remove(*terminals_to_remove)
    # return grammar
    return grammar
