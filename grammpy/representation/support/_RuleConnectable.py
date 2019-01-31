#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.01.2019 13:48
:Licence GPLv3
Part of grammpy

"""
import weakref
from typing import TYPE_CHECKING, Optional

from ...exceptions import TreeDeletedException

if TYPE_CHECKING:
    from .. import Rule


class _RuleConnectable:
    """
    Represent entity that can be connected by Rule in the AST.
    """

    def __init__(self):
        """
        Creates new instance.
        Properties from_rule and to_rule are None.
        """
        self._from_rule = None
        self._to_rule = None

    @property
    def from_rule(self):
        # type: (_RuleConnectable) -> Optional[Rule]
        """
        Rule that the symbol is rewrote from.
        :return: Instance of Rule that the symbol is rewrited from.
        :raise TreeDeletedException: If the tree was already deleted (pointer to the painter get lost).
        This can occur because weak reference to the parent is used.
        """
        if self._from_rule is None:
            return None
        if self._from_rule() is None:
            raise TreeDeletedException()
        return self._from_rule()

    @property
    def to_rule(self):
        # type: (_RuleConnectable) -> Optional[Rule]
        """
        Rule that the symbol is rewrote to.
        :return: Instance of Rule that the symbols is rewrited to.
        """
        return self._to_rule

    def _set_from_rule(self, r):
        # type: (_RuleConnectable, Rule) -> None
        """
        Set the rule that the symbol is rewrote from.
        :param r: Instance of Rule that the symbol should rewrite from.
        """
        self._from_rule = weakref.ref(r)

    def _set_to_rule(self, r):
        # type: (_RuleConnectable, Rule) -> None
        """
        Set the rule that the symbol is rewrote to.
        :param r: Instance of Rule that the symbol should rewrite to.
        """
        self._to_rule = r
