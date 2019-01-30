#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 01.08.2017 07:33
:Licence GNUv3
Part of grammpy

"""
from typing import Type, Optional

from ..exceptions import NonterminalDoesNotExistsException
from .Nonterminal import Nonterminal
from .constants import EPSILON
from .support import _NonterminalSet
from .support import _RulesSet
from .support import _TerminalSet


class Grammar:
    """
    Provide base interface for manipulating with the grammar
    """

    def __init__(self,
                 terminals=None,
                 nonterminals=None,
                 rules=None,
                 start_symbol=None):
        """
        Create instance of grammar
        :param terminals: Sequence of terminals to add, empty sequence by default
        :param nonterminals: Sequence of nonterminals to add, empty sequence by default
        :param rules: Sequence of rules to add, empty sequence by default
        :param start_symbol: Start symbol of the grammar, start symbol must be in nonterminals.
        None by default
        """
        assign_map = dict({EPSILON: set()})

        terminals = [] if terminals is None else terminals
        self._terminals = _TerminalSet(self, assign_map, terminals)

        nonterminals = [] if nonterminals is None else nonterminals
        self._nonterminals = _NonterminalSet(self, assign_map, nonterminals)

        self._start_symbol = None
        self.start = start_symbol

        rules = [] if rules is None else rules
        self._rules = _RulesSet(self, assign_map, rules)

    @property
    def terminals(self):
        # type: () -> _TerminalSet
        return self._terminals

    @property
    def nonterminals(self):
        # type: () -> _NonterminalSet
        return self._nonterminals

    @property
    def rules(self):
        # type: () -> _RulesSet
        return self._rules

    @property
    def start(self):
        # type: () -> Optional[Type[Nonterminal]]
        return self._start_symbol

    @start.setter
    def start(self, s):
        # type: (Optional[Type[Nonterminal]]) -> None
        if s is not None and s not in self.nonterminals:
            raise NonterminalDoesNotExistsException(None, s, self)
        self._start_symbol = s

    @start.deleter
    def start(self):
        # type: () -> None
        self.start = None

    def __copy__(self):
        return Grammar(terminals=self.terminals,
                       nonterminals=self.nonterminals,
                       rules=self.rules,
                       start_symbol=self.start)
