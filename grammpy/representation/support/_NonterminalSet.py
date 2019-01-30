#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.10.2018 15:10
:Licence GPLv3
Part of grammpy

"""
import inspect
from typing import Iterable, TYPE_CHECKING, Type

from .. import Nonterminal
from ...exceptions import NotNonterminalException

if TYPE_CHECKING:
    from .. import Grammar


class _NonterminalSet(set):
    def __init__(self, grammar, assign_map, iterable=None):
        # type: (Grammar, dict, Iterable[Type[Nonterminal]]) -> None
        self._grammar = grammar
        self._assign_map = assign_map
        super().__init__()
        iterable = [] if iterable is None else iterable
        self.add(*iterable)

    @staticmethod
    def _control_nonterminal(nonterm):
        # type: (Type[Nonterminal]) -> None
        """
        Check if the nonterminal is valid.
        :param nonterm: Nonterminal to check.
        :raise NotNonterminalException: If the object doesn't inherit from Nonterminal class.
        """
        if not inspect.isclass(nonterm) or not issubclass(nonterm, Nonterminal):
            raise NotNonterminalException(nonterm)

    def add(self, *nonterminals):
        # type: (Iterable[Type[Nonterminal]]) -> None
        for nonterm in nonterminals:
            if nonterm in self:
                continue
            _NonterminalSet._control_nonterminal(nonterm)
            super().add(nonterm)
            self._assign_map[nonterm] = set()

    def remove(self, *nonterminals):
        # type: (Iterable[Type[Nonterminal]]) -> None
        for nonterm in nonterminals:
            if nonterm not in self:
                continue
            self._grammar.rules.remove(*self._assign_map[nonterm], _validate=False)
            del self._assign_map[nonterm]
            if self._grammar.start is nonterm:
                del self._grammar.start
            super().remove(nonterm)

    def __contains__(self, o):
        # type: (Type[Nonterminal]) -> bool
        _NonterminalSet._control_nonterminal(o)
        return super().__contains__(o)
