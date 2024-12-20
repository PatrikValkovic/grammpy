#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 11.12.2024 16:18
:Licence MIT
Part of grammpy

"""
from inspect import isclass
from itertools import chain
from typing import TYPE_CHECKING, Union, Any, List, Iterable, Type, Set, cast
from ... import Terminal, END_OF_INPUT, Rule, Nonterminal, EPSILON
from ...exceptions import ParsingTableDiscrepancyException, NonterminalIsMissingException, NoRuleForLookAheadException, \
    ParsingAmbiguityException, NotRuleException

if TYPE_CHECKING:  # pragma: no cover
    from .create_ll_parsing_table import LLTableType


class _StackTerminalWrapper:
    def __init__(self, symbol, parent_rule):
        self.symbol = symbol
        self.parent_rule = parent_rule


def ll(start_nonterminal, sequence, parsing_table, look_ahead, *, raise_on_ambiguity=True):
    # type: (Type[Nonterminal], Iterable[Union[Terminal, Any]], LLTableType, int, Any, bool) -> Nonterminal
    """
    Parse input sequence using look-ahead of LL(k) parsing.
    :param start_nonterminal: Starting nonterminal of grammar, also the type of root node of the parsed AST.
    :param sequence: Sequence to parse. Must be iterator and support next() method.
    :param parsing_table: Parsing table to use for parsing. Look ahead for the table must be the same as look_ahead parameter.
    :param look_ahead: Look-ahead to use for parsing.
    :param raise_on_ambiguity: Raise exception if there are ambiguous rules applicable for current nonterminal and look ahead.
    :return: Root node of the parsed AST.
    """
    stack = []  # type: List[_StackTerminalWrapper]
    ending_sequence = tuple([END_OF_INPUT] * look_ahead)
    start = start_nonterminal()
    stack.append(_StackTerminalWrapper(start, None))

    input_sequence = chain(sequence, ending_sequence)
    current_lookahead = tuple([next(input_sequence) for _ in range(look_ahead)])
    current_symbol_index = 0
    while True:
        if current_lookahead == ending_sequence and len(stack) == 0:
            return start
        if len(current_lookahead) < look_ahead:
            current_lookahead = tuple([*current_lookahead, next(input_sequence)])
            continue
        top_stack = stack.pop()
        if top_stack.symbol is EPSILON:
            eps_terminal = Terminal(EPSILON)
            top_stack.parent_rule._to_symbols.append(eps_terminal)
            eps_terminal._set_from_rule(top_stack.parent_rule)
            continue
        if not isinstance(top_stack.symbol, Nonterminal):
            if hash(top_stack.symbol) != hash(current_lookahead[0]):
                raise ParsingTableDiscrepancyException(current_symbol_index, f"Expected terminal {top_stack.symbol}, but found {current_lookahead[0]}")
            term_symbol = current_lookahead[0]
            if not isinstance(term_symbol, Terminal):
                term_symbol = Terminal(term_symbol)
            current_lookahead = tuple(current_lookahead[1:])
            current_symbol_index += 1
            top_stack.parent_rule._to_symbols.append(term_symbol)
            term_symbol._set_from_rule(top_stack.parent_rule)
            continue
        # Connect the nonterminal
        if top_stack.parent_rule is not None:
            top_stack.parent_rule._to_symbols.append(top_stack.symbol)
            top_stack.symbol._set_from_rule(top_stack.parent_rule)
        # Find rule to use
        nonterminal_instance = top_stack.symbol
        nonterminal = type(nonterminal_instance)
        if nonterminal not in parsing_table:
            raise NonterminalIsMissingException(current_symbol_index, nonterminal, f"There are no rules for nonterminal {nonterminal.__name__}")
        table_for_nonterminal = parsing_table[nonterminal]
        if current_lookahead not in table_for_nonterminal:
            raise NoRuleForLookAheadException(current_symbol_index, f"No rule for {nonterminal.__name__} with lookahead {current_lookahead} found")
        rule_to_use = table_for_nonterminal[current_lookahead]
        if isinstance(rule_to_use, set) and len(rule_to_use) == 0:
            raise NoRuleForLookAheadException(current_symbol_index, f"No rule for {nonterminal.__name__} with lookahead {current_lookahead} found")
        if isinstance(rule_to_use, set) and len(rule_to_use) > 1 and raise_on_ambiguity:
            raise ParsingAmbiguityException(current_symbol_index, [*rule_to_use], f"Ambiguity found for {nonterminal.__name__} and lookahead {current_lookahead}")
        if isinstance(rule_to_use, set):
            rule_to_use = next(iter(rule_to_use))
        if not isclass(rule_to_use) or not issubclass(rule_to_use, Rule):
            raise NotRuleException(rule_to_use)
        # Apply the rule
        rule_instance = rule_to_use()
        nonterminal_instance._set_to_rule(rule_instance)
        rule_instance._from_symbols.append(nonterminal_instance)
        for symbol in reversed(rule_instance.right):
            if symbol == EPSILON:
                stack.append(_StackTerminalWrapper(EPSILON, rule_instance))
            elif isclass(symbol) and issubclass(symbol, Nonterminal):
                stack.append(_StackTerminalWrapper(symbol(), rule_instance))
            else:
                stack.append(_StackTerminalWrapper(symbol, rule_instance))
