#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 20.08.2017 15:43
:Licence MIT
Part of grammpy

"""
from copy import copy
from queue import Queue
from typing import TYPE_CHECKING, Type, Dict

from .find_nonterminals_rewritable_to_epsilon import find_nonterminals_rewritable_to_epsilon
from ... import Rule, EPSILON

if TYPE_CHECKING:  # pragma: no cover
    from ... import Grammar, Nonterminal


class EpsilonRemovedRule(Rule):
    """
    Replace rule, when one symbol of the original rule is rewritable to epsilon.
    The new Rule contains original rule in `from_rule` field,
    index of the nonterminal rewritable to epsilon at `replace_index` field and
    series of rules ending the epsilon in `backtrack` field.
    """
    from_rule = None  # type: Type[Rule]
    replace_index = None  # type: int
    backtrack = None  # type: Dict[Type[Nonterminal], Type[Rule]]


def _create_rule(rule, index, backtrack):
    # type: (Rule, int, Dict[Type[Nonterminal], Type[Rule]]) -> Type[EpsilonRemovedRule]
    """
    Create EpsilonRemovedRule. This rule will skip symbol at the `index`.
    :param rule: Original rule.
    :param index: Index of symbol that is rewritable to epsilon.
    :param backtrack: Dictionary where key is nonterminal and value is rule which is next to generate epsilon.
    :return: EpsilonRemovedRule class without symbol rewritable to epsilon.
    """
    # remove old rules from the dictionary
    old_dict = rule.__dict__.copy()
    if 'rules' in old_dict: del old_dict['rules']
    if 'rule' in old_dict: del old_dict['rule']
    if 'left' in old_dict: del old_dict['left']
    if 'right' in old_dict: del old_dict['right']
    if 'fromSymbol' in old_dict: del old_dict['fromSymbol']
    if 'toSymbol' in old_dict: del old_dict['toSymbol']
    # create type
    created = type('NoEps[' + rule.__name__ + ']',
                   (EpsilonRemovedRule,),
                   old_dict)  # type: Type[EpsilonRemovedRule]
    # add from_rule and index
    created.from_rule = rule
    created.replace_index = index
    created.backtrack = backtrack
    # attach rule
    created.fromSymbol = rule.fromSymbol
    created.right = [rule.right[i] for i in range(len(rule.right)) if i != index]
    # ff the right side is empty
    if len(created.right) == 0:
        created.right = [EPSILON]
    return created


def remove_rules_with_epsilon(grammar, inplace=False):
    # type: (Grammar, bool) -> Grammar
    """
    Remove epsilon rules.
    :param grammar: Grammar where rules remove
    :param inplace: True if transformation should be performed in place, false otherwise.
    False by default.
    :return: Grammar without epsilon rules.
    """
    # copy if required
    if inplace is False:
        grammar = copy(grammar)
    # find nonterminals rewritable to epsilon
    rewritable = find_nonterminals_rewritable_to_epsilon(grammar)  # type: Dict[Type[Nonterminal], Type[Rule]]
    # create queue from rules to iterate over
    rules = Queue()
    for r in grammar.rules:
        rules.put(r)
    # iterate thought rules
    while not rules.empty():
        rule = rules.get()
        right = rule.right
        # if the rule rewrite to epsilon we can safely delete it
        if right == [EPSILON]:
            # unless it rewrites from the start symbol
            if rule.fromSymbol != grammar.start:
                grammar.rules.discard(rule)
            # continue IS executed, but due optimization line is marked as missed.
            continue  # pragma: no cover
        # iterate over the right side
        for rule_index in range(len(right)):
            symbol = right[rule_index]
            # if symbol is rewritable, generate new rule without that symbol
            if symbol in rewritable:
                new_rule = _create_rule(rule, rule_index, rewritable)
                grammar.rules.add(new_rule)
                rules.put(new_rule)  # in case there are more rewritable symbols
    return grammar
