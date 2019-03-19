#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 15.10.2018 15:10
:Licence MIT
Part of grammpy

"""
import inspect
from typing import Iterable, TYPE_CHECKING, Type

from ._BaseSet import _BaseSet
from ..Nonterminal import Nonterminal
from ...exceptions import NotNonterminalException

if TYPE_CHECKING:  # pragma: no cover
    from .. import Grammar


class _NonterminalSet(_BaseSet):
    """
    Set that store nonterminals inside the grammar.
    """

    def __init__(self, grammar, assign_map, iterable=None):
        # type: (Grammar, dict, Iterable[Type[Nonterminal]]) -> None
        """
        Create new instance of _NonterminalSet.
        :param grammar: Grammar for which create the set.
        :param assign_map: Map used for assignment rules to nonterminals.
        :param iterable: Nonterminals to insert.
        """
        self._grammar = grammar
        self._assign_map = assign_map
        super().__init__()
        self.add(*(iterable or []))

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
        """
        Add nonterminals into the set.
        :param nonterminals: Nonterminals to insert.
        :raise NotNonterminalException: If the object doesn't inherit from Nonterminal class.
        """
        for nonterm in nonterminals:
            if nonterm in self:
                continue
            _NonterminalSet._control_nonterminal(nonterm)
            super().add(nonterm)
            self._assign_map[nonterm] = set()

    def remove(self, *nonterminals):
        # type: (Iterable[Type[Nonterminal]]) -> None
        """
        Remove nonterminals from the set.
        Removes also rules using this nonterminal.
        Set start symbol to None if deleting nonterminal is start symbol at the same time.
        :param nonterminals: Nonterminals to remove.
        """
        for nonterm in set(nonterminals):
            _NonterminalSet._control_nonterminal(nonterm)
            if nonterm not in self:
                raise KeyError('Nonterminal ' + nonterm.__name__ + ' is not inside')
            self._grammar.rules.remove(*self._assign_map[nonterm], _validate=False)
            del self._assign_map[nonterm]
            if self._grammar.start is nonterm:
                del self._grammar.start
            super().remove(nonterm)

    def __contains__(self, o):
        # type: (Type[Nonterminal]) -> bool
        """
        Check, if is nonterminal in the set.
        :param o: Nonterminal to check.
        :return: True if the nonterminal is in the set, false otherwise.
        :raise NotNonterminalException: If the object doesn't inherit from Nonterminal class.
        """
        _NonterminalSet._control_nonterminal(o)
        return super().__contains__(o)
