#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 05.12.2024 21:01
:Licence MIT
Part of grammpy

"""
from inspect import isclass
from typing import TYPE_CHECKING, Dict, Union, Type, Tuple, Set, Any
from grammpy import Nonterminal, EPSILON

if TYPE_CHECKING:   # pragma: no cover
    from grammpy import Grammar, Terminal, Rule, END_OF_INPUT_TYPE, EPSILON_TYPE
    from ...transforms.FirstTable.create_first_table import FirstTableType
    from ...transforms.FollowTable.create_follow_table import FollowTableType
    LLTableType = Dict[
        Type[Nonterminal],
        Dict[
            Tuple[
                Union[
                    END_OF_INPUT_TYPE,
                    Type[Terminal],
                    Any
                ],
                ...
            ],
            Union[
                Set[Type[Rule]],
                Type[Rule]
            ]
        ]
    ]

def create_ll_parsing_table(g, first, follow, look_ahead):
    # type: (Grammar, FirstTableType, FollowTableType, int) -> LLTableType
    """
    Create LL parser for given grammar.
    You must provide FIRST and FOLLOW table for the grammar with the proper look ahead.
    :param g: Grammar to create LL parser for.
    :param first: FIRST table for the grammar.
    :param follow: FOLLOW table for the grammar.
    :param look_ahead: Number of symbols that the parser will look.
    :return: LL(k) parsing table.
    """
    parsing_table = {N: dict() for N in g.nonterminals}

    for rule in g.rules:
        left = rule.fromSymbol
        right = rule.right
        # generate FIRST of the right side
        can_generate_epsilon = True
        first_of_right = set()
        for symbol in right:  # type: Union[Type[Terminal], Terminal, EPSILON_TYPE]
            if symbol == EPSILON:
                continue
            if not isclass(symbol) or not issubclass(symbol, Nonterminal):
                first_of_right = {
                    tuple([*e, symbol]) for e in first_of_right
                }
                if can_generate_epsilon:
                    first_of_right.add(tuple([symbol]))
                can_generate_epsilon = False
            else:
                first_without_epsilon = {f for f in first[symbol] if f != EPSILON}
                first_of_right = {
                    tuple([*e, *([*f] if f is not EPSILON else [])]) for f in first[symbol] for e in first_of_right
                }
                if can_generate_epsilon:
                    first_of_right.update(f for f in first_without_epsilon)
                can_generate_epsilon = can_generate_epsilon and EPSILON in first[symbol]
        # add follow
        first_of_right = {
            tuple([*e, *f]) for f in follow[left] for e in first_of_right
        }
        if can_generate_epsilon:
            first_of_right.update(follow[left])
        # shorten sequences
        first_of_right = {tuple(e[:look_ahead]) for e in first_of_right}
        # add to the parsing table
        for sequence in first_of_right:
            if sequence not in parsing_table[left]:
                parsing_table[left][sequence] = set()
            parsing_table[left][sequence].add(rule)

    return parsing_table
