#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 28.07.2017 09:14
:Licence GNUv3
Part of grammpy

"""

import weakref
from .exceptions import TreeDeletedException


class Nonterminal:
    def __init__(self):
        self._from_rule = None
        self._to_rule = None

    @property
    def from_rule(self):
        if self._from_rule() is None:
            raise TreeDeletedException()
        return self._from_rule()

    @property
    def to_rule(self):
        return self._to_rule

    def _set_from_rule(self, r):
        self._from_rule = weakref.ref(r)

    def _set_to_rule(self, r):
        self._to_rule = r
