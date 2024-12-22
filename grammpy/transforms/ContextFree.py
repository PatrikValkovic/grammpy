#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 10.08.2017 20:33
:Licence MIT
Part of grammpy

"""

from typing import TYPE_CHECKING, Dict

from .ChomskyForm import *
from .EpsilonRulesRemove import *
from .NongeneratingSymbolsRemove import *
from .UnitRulesRemove import *
from .UnreachableSymbolsRemove import *
from .FirstTable import *
from .FollowTable import *

if TYPE_CHECKING:  # pragma: no cover
    from .. import Grammar
    from .FirstTable.create_first_table import FirstTableType

__all__ = ['ContextFree']


class ContextFree:
    """
    Class that aggregates functions transforming context-free grammars.
    """

    EpsilonRemovedRule = EpsilonRemovedRule
    ReducedUnitRule = ReducedUnitRule
    ChomskyRule = ChomskyRule
    ChomskySplitRule = ChomskySplitRule
    ChomskyTermRule = ChomskyTermRule
    ChomskyRestRule = ChomskyRestRule
    ChomskyTerminalReplaceRule = ChomskyTerminalReplaceRule

    ChomskyNonterminal = ChomskyNonterminal
    ChomskyGroupNonterminal = ChomskyGroupNonterminal
    ChomskyTermNonterminal = ChomskyTermNonterminal

    UnitSymbolRechablingResults = UnitSymbolReachability

    @staticmethod
    def remove_nongenerating_nonterminals(grammar, inplace=False):
        # type: (Grammar, bool) -> Grammar
        """
        Remove nongenerating symbols from the grammar.
        Nongenerating symbols are symbols, that don't generate sequence of terminals.
        For example never ending recursion.
        :param grammar: Grammar where to remove nongenerating symbols.
        :param inplace: True if transformation should be performed in place. False by default.
        :return: Grammar without nongenerating symbols.
        """
        return remove_nongenerating_nonterminals(grammar, inplace)

    @staticmethod
    def is_grammar_generating(grammar, remove=False):
        # type: (Grammar, bool) -> bool
        """
        Check if is grammar is generating.
        Generating grammar generates at least one sentence.
        :param grammar: Grammar to check.
        :param remove: True to remove nongenerating symbols from the grammar.
        :return: True if is grammar generating, false otherwise.
        """
        g = ContextFree.remove_nongenerating_nonterminals(grammar, remove)
        return g.start is not None

    @staticmethod
    def remove_unreachable_symbols(grammar, inplace=False):
        # type: (Grammar, bool) -> Grammar
        """
        Remove unreachable symbols from the grammar.
        :param grammar: Grammar where to remove symbols
        :param inplace: True if transformation should be performed in place. False by default.
        :return: Grammar without unreachable symbols.
        """
        return remove_unreachable_symbols(grammar, inplace)

    @staticmethod
    def remove_useless_symbols(grammar, inplace=False):
        # type: (Grammar, bool) -> Grammar
        """
        Remove useless symbols from the grammar.
        Useless symbols are unreachable or nongenerating one.
        :param grammar: Grammar where to remove symbols.
        :param inplace: True if transformation should be performed in place, false otherwise.
        False by default.
        :return: Grammar without useless symbols.
        """
        grammar = ContextFree.remove_nongenerating_nonterminals(grammar, inplace)
        grammar = ContextFree.remove_unreachable_symbols(grammar, True)
        return grammar

    @staticmethod
    def remove_rules_with_epsilon(grammar, inplace=False):
        # type: (Grammar, bool) -> Grammar
        """
        Remove epsilon rules.
        :param grammar: Grammar where rules remove
        :param inplace: True if transformation should be performed in place, false otherwise.
        False by default.
        :return: Grammar without epsilon rules.
        """
        return remove_rules_with_epsilon(grammar, inplace)

    @staticmethod
    def find_nonterminals_rewritable_to_epsilon(grammar):
        # type: (Grammar) -> Dict[Type[Nonterminal], Type[Rule]]
        """
        Get nonterminals rewritable to epsilon.
        :param grammar: Grammar where to search.
        :return: Dictionary, where key is nonterminal rewritable to epsilon and
        value is rule that is responsible for it.
        The rule doesn't need to rewrite to epsilon directly,
        but the whole right side can be rewritable to epsilon using different rules.
        """
        return find_nonterminals_rewritable_to_epsilon(grammar)

    @staticmethod
    def find_nonterminals_reachable_by_unit_rules(grammar):
        # type: (Grammar) -> UnitSymbolReachability
        """
        Get nonterminal for which exist unit rule
        :param grammar: Grammar where to search
        :return: Instance of UnitSymbolReachability.
        """
        return find_nonterminals_reachable_by_unit_rules(grammar)

    @staticmethod
    def remove_unit_rules(grammar, inplace=False):
        # type: (Grammar, bool) -> Grammar
        """
        Remove unit rules from the grammar.
        :param grammar: Grammar where remove the rules.
        :param inplace: True if transformation should be performed in place. False by default.
        :return: Grammar without unit rules.
        """
        return remove_unit_rules(grammar, inplace)

    @staticmethod
    def transform_to_chomsky_normal_form(grammar, inplace=False):
        # type: (Grammar, bool) -> Grammar
        """
        Transform grammar to Chomsky Normal Form.
        :param grammar: Grammar to transform.
        :param inplace: True if transformation should be performed in place. False by default.
        :return: Grammar in Chomsky Normal Form.
        """
        return transform_to_chomsky_normal_form(grammar, inplace)

    @staticmethod
    def prepare_for_cyk(grammar, inplace=False):
        # type: (Grammar, bool) -> Grammar
        """
        Take common context-free grammar and perform all the necessary steps to use it in the CYK algorithm.
        Performs following steps:
        - remove useless symbols
        - remove rules with epsilon
        - remove unit rules
        - remove useless symbols once more (as previous steps could change the grammar)
        - transform it to Chomsky Normal Form
        :param grammar: Grammar to transform.
        :param inplace: True if the operation should be done in place. False by default.
        :return: Modified grammar.
        """
        grammar = ContextFree.remove_useless_symbols(grammar, inplace)
        grammar = ContextFree.remove_rules_with_epsilon(grammar, True)
        grammar = ContextFree.remove_unit_rules(grammar, True)
        grammar = ContextFree.remove_useless_symbols(grammar, True)
        grammar = ContextFree.transform_to_chomsky_normal_form(grammar, True)
        return grammar

    @staticmethod
    def create_first_table(grammar, look_ahead):
        # type: (Grammar, int) -> FirstTableType
        """
        Given LL(n) grammar creates first table
        :param grammar: Grammar to create first table for
        :param look_ahead: Number of symbols to look ahead
        :return: First table
        """
        return create_first_table(grammar, look_ahead)

    @staticmethod
    def create_follow_table(grammar, first_table, look_ahead):
        # type: (Grammar, FirstTableType, int) -> FollowTableType
        """
        Given LL(k) grammar and its corresponding first table, create follow table.
        :param grammar: Grammar for which follow table is created.
        :param first_table: First table for the grammar.
        :param look_ahead: Look ahead of the parser, must be same or lower as the first table.
        :return: Follow table for the grammar
        """
        return create_follow_table(grammar, first_table, look_ahead)
