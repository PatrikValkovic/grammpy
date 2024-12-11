#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.12.2024 16:18
:Licence MIT
Part of grammpy

"""
from inspect import isclass
from typing import TYPE_CHECKING, Union, Any, List, Iterable, Type, Set
from ... import Terminal, END_OF_INPUT, Rule, Nonterminal, EPSILON
from itertools import chain

if TYPE_CHECKING:  # pragma: no cover
    from ... import Grammar
    from .create_LL_parsing_table import LLTableType

class _StackTerminalWrapper:
    def __init__(self, terminal, parent_rule):
        self.terminal = terminal
        self.parent_rule = parent_rule

def ll(grammar, sequence, parsing_table, look_ahead, *, raise_on_ambiguity = True):
    # type: (Grammar, Iterable[Union[Terminal, Any]], LLTableType, int, Any, bool) -> Nonterminal
    stack = []  # type: List[Union[Nonterminal, _StackTerminalWrapper]]
    ending_sequence = tuple([END_OF_INPUT]*look_ahead)
    start = grammar.start()
    stack.append(start)

    input_sequence = chain(sequence, ending_sequence)
    current_lookahead = tuple([next(input_sequence) for _ in range(look_ahead)])  # type: Tuple[Nonterminal, ...]
    while True:
        if current_lookahead == ending_sequence and len(stack) == 0:
            return start
        if len(current_lookahead) < look_ahead:
            current_lookahead = tuple([*current_lookahead, next(input_sequence)])
            continue
        top_stack = stack[-1]
        if isinstance(top_stack, _StackTerminalWrapper) and top_stack.terminal == EPSILON:
            stack.pop()
            eps_terminal = Terminal(EPSILON)
            top_stack.parent_rule._to_symbols.append(eps_terminal)
            eps_terminal._set_from_rule(top_stack.parent_rule)
            continue
        if isinstance(top_stack, _StackTerminalWrapper):
            if hash(top_stack.terminal) != hash(current_lookahead[0]):
                raise Exception(f"Expected terminal {top_stack.terminal}, but found {current_lookahead[0]}")
            stack.pop()
            term_symbol = current_lookahead[0]
            if not isinstance(term_symbol, Terminal):
                term_symbol = Terminal(term_symbol)
            current_lookahead = tuple(current_lookahead[1:])
            top_stack.parent_rule._to_symbols.append(term_symbol)
            term_symbol._set_from_rule(top_stack.parent_rule)
            continue
        # Find rule to use
        nonterminal_instance = stack.pop()
        nonterminal = type(nonterminal_instance)
        if nonterminal not in parsing_table:
            raise Exception(f"Rule for nontermianl {nonterminal.__name__} not found")
        table_for_nonterminal = parsing_table[nonterminal]
        if current_lookahead not in table_for_nonterminal:
            raise Exception(f"Rule for {nonterminal.__name__} with lookahead {current_lookahead} not found")
        rule_to_use = table_for_nonterminal[current_lookahead]  # type: Union[Type[Rule], Set[Type[Rule]]]
        if isinstance(rule_to_use, set) and len(rule_to_use) == 0:
            raise Exception(f"No rule to apply for {nonterminal.__name__} with lookahead {current_lookahead}")
        if isinstance(rule_to_use, set) and len(rule_to_use) > 1 and raise_on_ambiguity:
            raise Exception(f"Ambiguity found for {nonterminal.__name__} with lookahead {current_lookahead}")
        if isinstance(rule_to_use, set):
            rule_to_use = next(iter(rule_to_use))
        if not issubclass(rule_to_use, Rule):
            raise Exception(f"Rule is not subclass of Rule")
        # Apply the rule
        rule_instance = rule_to_use()
        nonterminal_instance._set_to_rule(rule_instance)
        rule_instance._from_symbols.append(nonterminal_instance)
        for symbol in reversed(rule_instance.right):
            if symbol == EPSILON:
                stack.append(_StackTerminalWrapper(EPSILON, rule_instance))
            elif isclass(symbol) and issubclass(symbol, Nonterminal):
                follow_instance = symbol()
                rule_instance._to_symbols.append(follow_instance)
                follow_instance._set_from_rule(rule_instance)
                stack.append(follow_instance)
            else:
                stack.append(_StackTerminalWrapper(symbol, rule_instance))

