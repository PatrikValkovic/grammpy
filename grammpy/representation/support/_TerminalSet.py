#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.10.2018 15:10
:Licence GPLv3
Part of grammpy

"""
from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from .. import Grammar


class _TerminalSet(set):
    def __init__(self, grammar, assign_map, iterable=None):
        # type: (Grammar, dict, Iterable) -> None
        self._grammar = grammar
        self._assign_map = assign_map
        super().__init__()
        iterable = [] if iterable is None else iterable
        self.add(*iterable)

    def add(self, *terminals):
        # type: (Iterable) -> None
        for term in terminals:
            if term in self:
                continue
            super().add(term)
            self._assign_map[term] = set()

    def remove(self, *terminals):
        # type: (Iterable) -> None
        for term in terminals:
            self._grammar.rules.remove(*self._assign_map[term], _validate=False)
            del self._assign_map[term]
            super().remove(term)
