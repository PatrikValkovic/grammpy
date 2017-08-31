#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 11:18
:Licence GNUv3
Part of grammpy

"""

from ..WeakList import WeakList
from .IsMethodsRuleExtension import IsMethodsRuleExtension


class InstantiableRule(IsMethodsRuleExtension):
    def __init__(self):
        self._from_nonterms = WeakList()
        self._to_nonterms = list()

    @property
    def from_nonterms(self):
        return list(self._from_nonterms)

    @property
    def to_nonterms(self):
        return self._to_nonterms