#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 11:18
:Licence GNUv3
Part of grammpy

"""

from ..WeakList import WeakList
from .ValidationRule import ValidationRule


class InstantiableRule(ValidationRule):
    def __init__(self):
        self._from_symbols = WeakList()
        self._to_symbols = list()

    @property
    def from_symbols(self):
        return list(self._from_symbols)

    @property
    def to_symbols(self):
        return self._to_symbols