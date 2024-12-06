#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.12.2024 11:53
:Licence MIT
Part of grammpy

"""
from inspect import isclass
from typing import TYPE_CHECKING, Dict, Set, List, Union, Type
from grammpy import END_OF_INPUT, Nonterminal, EPSILON

if TYPE_CHECKING:   # pragma: no cover
    from grammpy import Grammar, Terminal, Rule, END_OF_INPUT_TYPE
    from ..FirstTable.create_first_table import FirstTableType, FirstTableTypeValue
    FollowTableTypeValue = Set[Union[
        END_OF_INPUT_TYPE,
        List[Union[Type[Terminal], Terminal]]
    ]]
    FollowTableType = Dict[
        Union[Type[Nonterminal]],
        FollowTableTypeValue
    ]

def create_follow_table(grammar, first_table, look_ahead):
    # type: (Grammar, FirstTableType, int) -> FollowTableType
    """
    Given LL(k) grammar and its corresponding first table, create follow table
    :param grammar: Grammar for which follow table is created
    :param next_table: First table for the grammar
    :return: Follow table for the grammar
    """
    table = {nt: set() for nt in grammar.nonterminals}  # type: FollowTableType
    table[grammar.start].add((END_OF_INPUT,))
    updated = True

    def add_from_first(from_nonterminal, to_symbols_set):
        # type: (Type[Nonterminal], FirstTableTypeValue) -> None
        nonlocal updated
        original_size = len(table[from_nonterminal])
        for symbols in to_symbols_set:
            if symbols != EPSILON:
                table[from_nonterminal].add(symbols)
        if len(table[from_nonterminal]) > original_size:
            updated = True

    def add_from_follow(from_nonterminal, to_symbols_set):
        # type: (Type[Nonterminal], FollowTableTypeValue) -> None
        nonlocal updated
        original_size = len(table[from_nonterminal])
        for symbols in to_symbols_set:
            table[from_nonterminal].add(symbols)
        if len(table[from_nonterminal]) > original_size:
            updated = True

    while updated:
        updated = False
        for rule in grammar.rules:  # type: Type[Rule]
            left = rule.fromSymbol
            right = rule.right
            right_side_generates_epsilon = True
            right_side_first = set()
            for i in range(len(right)-1, -1, -1):
                right_side_first = {tuple(k[:look_ahead]) for k in right_side_first if k != EPSILON}
                symbol = right[i]
                # check if it is terminal
                if symbol == EPSILON:
                    continue
                if not isclass(symbol) or not issubclass(symbol, Nonterminal):
                    right_side_first = {
                        tuple([symbol, *k]) for k in right_side_first
                    }
                    if right_side_generates_epsilon:
                        right_side_first.add(tuple([symbol]))
                    right_side_generates_epsilon = False
                    continue
                # it is nonterminal
                if right_side_generates_epsilon:
                    add_from_follow(symbol, table[left])
                add_from_first(symbol, right_side_first)
                right_side_first = {
                    tuple([*c ,*e]) for c in first_table[symbol] if c != EPSILON for e in right_side_first
                }
                if right_side_generates_epsilon:
                    for c in first_table[symbol]:
                        right_side_first.add(c)
                right_side_generates_epsilon = right_side_generates_epsilon and EPSILON in first_table[symbol]

    return table