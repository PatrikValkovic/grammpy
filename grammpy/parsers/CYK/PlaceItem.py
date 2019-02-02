#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 21:56
:Licence GNUv3
Part of grammpy

"""

from typing import TYPE_CHECKING, Type

if TYPE_CHECKING:  # pragma: no cover
    from ... import Rule, Nonterminal


class PlaceItem:
    """
    Represent item in the CYK structure.
    """
    def __init__(self, r, t1, t2):
        # type: (Type[Rule], Type[Rule], Type[Rule]) -> None
        """
        Create instance of PlaceItem.
        :param r: Rule to store.
        :param t1: Rule to match first symbol on the right side.
        :param t2: Rule to match second symbol on the right side.
        """
        self.to_rule = [t1, t2]
        self.rule = r

    def __hash__(self):
        # type: () -> int
        """
        Return hash of stored rule.
        :return: Hash of stored rule.
        """
        return hash(self.rule)

    @property
    def fromSymbol(self):
        # type: () -> Type[Nonterminal]
        """
        Get symbol on the left side of the rule.
        :return: Left side of the rule.
        """
        return self.rule.fromSymbol
