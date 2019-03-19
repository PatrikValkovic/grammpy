#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 22.08.2017 11:37
:Licence MIT
Part of grammpy

"""
from copy import copy
from typing import TYPE_CHECKING, List, Type

from ._support import _is_unit
from .find_symbols_reachable_by_unit_rules import find_nonterminals_reachable_by_unit_rules
from ... import Rule

if TYPE_CHECKING:  # pragma: no cover
    from ... import Grammar


class ReducedUnitRule(Rule):
    """
    Represent rule that replace sequence of unit rules (with the last rule that generates something)
    with single rule.
    The sequence of applied rules is in the `by_rules` property.
    The last, generating rule is in the `end_rule` property.
    """
    by_rules = []  # type: List[Type[Rule]]
    end_rule = None  # type: Type[Rule]


def _create_rule(path, rule):
    # type: (List[Type[Rule]], Type[Rule]) -> Type[ReducedUnitRule]
    """
    Create ReducedUnitRule based on sequence of unit rules and end, generating rule.
    :param path: Sequence of unit rules.
    :param rule: Rule that is attached after sequence of unit rules.
    :return: ReducedUnitRule class.
    """
    created = type('Reduced[' + rule.__name__ + ']',
                   (ReducedUnitRule,),
                   ReducedUnitRule.__dict__.copy())  # type: Type[ReducedUnitRule]
    created.rule = ([path[0].fromSymbol], rule.right)
    created.end_rule = rule
    created.by_rules = path
    return created


def remove_unit_rules(grammar, inplace=False):
    # type: (Grammar, bool) -> Grammar
    """
    Remove unit rules from the grammar.
    :param grammar: Grammar where remove the rules.
    :param inplace: True if transformation should be performed in place. False by default.
    :return: Grammar without unit rules.
    """
    # copy if needed
    if inplace is False:
        grammar = copy(grammar)
    # get connections
    res = find_nonterminals_reachable_by_unit_rules(grammar)
    # iterate through rules
    for rule in grammar.rules.copy():
        # delete unit rules
        if _is_unit(rule):
            grammar.rules.remove(rule)
            continue
        for nonterm in grammar.nonterminals:
            # find all nonterminals that can rewrite to current rule
            path = res.path_rules(nonterm, rule.fromSymbol)
            # get rid of cyclic paths
            if len(path) > 0 and path[0].fromSymbol != path[-1].toSymbol:
                created = _create_rule(path, rule)
                grammar.rules.add(created)
    return grammar
