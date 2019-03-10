#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.10.2018 15:10
:Licence MIT
Part of grammpy

"""
from typing import Iterable, TYPE_CHECKING, Any

from ._BaseSet import _BaseSet

if TYPE_CHECKING:  # pragma: no cover
    from .. import Grammar


class _TerminalSet(_BaseSet):
    """
    Set that store terminals inside the grammar.
    """

    def __init__(self, grammar, assign_map, iterable=None):
        # type: (Grammar, dict, Iterable[Any]) -> None
        """
        Create new instance of _TerminalSet.
        :param grammar: Grammar for which create the set.
        :param assign_map: Map used for assignment rules to terminals.
        :param iterable: Terminals to insert.
        """
        self._grammar = grammar
        self._assign_map = assign_map
        super().__init__()
        self.add(*(iterable or []))

    def add(self, *terminals):
        # type: (Iterable[Any]) -> None
        """
        Add terminals into the set.
        :param terminals: Terminals to insert.
        """
        for term in terminals:
            if term in self:
                continue
            super().add(term)
            self._assign_map[term] = set()

    def remove(self, *terminals):
        # type: (Iterable[Any]) -> None
        """
        Remove terminals from the set.
        Removes also rules using this terminal.
        :param terminals: Terminals to remove.
        :raise KeyError if the object is not in the set.
        """
        for term in terminals:
            if term not in self:
                raise KeyError('Terminal ' + str(term) + ' is not inside')
            self._grammar.rules.remove(*self._assign_map[term], _validate=False)
            del self._assign_map[term]
            super().remove(term)