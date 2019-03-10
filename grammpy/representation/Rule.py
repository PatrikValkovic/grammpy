#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:45
:Licence MIT
Part of grammpy

"""

from typing import Any, List, TYPE_CHECKING

from .support._MetaRule import _MetaRule
from .support._WeakList import _WeakList

if TYPE_CHECKING:  # pragma: no cover
    from .support._RuleConnectable import _RuleConnectable


class Rule(metaclass=_MetaRule):
    """
    Basic implementation of rules.
    For definition of rule, you can use following attributes:
    fromSymbol = EPSILON
    toSymbol = EPSILON
    left = [EPSILON]
    right = [EPSILON]
    rule = ([EPSILON], [EPSILON])
    rules = [([EPSILON], [EPSILON])]
    """

    def __init__(self):
        # type: () -> Rule
        """
        Create new instance of rule.
        """
        self._from_symbols = _WeakList()
        self._to_symbols = list()

    def __getattr__(self, name):
        # type: (str) -> Any
        """
        Handle special attributes: toSymbol fromSymbol left right rule rules.
        For the rest throws AttributeError.
        :param name: Name of the attribute to find.
        :throw AttributeError:
        """
        if name in {'toSymbol',
                    'fromSymbol',
                    'left',
                    'right',
                    'rule',
                    'rules'}:
            return getattr(self.__class__, name)
        raise AttributeError

    @property
    def from_symbols(self):
        # type: () -> List[_RuleConnectable]
        """
        Instances that the rule derived from.
        :return: List of symbols.
        """
        return list(self._from_symbols)

    @property
    def to_symbols(self):
        # type: () -> List[_RuleConnectable]
        """
        Instances that the rule derived to.
        :return: List of symbols.
        """
        return self._to_symbols
