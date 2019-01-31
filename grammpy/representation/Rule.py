#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:45
:Licence GNUv3
Part of grammpy

"""

from .support._WeakList import _WeakList
from .support._MetaRule import _MetaRule


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
        self._from_symbols = _WeakList()
        self._to_symbols = list()

    def __getattr__(self, name):
        if name in {'toSymbol',
                    'fromSymbol',
                    'left',
                    'right',
                    'rule',
                    'rules'}:
            return getattr(self.__class__, name)
        raise AttributeError

    def __hash__(self) -> int:
        return hash(self.__class__)

    def __eq__(self, o: object) -> bool:
        return hash(self) == hash(o)

    @property
    def from_symbols(self):
        """
        Instances of the left side of the rule
        :return: List of symbols
        """
        return list(self._from_symbols)

    @property
    def to_symbols(self):
        """
        Instances of the right side of the rule
        :return: List of symbols
        """
        return self._to_symbols
