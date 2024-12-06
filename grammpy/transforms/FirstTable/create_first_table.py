#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.12.2024 17:56
:Licence MIT
Part of grammpy

"""
from inspect import isclass
from typing import TYPE_CHECKING, Dict, List, Set, Union, Type, Tuple
from grammpy import Nonterminal, Terminal, EPSILON
if TYPE_CHECKING:  # pragma: no cover
    from grammpy import Grammar, EPSILON_TYPE
    FirstTableTypeValue = Set[Union[EPSILON_TYPE, List[Union[Type[Terminal], Terminal]]]]
    FirstTableType = Dict[
        Union[Type[Nonterminal]],
        FirstTableTypeValue
    ]

def create_first_table(grammar, look_head):
    # type: (Grammar, int) -> FirstTableType
    """
    Given LL(n) grammar creates first table
    :param grammar: Grammar to create first table for
    :param look_head: Number of symbols to look ahead
    :return: First table
    """
    if type(look_head) != int:
        raise TypeError('Look ahead must be integer')
    if look_head < 1:
        raise ValueError('Look ahead must be at least 1')

    table = {nt: set() for nt in grammar.nonterminals}  # type: FirstTableType

    updated = True
    while updated:
        updated = False
        for rule in grammar.rules:
            from_symbol = rule.fromSymbol  # type: Type[Nonterminal]
            to_symbols = rule.right  # type: List[Union[Type[Terminal], Terminal, EPSILON_TYPE, Type[Nonterminal]]]

            def add_to_table(current_firsts):
                nonlocal updated
                # Add generated sequences to the FIRST set of `from_symbol`
                original_size = len(table[from_symbol])
                if current_firsts == EPSILON:
                    table[from_symbol].add(current_firsts)
                else:
                    table[from_symbol].add(tuple(current_firsts[:look_head]))
                if len(table[from_symbol]) > original_size:
                    updated = True

            def add_to_table_set(current_firsts):
                for current_first in current_firsts:
                    add_to_table(current_first)

            def iterate_rule(current_firsts, to_look, contains_epsilon_prefix):
                # type: (Set[Tuple], List, bool) -> None

                # If some prefix is long enough, add it to the table and ignore it for further processing
                long_enough_current_firsts = [c for c in current_firsts if len(c) >= look_head]
                for current in long_enough_current_firsts:
                    add_to_table(current)
                # Focus only on short prefixes
                current_firsts = set([c for c in current_firsts if len(c) < look_head])
                # If there is nothing to look at, add the current FIRST set to the table
                if len(to_look) == 0:
                    if contains_epsilon_prefix:
                        add_to_table(EPSILON)
                    add_to_table_set(current_firsts)
                    return
                symbol = to_look[0]

                # Right side is epsilon, skip it and look at next symbol
                if symbol == EPSILON:
                    return iterate_rule(current_firsts, to_look[1:], contains_epsilon_prefix)
                # Right side has terminal, add it to the FIRST set
                elif not isclass(symbol) or not issubclass(symbol, Nonterminal):
                    new_first = set(
                        [tuple([*c, symbol]) for c in current_firsts] +
                        ([tuple([symbol])] if contains_epsilon_prefix else []) # If there is epsilon prefix, FIRST may start with the symbol
                    )
                    return iterate_rule(new_first, to_look[1:], False)
                # Right side has nonterminal, add its FIRST table to the current symbol
                elif issubclass(symbol, Nonterminal):
                    nonterminal_entries = table[symbol].copy()
                    for entry in nonterminal_entries:  # type: Tuple | EPSILON_TYPE
                        is_eps = entry == EPSILON
                        if is_eps:
                            iterate_rule(current_firsts, to_look[1:], contains_epsilon_prefix)
                        else:
                            new_first = set(
                                [tuple([*c, *entry]) for c in current_firsts] +
                                ([entry] if contains_epsilon_prefix else [])
                            )
                            iterate_rule(new_first, to_look[1:], False)
                else:
                    raise ValueError('Unknown symbol type, should never happen', symbol)  # pragma no cover

            iterate_rule(set(), to_symbols, True)

    return table

