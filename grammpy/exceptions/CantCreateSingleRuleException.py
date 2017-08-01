#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .CannotConvertException import CannotConvertException


class CantCreateSingleRuleException(CannotConvertException):
    def __init__(self, rules):
        self.rules = rules
