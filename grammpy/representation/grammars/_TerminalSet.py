#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.10.2018 15:10
:Licence GPLv3
Part of grammpy

"""
from typing import Iterable


class _TerminalSet(set):
    def __init__(self, grammar, iterable=...):
        self._grammar = grammar
        super().__init__()
        self.add(*iterable)

    def add(self, *terminals):
        for term in terminals:
            if term in self:
                continue
            super().add(term)
            self._grammar._symbs_of_rules[term] = set()

    def remove(self, *terminals):
        for term in terminals:
            self._grammar.remove_rule(list(self._grammar._symbs_of_rules[term]), _validate=False)
            del self._grammar._symbs_of_rules[term]
            super().remove(term)




