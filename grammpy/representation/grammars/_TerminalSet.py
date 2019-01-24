#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.10.2018 15:10
:Licence GPLv3
Part of grammpy

"""
from typing import Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from ..grammars import Grammar


class _TerminalSet(set):
    def __init__(self, grammar, iterable=None):
        # type: (Grammar, Iterable) -> None
        self._grammar = grammar
        super().__init__()
        iterable = [] if iterable is None else iterable
        self.add(*iterable)

    def add(self, *terminals):
        # type: (Iterable) -> None
        for term in terminals:
            if term in self:
                continue
            super().add(term)
            self._grammar._symbs_of_rules[term] = set()

    def remove(self, *terminals):
        # type: (Iterable) -> None
        for term in terminals:
            self._grammar.remove_rule(list(self._grammar._symbs_of_rules[term]), _validate=False)
            del self._grammar._symbs_of_rules[term]
            super().remove(term)
