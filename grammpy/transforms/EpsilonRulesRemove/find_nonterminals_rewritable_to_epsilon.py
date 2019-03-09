#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.08.2017 15:42
:Licence GNUv3
Part of grammpy

"""
from typing import TYPE_CHECKING, Dict, Type, Optional

from ... import EPSILON

if TYPE_CHECKING:  # pragma: no cover
    from ... import Grammar, Nonterminal, Rule


def find_nonterminals_rewritable_to_epsilon(grammar):
    # type: (Grammar) -> Dict[Type[Nonterminal], Type[Rule]]
    """
    Get nonterminals rewritable to epsilon.
    :param grammar: Grammar where to search.
    :return: Dictionary, where key is nonterminal rewritable to epsilon and value is rule that is responsible for it.
    """
    # start with empty dictionary (contains only epsilon)
    rewritable = dict()  # type: Dict[Type[Nonterminal], Optional[Type[Rule]]]
    rewritable[EPSILON] = None
    # iterate until the dictionary change
    while True:
        working = rewritable.copy()
        for rule in grammar.rules:
            # no need to process rules we already know rewrite to epsilon
            if rule.fromSymbol in working:
                continue
            # check if the whole right side rewrite to epsilon
            right_side_rewrite = True
            for symbol in rule.right:
                if symbol not in rewritable:
                    right_side_rewrite = False
            # the whole right side can be reduce to epsilon, add left side to dictionary
            if right_side_rewrite:
                working[rule.fromSymbol] = rule
        # Working set didn't change, we are done
        if working == rewritable:
            break
        # Otherwise swap the sets and iterate
        rewritable = working
    # delete epsilon from the dictionary
    del rewritable[EPSILON]
    return rewritable
