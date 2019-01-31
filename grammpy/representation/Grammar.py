#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 07:33
:Licence GNUv3
Part of grammpy

"""
from typing import Type, Optional, Iterable, TYPE_CHECKING, Any

from .Nonterminal import Nonterminal
from .support._NonterminalSet import _NonterminalSet
from .support._RulesSet import _RulesSet
from .support._TerminalSet import _TerminalSet
from .support._constants import EPSILON
from ..exceptions import NonterminalDoesNotExistsException

if TYPE_CHECKING:
    from . import Rule


class Grammar:
    """
    Provide interface for manipulating with the grammar
    """

    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol=None):
        # type: (Optional[Iterable[Any]], Optional[Iterable[Type[Nonterminal]]], Optional[Iterable[Type[Rule]]], Optional[Type[Nonterminal]]) -> Grammar
        """
        Create instance of grammar.
        :param terminals: Sequence of terminals to add, empty sequence by default.
        :param nonterminals: Sequence of nonterminals to add, empty sequence by default.
        :param rules: Sequence of rules to add, empty sequence by default.
        :param start_symbol: Start symbol of the grammar, start symbol must be in nonterminals.
        None by default.
        """
        assign_map = dict({EPSILON: set()})
        self._terminals = _TerminalSet(self, assign_map, terminals)
        self._nonterminals = _NonterminalSet(self, assign_map, nonterminals)
        self._start_symbol = None
        self._rules = _RulesSet(self, assign_map, rules)
        self.start = start_symbol

    @property
    def terminals(self):
        # type: () -> _TerminalSet
        """
        Get set representing terminals.
        :return: Set representing terminals.
        """
        return self._terminals

    @property
    def nonterminals(self):
        # type: () -> _NonterminalSet
        """
        Get set representing nonterminals.
        :return: Set representing nonterminals.
        """
        return self._nonterminals

    @property
    def rules(self):
        # type: () -> _RulesSet
        """
        Get set representing rules.
        :return: Set representing rules.
        """
        return self._rules

    @property
    def start(self):
        # type: () -> Optional[Type[Nonterminal]]
        """
        Get start symbol of the grammar.
        :return: Start symbol of the grammar, or None if it isn't defined.
        """
        return self._start_symbol

    @start.setter
    def start(self, s):
        # type: (Optional[Type[Nonterminal]]) -> None
        """
        Set start symbol of the grammar.
        :param s: Start symbol to set.
        :raise NonterminalDoesNotExistsException: If the start symbol is not in nonterminals.
        """
        if s is not None and s not in self.nonterminals:
            raise NonterminalDoesNotExistsException(None, s, self)
        self._start_symbol = s

    @start.deleter
    def start(self):
        # type: () -> None
        """
        Unset start symbol and set it to None.
        """
        self.start = None

    def __copy__(self):
        # type: () -> Grammar
        """
        Perform shallow copy of the grammar.
        :return: Shallow copy of the grammar.
        """
        return Grammar(terminals=self.terminals,
                       nonterminals=self.nonterminals,
                       rules=self.rules,
                       start_symbol=self.start)
