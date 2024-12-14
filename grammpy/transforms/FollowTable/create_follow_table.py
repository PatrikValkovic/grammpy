#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.12.2024 11:53
:Licence MIT
Part of grammpy

"""
from inspect import isclass
from typing import TYPE_CHECKING, Dict, Set, Tuple, Union, Type, Any
from grammpy import END_OF_INPUT, Nonterminal, EPSILON

if TYPE_CHECKING:   # pragma: no cover
    from grammpy import Grammar, Terminal, Rule, END_OF_INPUT_TYPE
    from ..FirstTable.create_first_table import FirstTableType
    FollowTableTypeValue = Set[
        Union[
            END_OF_INPUT_TYPE,
            Tuple[
                Union[
                    Type[Terminal],
                    Any,
                    END_OF_INPUT_TYPE
                ],
                ...
            ]
        ]
    ]
    FollowTableType = Dict[
        Union[Type[Nonterminal]],
        FollowTableTypeValue
    ]

def create_follow_table(grammar, first_table, look_ahead):
    # type: (Grammar, FirstTableType, int) -> FollowTableType
    """
    Given LL(k) grammar and its corresponding first table, create follow table.
    :param grammar: Grammar for which follow table is created.
    :param first_table: First table for the grammar.
    :param look_ahead: Look ahead of the parser, must be same or lower as the first table.
    :return: Follow table for the grammar
    """
    table = {nt: set() for nt in grammar.nonterminals}  # type: FollowTableType
    eoi_tuple = tuple([END_OF_INPUT]*look_ahead)
    table[grammar.start].add(eoi_tuple)
    updated = True

    def add_from_set(from_nonterminal, to_symbols_set):
        # type: (Type[Nonterminal], FollowTableTypeValue) -> None
        nonlocal updated
        original_size = len(table[from_nonterminal])
        for symbols in to_symbols_set:
            if len(symbols) == look_ahead:
                table[from_nonterminal].add(symbols)
        if len(table[from_nonterminal]) > original_size:
            updated = True

    while updated:
        updated = False
        for rule in grammar.rules:  # type: Type[Rule]
            left = rule.fromSymbol
            right = rule.right
            right_side_generates_epsilon = True
            right_side_first = table[left].copy()
            for i in range(len(right)-1, -1, -1):
                symbol = right[i]
                # check if it is terminal
                if symbol == EPSILON:
                    add_from_set(left, right_side_first)
                    continue
                if not isclass(symbol) or not issubclass(symbol, Nonterminal):
                    right_side_first = {
                        tuple([symbol, *k][:look_ahead]) for k in right_side_first
                    }
                    if right_side_generates_epsilon:
                        right_side_first.add(tuple([symbol]))
                    right_side_generates_epsilon = False
                    continue
                # it is nonterminal
                if right_side_generates_epsilon:
                    add_from_set(symbol, table[left])
                add_from_set(symbol, right_side_first)
                right_side_first = {
                    tuple([*c ,*e][:look_ahead]) for c in first_table[symbol] if c != EPSILON for e in right_side_first
                }
                right_side_generates_epsilon = right_side_generates_epsilon and EPSILON in first_table[symbol]

    return table
