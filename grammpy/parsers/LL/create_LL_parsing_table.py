#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 05.12.2024 21:01
:Licence MIT
Part of grammpy

"""
from inspect import isclass
from typing import TYPE_CHECKING, Dict, Union, Type, List, Set, Tuple
from grammpy import Nonterminal, EPSILON, EPSILON_TYPE

if TYPE_CHECKING:   # pragma: no cover
    from grammpy import Grammar, Terminal, Rule, END_OF_INPUT_TYPE
    from ...transforms.FirstTable.create_first_table import FirstTableType
    from ...transforms.FollowTable.create_follow_table import FollowTableType

type LLTableType = Dict[
    Type[Nonterminal],
    Dict[
        List[Union[END_OF_INPUT_TYPE, Type[Terminal], Terminal]],
        Set[Type[Rule]]
    ]
]

def create_LL_parsing_table(g, first, follow, look_ahead):
    # type: (Grammar, FirstTableType, FollowTableType, int) -> LLTableType
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
                    tuple([*e, *f]) for f in first_without_epsilon for e in first_of_right
                }
                if can_generate_epsilon:
                    first_of_right.update(f for f in first[symbol] if f != EPSILON)
                can_generate_epsilon = can_generate_epsilon and EPSILON in first[symbol]
        # shorten sequences
        first_of_right = {tuple(e[:look_ahead]) for e in first_of_right}
        # add to the parsing table
        for sequence in first_of_right:
            sequence_to_add = tuple(sequence[:look_ahead])
            if sequence_to_add not in parsing_table[left]:
                parsing_table[left][sequence_to_add] = set()
            parsing_table[left][sequence_to_add].add(rule)
        if can_generate_epsilon:
            for sequence_to_add in follow[left]:
                if sequence_to_add not in parsing_table[left]:
                    parsing_table[left][sequence_to_add] = set()
                parsing_table[left][sequence_to_add].add(rule)

    return parsing_table