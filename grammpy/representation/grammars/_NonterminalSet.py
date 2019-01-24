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
    from ..grammars import Grammar


class _NonterminalSet(set):
    def __init__(self, grammar, iterable=None):
        # type: (Grammar, Iterable[Type[Nonterminal]]) -> None
        self._grammar = grammar
        super().__init__()
        iterable = [] if iterable is None else iterable
        self.add(*iterable)

    @staticmethod
    def _control_nonterminal(nonterm):
        if not inspect.isclass(nonterm) or not issubclass(nonterm, Nonterminal):
            raise NotNonterminalException(nonterm)

    def add(self, *nonterminals):
        # type: (Iterable[Type[Nonterminal]]) -> None
        for nonterm in nonterminals:
            if nonterm in self:
                continue
            _NonterminalSet._control_nonterminal(nonterm)
            super().add(nonterm)
            self._grammar._symbs_of_rules[nonterm] = set()

    def remove(self, *nonterminals):
        # type: (Iterable[Type[Nonterminal]]) -> None
        for nonterm in nonterminals:
            if not nonterm in self:
                continue
            self._grammar.remove_rule(list(self._grammar._symbs_of_rules[nonterm]), _validate=False)
            del self._grammar._symbs_of_rules[nonterm]
            if self._grammar.start_get() == nonterm:
                self._grammar.start_set(None)
            super().remove(nonterm)

    def __contains__(self, o):
        # type: (Type[Nonterminal]) -> bool
        _NonterminalSet._control_nonterminal(o)
        return super().__contains__(o)


