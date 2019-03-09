#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 22.08.2017 11:39
:Licence GNUv3
Part of grammpy

"""

from typing import List, Dict, Type, TYPE_CHECKING

from ._support import _is_unit
from ... import Grammar, Nonterminal

if TYPE_CHECKING:  # pragma: no cover
    from ... import Rule

    MATRIX_OF_UNIT_RULES = List[List[List[Type[Rule]]]]


class UnitSymbolReachability:
    """
    Class containing info about reachability of unit rules.
    """

    def __init__(self, field, translation):
        # type: (MATRIX_OF_UNIT_RULES, Dict[Type[Nonterminal], int]) -> None
        """
        Create isntance of UnitSymbolRechablingResults
        :param field: Result of Floyd-Warshall algorithm
        :param translation: Dictionary where keys is nonterminal and value is position in the field.
        """
        # matrix of lists
        self.f = field  # type: MATRIX_OF_UNIT_RULES
        self.t = translation  # type: Dict[Type[Nonterminal], int]

    def reach(self, from_symbol, to_symbol):
        # type: (Type[Nonterminal], Type[Nonterminal]) -> bool
        """
        Check if exists sequence of unit rules between two symbols.
        :param from_symbol: From which symbol find the sequence.
        :param to_symbol:  To which symbol find the sequence.
        :return: True if exists sequence of unit rules, false otherwise.
        """
        return len(self.path_rules(from_symbol, to_symbol)) > 0

    def reachables(self, from_symbol):
        # type: (Type[Nonterminal]) -> List[Type[Nonterminal]]
        """
        Get list of nonterminals, what are rewritable from nonterminal passed as parameter
        using only unit rules.
        :param from_symbol: For which symbols to search.
        :return: List of nonterminals.
        """
        if from_symbol not in self.t:
            return []
        reachable = []
        index = self.t[from_symbol]
        for n, i in self.t.items():
            if len(self.f[index][i] or []) > 0:
                reachable.append(n)
        return reachable

    def path_rules(self, from_symbol, to_symbol):
        # type: (Type[Nonterminal], Type[Nonterminal]) -> List[Type[Rule]]
        """
        Get sequence of unit rules between first and second parameter.
        :param from_symbol: From which symbol.
        :param to_symbol: To which symbol.
        :return: Sequence of unit rules. Empty sequence mean there is no way between them.
        """
        if from_symbol not in self.t or to_symbol not in self.t:
            return []
        return self.f[self.t[from_symbol]][self.t[to_symbol]] or []


def find_nonterminals_reachable_by_unit_rules(grammar):
    # type: (Grammar) -> UnitSymbolReachability
    """
    Get nonterminal for which exist unit rule
    :param grammar: Grammar where to search
    :return: Instance of UnitSymbolRechablingResults.
    """
    # get nonterminals
    nonterminals = list(grammar.nonterminals)  # type: List[Type[Nonterminal]]
    count_of_nonterms = len(nonterminals)
    # create indexes for nonterminals
    nonterm_to_index = dict()  # type: Dict[Type[Nonterminal], int]
    for i in range(count_of_nonterms):
        nonterm_to_index[nonterminals[i]] = i
    # prepare matrix
    field = [[None for _ in nonterminals] for _ in nonterminals]  # type: MATRIX_OF_UNIT_RULES
    # fill existing unit rules
    for rule in grammar.rules:
        if _is_unit(rule):
            field[nonterm_to_index[rule.fromSymbol]][nonterm_to_index[rule.toSymbol]] = [rule]
    # run Floyd Warshall
    f = field
    for k in range(count_of_nonterms):
        for i in range(count_of_nonterms):
            for j in range(count_of_nonterms):
                if f[i][k] is not None and f[k][j] is not None:
                    if f[i][j] is None or len(f[i][j]) > len(f[i][k]) + len(f[k][j]):
                        f[i][j] = f[i][k] + f[k][j]
    # return results
    return UnitSymbolReachability(f, nonterm_to_index)
