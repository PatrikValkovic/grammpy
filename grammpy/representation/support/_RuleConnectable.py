#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.01.2019 13:48
:Licence GPLv3
Part of grammpy

"""

import weakref
from ...exceptions import TreeDeletedException


class _RuleConnectable:
    """
    Represent entity that can be connected by Rule in the AST
    """

    def __init__(self):
        self._from_rule = None
        self._to_rule = None

    @property
    def from_rule(self):
        """
        Rule symbol is rewrite from
        :return: Instance of Rule
        """
        if self._from_rule is None:
            return None
        if self._from_rule() is None:
            raise TreeDeletedException()
        return self._from_rule()

    @property
    def to_rule(self):
        """
        Rule symbol is rewrite to
        :return: Instance of Rule
        """
        return self._to_rule

    def _set_from_rule(self, r):
        """
        Set rule symbol is rewrite from
        :param r: Instance of Rule
        """
        self._from_rule = weakref.ref(r)

    def _set_to_rule(self, r):
        """
        Set rule symbol is rewrite to
        :param r: Instance of Rule
        """
        self._to_rule = r
